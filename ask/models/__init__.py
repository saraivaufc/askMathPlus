# -*- encoding: utf-8 -*-



#IMPORTS PYTHON
from datetime import datetime
import unicodedata

#IMPORTS DJANGO
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.core.urlresolvers import reverse

#IMPORTS SPIRIT

#IMPORTS USER_PROFILE_SPIRIT
from spirit_user_profile.models import User

#IMPORTS ASK
from ask.utils import *



#CHOICES
POSICAOMETRO = (
		(1, "TOPO"),
		(2, "MEIO"),
		(3, "BAIXO"),
	)
TAMANHOMETRO = (
	(1, "PEQUENO"),
	(2, "GRANDE"),
)

ITENS = (
	(1, "ITEM A"),
	(2, "ITEM B"),
	(3, "ITEM C"),
	(4, "ITEM D"),
	(5, "ITEM E"),
)


class Model(models.Model):	
	criacao = models.DateTimeField(default=datetime.now, blank=True,null = True, verbose_name="Criacao")
	def __unicode__(self):
		return format(self.criacao, "%d/%m/%Y %H:%M:%S")

	class Meta:
		verbose_name = "Modelo Genérico"
		verbose_name_plural = "Modelos Genéricos"

class Turma(Model):
	disciplina = models.CharField(max_length=255 , verbose_name="Disciplina",  help_text="Coloque aqui o nome a disciplina dessa turma.")
	semestre = models.FloatField(verbose_name="Semestre",  help_text="Coloque aqui o semestre que essa disciplina do item anterior esta sendo cursada.");
	professor = models.CharField(max_length=255 , verbose_name="Professor",  help_text="Escrevao nome do Professor que esta dando essa disciplina.")


	def __unicode__(self):
		return str(self.semestre) + ": " + self.disciplina + ":" + self.professor

	class Meta:
		ordering = ['-semestre']
		verbose_name = "Turma"
		verbose_name_plural = "Turmas"

class Usuario(User):
	turma = models.ForeignKey('Turma', null= True, blank= True, verbose_name="Turma", on_delete = models.SET_NULL,  help_text="Escolha a turma que o aluno pertence.")

	def __unicode__(self):
		return self.first_name +" " + self.last_name

	class Meta:
		verbose_name = "Usuário"
		verbose_name_plural = "usuários"

class Conteudo(Model):
	turma = models.ManyToManyField('Turma', null= True, blank=True , verbose_name="Turma", help_text="Escolha as turmas que esse conteudo pertence.")
	tema = models.CharField(max_length=255 , unique=True, verbose_name="Tema", help_text="Escolha um tema para o conteudo.")
	descricao = models.TextField(verbose_name="Descrição", help_text="Escreva uma descriçao sobre o assunto do conteudo")
	pergunta_inicial = models.ForeignKey('Pergunta',  null=True , blank=True , verbose_name="Pergunta Inicial", on_delete = models.SET_NULL, help_text="Todo conteudo precisa ter uma pergunta inicial.")
	requisitos = models.ManyToManyField('Conteudo',related_name="Requisitos",null=True , blank=True, verbose_name="Requisitos", help_text="Escolha aqui os conteudo que e recomendado a concluçao antes de seguir para esse.")
	sugestao_estudo = models.ManyToManyField('Conteudo',related_name="Sugestoes",null=True , blank=True,verbose_name="Sugestao Estudo", help_text="Escolha aqui quais conteudo o usuario deve seguir apos concluir esse.")
	max_pulos = models.IntegerField(verbose_name="Maximo de Pulos", help_text="Coloque aqui a quantidade de pulos que o usuario pode realizar nesse conteudo.")

	linha_metro = models.IntegerField(verbose_name="Posição Metro",choices=POSICAOMETRO, help_text="Escolha em qual posicao esse conteudo sera exibido.");
	tamanho_metro = models.IntegerField(verbose_name="Tamanho Metro",choices=TAMANHOMETRO, help_text="Escolha o tamanho do azulejo que esse conteudo sera exibido.");
	
	
	def __unicode__(self):
		return  self.tema
	
	class Meta:
		ordering = ['-criacao']
		verbose_name = "Conteudo"
		verbose_name_plural = "Conteudos"
	
	def clean(self):
		if self.pergunta_inicial_id != None:
			pergunta = Pergunta.objects.get(id = self.pergunta_inicial_id)
			if self.id != pergunta.conteudo_pertence_id:
				raise ValidationError("A Pergunta Inicial Não Pertence a esse Conteúdo.")

	def getTema(self):
		return transform_tema_revert(self.tema)
	def getDescricao(self):
		return string_to_latex(self.descricao)

	def getDescricaoMin(self):
		return minimize_frase(self.descricao)
	getDescricaoMin.short_description = 'Descrição'
	


	#GETS
	def getQuantPerguntasTotal(self):
		return len(self.getPerguntasOrdenadas())

	def getPerguntasOrdenadas(self):
		print "getPerguntasOrdenadas"
		perguntas = []
		perguntas_vistas = []
		if self.pergunta_inicial_id != None:
			pergunta_inicial =  Pergunta.objects.get(id = self.pergunta_inicial_id)
			perguntas.append(pergunta_inicial)
			perguntas_vistas.append(pergunta_inicial.id)

			while perguntas[len(perguntas)-1].pergunta_proximo_id != None:
				pergunta_proximo = Pergunta.objects.get(id = perguntas[len(perguntas)-1].pergunta_proximo_id)
				if pergunta_proximo.id in perguntas_vistas:
					break
				perguntas.append(pergunta_proximo)
				perguntas_vistas.append(pergunta_proximo.id)
				
		return perguntas

	def getPerguntasNaoOrdenadas(self):
		print "getPerguntasNaoOrdenadas"
		perguntas_all = Pergunta.objects.filter(conteudo_pertence_id = self.id)
		print len(perguntas_all) , "casa"
		perguntas_ordenadas = self.getPerguntasOrdenadas()
		print len(perguntas_ordenadas)
		perguntas_nao_ordenadas = []
		for i in perguntas_all:
			cotem = False
			for k in perguntas_ordenadas:
				if i.id == k.id:
					cotem = True
			if cotem == False:
				perguntas_nao_ordenadas.append(i)
		return perguntas_nao_ordenadas


	def getRequisitos(self):
		return self.requisitos.all()

	def getSugestoes(self):
		return self.sugestao_estudo.all()

	def getQuantPulosRealizados(self, usuario):
		pulos = Pulo.objects.filter(usuario = usuario.id, conteudo = self.id)
		if pulos != None:
			return len(pulos)
		else:
			return 0

	def getQuantPulosRestantes(self, usuario):
		try:
			pulos = Pontuacao.objects.get(usuario = usuario.id, conteudo = self.id)
		except:
			pulos = Pontuacao.objects.create(
				usuario_id = usuario.id,
				conteudo_id = self.id,
				pulosMaximo = self.max_pulos,
				pulosRestantes = self.max_pulos,
			)
			print 'Pontuacao Criada'
			pulos.save()
			return self.max_pulos
		return  pulos.pulosRestantes

	def inclementaPulosRestantes(self, usuario):
		try:
			pulos = Pontuacao.objects.get(usuario = usuario.id, conteudo = self.id)
		except:
			print "Impossivel encontrar Pontuacao em Inclementar Pulos Restantes"
			return
		pulos.inclementaPulosRestantes()

	def declementaPulosRestantes(self, usuario):
		try:
			pulos = Pontuacao.objects.get(usuario = usuario.id, conteudo = self.id)
		except:
			print "Impossivel encontrar Pontuacao em Declementar Pulos Restantes"
			return
		pulos.declementaPulosRestantes()


	def getPerguntasRespondidas(self, usuario):
		his = Historico.objects.filter(conteudo = self.id, usuario = usuario.id)
		per = []
		for i in his:
			existe = False
			for k in per:
				if k.id == i.pergunta_id:
					existe = True
			if existe == False:
				per.append(Pergunta.objects.get(id = i.pergunta_id))
		return per

	def getPerguntasNaoRespondidas(self, usuario):
		respondidas = self.getPerguntasRespondidas(usuario)
		nao_respondidas = []
		for i in self.getPerguntasOrdenadas():
			existe = False
			for k in respondidas:
				if i.id == k.id:
					existe = True			
			if existe == False:
				nao_respondidas.append(i)
		return nao_respondidas


	def getPerguntasCertas(self, usuario):
		his = Historico.objects.filter(conteudo = self.id, usuario = usuario.id, acertou = True)
		per = []
		for i in his:
			existe = False
			for k in per:
				if k.id == i.pergunta_id:
					existe = True
			if existe == False:
				per.append(Pergunta.objects.get(id = i.pergunta_id))
		return per

	def getPerguntasErradas(self, usuario):
		try:
			his = Historico.objects.all()[0]
		except:
			return []
		conteudo = Conteudo.objects.get(id = self.id)
		his = his.getRecente(usuario, conteudo)
		per = []
		for i in his:
			existe = False
			for k in per:
				if k.id == i.pergunta_id:
					existe = True
					break
			if (existe == False) and (i.acertou == False) :
				per.append(Pergunta.objects.get(id = i.pergunta_id))
		return per


	def getPerguntasPuladas(self, usuario):
		pulos = Pulo.objects.filter(usuario = usuario.id, conteudo = self.id)
		res = []
		for p in pulos:
			existe = False
			for k in res:
				if k.id == p.pergunta_id:
					existe = True
			if existe == False:
				res.append(Pergunta.objects.get(id = p.pergunta_id))

		resFinal = []
		for i in res:
			respondida = False
			for k in self.getPerguntasCertas(usuario):
				if i.id == k.id:
					respondida = True
			if respondida == False:
				resFinal.append(i)

		return resFinal

	def getPerguntasPuladasExclude(self, usuario, pergunta_id):
		p = self.getPerguntasPuladas(usuario)
		k = []
		for i in p:
			if i.id != pergunta_id:
				k.append(i)
		return k

	def getPerguntasRestantes(self, usuario):
		nao_respondidas = self.getPerguntasNaoRespondidas(usuario)
		erradas = self.getPerguntasErradas(usuario)
		todas = []
		for i in erradas:
			todas.append(i)
		for i in nao_respondidas:
			todas.append(i)
		return todas

	def getVezesPediuAjuda(self, usuario):
		return Busca_Ajuda.objects.filter(usuario=usuario.id, conteudo= self.id).count()

	def getQuantPontos(self, usuario):
		try:
			pontuacao = Pontuacao.objects.get(usuario = usuario.id,
													 conteudo = self.id,
													 )
		except:
			pontuacao = Pontuacao.objects.create(usuario_id = usuario.id,
														conteudo_id = self.id,
														pulosMaximo = self.max_pulos,
														pulosRestantes = self.max_pulos)
			pontuacao.save()
		return pontuacao.pontos

	
class Pergunta(Model):
	conteudo_pertence = models.ForeignKey(Conteudo, verbose_name="Conteudo Pertence",null=True , blank=False, on_delete = models.SET_NULL,  help_text="Escolha aqui o  conteudo ao qual esta pergunta esta associada.")
	descricao = models.TextField(verbose_name="Descrição",  help_text="Escreva uma descricao para a pergunta.")
	item_a =  models.TextField(null= True,  blank= True,  verbose_name="Item A",  help_text="Escreva o Item A.")
	deficiencia_a =  models.TextField(null= True,  blank= True,  verbose_name="Deficiencia A",  help_text="Escreva a Deficiencia do Item  A.")
	
	item_b =  models.TextField(null= True,  blank= True,  verbose_name="Item B",  help_text="Escreva o Item B.")
	deficiencia_b =  models.TextField(null= True,  blank= True,  verbose_name="Deficiencia B",  help_text="Escreva a Deficiencia do Item  B.")
	
	item_c =  models.TextField(null= True,  blank= True,  verbose_name="Item C",  help_text="Escreva o Item C.")
	deficiencia_c =  models.TextField(null= True,  blank= True,  verbose_name="Deficiencia C",  help_text="Escreva a Deficiencia do Item  C.")

	item_d =  models.TextField(null= True,  blank= True,  verbose_name="Item D",  help_text="Escreva o Item D.")
	deficiencia_d =  models.TextField(null= True,  blank= True,  verbose_name="Deficiencia D",  help_text="Escreva a Deficiencia do Item  D.")

	item_e =  models.TextField(null= True,  blank= True,  verbose_name="Item E",  help_text="Escreva o Item E.")
	deficiencia_e =  models.TextField(null= True,  blank= True,  verbose_name="Deficiencia E",  help_text="Escreva a Deficiencia do Item  E.")

	item_correto = models.IntegerField(null = True, blank = True, verbose_name="Item Correto", help_text="Diga qual dos itens e o correto.", choices=ITENS)
	pergunta_proximo = models.ForeignKey('Pergunta' ,related_name="proxima pergunta" , null=True , blank=True, verbose_name="Pergunta Proximo", on_delete = models.SET_NULL,  help_text="Escolha a pergunta na qual o usuario seguira apos responder essa.")
	ajuda = models.TextField(null= True,  blank= True,  verbose_name="Ajuda",  help_text="Se desejar, pode adicionar uma ajuda para essa pergunta.")
	pontos = models.IntegerField(verbose_name="Pontos Valem",  help_text="Digite aqui a quantidade de pontos que a pergunta vale.")


	def __unicode__(self):
		return self.getDescricaoMin()
	
	class Meta:
		ordering = ['-conteudo_pertence']
		verbose_name = "Pergunta"
		verbose_name_plural = "Perguntas"

	def clean(self):
		if self.item_correto != None:
			if self.item_correto == 1 and self.item_a == None:
				raise ValidationError("Item Correto Esta em Branco")
			elif self.item_correto == 2 and self.item_b == None:
				raise ValidationError("Item Correto Esta em Branco")
			elif self.item_correto == 3 and self.item_c == None:
				raise ValidationError("Item Correto Esta em Branco")
			elif self.item_correto == 4 and self.item_d == None:
				raise ValidationError("Item Correto Esta em Branco")
			elif self.item_correto == 5 and self.item_e == None:
				raise ValidationError("Item Correto Esta em Branco")

		if self.pergunta_proximo_id != None:
			pergunta = Pergunta.objects.get(id = self.pergunta_proximo_id)
			if pergunta.conteudo_pertence_id != self.conteudo_pertence_id:
				raise ValidationError('A Proxima Pergunta Não Pertence ao Conteúdo dessa Pergunta.')

	def pediuAjuda(self, usuario):
		try:
			b = Busca_Ajuda.objects.create(
					usuario = usuario.id,
					pergunta = self.id,
				)
			b.save()
		except:
			print "pediuAjuda() Falhou!!!!"

	def getDescricao(self):
		quant = 0
		des = ""
		add = False
		for i in self.descricao:
			if quant < 100:
				des += i
			else:
				add = True
				break
			quant+=1
		if add:
			des +="..."
		return string_to_latex(des)

	def getDescricaoMin(self):
		return minimize_frase(self.descricao)
	getDescricaoMin.short_description = 'Descrição'

	def getItemCorreto(self):
		return self.item_correto

	def getDescricaoItemCorreto(self):
		if self.item_correto == 1:
			return minimize_frase(self.item_a)
		elif self.item_correto == 2:
			return minimize_frase(self.item_b)
		elif self.item_correto == 3:
			return minimize_frase(self.item_c)
		elif self.item_correto == 4:
			return minimize_frase(self.item_d)
		elif self.item_correto == 5:
			return minimize_frase(self.item_e)
		else:
			return None
		

	def getItens(self):
		itens = {}
		if self.item_a != '':
			try:
				itens[1]=self.item_a
			except:
				pass
		if self.item_b != '':
			try:
				itens[2]=self.item_b
			except:
				pass
		if self.item_c != '':
			try:
				itens[3]=self.item_c
			except:
				pass
		if self.item_d != '':
			try:
				itens[4]= self.item_d
			except:
				pass
		if self.item_e!= '':
			try:
				itens[5]= self.item_e
			except:
				pass
		return itens

		
		
		




	def acertou(self, usuario):
		pontuacao = None
		try:
			pontuacao = Pontuacao.objects.get(usuario = usuario.id, conteudo = self.conteudo_pertence )
		except:
			pontuacao = Pontuacao.objects.create(
				usuario = usuario.id,
				conteudo = self.conteudo_pertence,
				pulosRestantes = (Conteudo.objects.get(id = self.conteudo_pertence)).max_pulos,
			)
			pontuacao.save()
		finally:
			pontuacao.inclementaPontos(self.pontos)
			#Como ele acertou a questao, entao aumentamos a quantidade de acertos seguintos e 
			# zeramos a quantidade de erros seguindos
			pontuacao.inclementaAcertosSeguidos()
			pontuacao.zerarErrosSeguidos()

	def errou(self, usuario):
		pontuacao = None
		try:
			pontuacao = Pontuacao.objects.get(usuario = usuario.id, conteudo = self.conteudo_pertence )
		except:
			pontuacao = Pontuacao.objects.create(
				usuario = usuario.id,
				conteudo = self.conteudo_pertence,
				pulosRestantes = (Conteudo.objects.get(id = self.conteudo_pertence)).max_pulos,
			)
			pontuacao.save()
		finally:
			#Como ele errou a questao, entao aumentamos a quantidade de erros seguintos e 
			# zeramos a quantidade de acertos seguindos
			pontuacao.inclementaErrosSeguidos()
			pontuacao.zerarAcertosSeguidos()


class Busca_Ajuda(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuário", help_text="Escolha o usuário que pediu a ajuda.")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteudo", help_text="Escolha o conteúdo ao qual ele pediu a ajuda.")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta", help_text="Escolha a pergunta ao qual ele pediu ajuda.")

	def __unicode__(self):
		return str(self.usuario)
	class Meta:
		ordering = ['-criacao']
		verbose_name = "Busca Ajuda"
		verbose_name_plural = "Busca Ajudas"

class Historico(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuário")
	turma = models.ForeignKey(Turma, verbose_name="Turma")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteúdo")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta")
	item = models.IntegerField(verbose_name="Item")
	acertou = models.BooleanField(default=False, verbose_name="Acertou")

	def __unicode__(self):
		return  str(self.usuario)
	class Meta:
		ordering = ['-criacao']
		verbose_name = "Histórico do Usuário"
		verbose_name_plural = "Histórico dos Usuários"

	def getRecente(self, usuario, conteudo):
		todo = Historico.objects.filter(usuario = usuario.id, conteudo = conteudo.id).order_by('-criacao')
		recente = []
		for i in todo:
			existe = False
			for k in recente:
				if i.pergunta_id == k.pergunta_id:
					existe = True
			if existe == False:
				recente.append(i)
		return recente

class Estado_Usuario(Model):
	turma  = models.ForeignKey(Turma, verbose_name="Turma")
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo , verbose_name="Conteudo")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta")

	def __unicode__(self):
		return str(self.usuario)
	class Meta:
		ordering = ['usuario']
		verbose_name = "Estado do Usuário"
		verbose_name_plural = "Estado dos Usuários"

class Pulo(Model):
	turma  = models.ForeignKey(Turma, verbose_name="Turma")
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo , verbose_name="Conteudo")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta", null=True , blank=True, on_delete = models.SET_NULL)

	def __unicode__(self):
		return  str(self.usuario)
	class Meta:
		ordering = ['usuario']
		verbose_name = "Salto"
		verbose_name_plural = "Saltos"

class Pontuacao(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteudo")
	pontos = models.IntegerField(default=0, verbose_name="Pontos", null= True, blank=True)
	pulosMaximo = models.IntegerField(default=0, verbose_name="Pulos Maximo", null= True, blank=True)
	pulosRestantes = models.IntegerField(default=0, verbose_name="Pulos Restantes", null= True, blank=True)
	ganhou_bonus = models.BooleanField(default = False, verbose_name="Ganhou Bonus", blank=True)
	acertos_seguidos = models.IntegerField(default=0, verbose_name="Acertos Seguidos", null= True, blank=True)
	erros_seguidos = models.IntegerField(default=0, verbose_name="Erros Seguidos", null= True, blank=True)

	class Meta:
		verbose_name = "Pontuação"
		verbose_name_plural = "Pontuações"

	def __unicode__(self):
		return str(self.usuario)

	def inclementaPontos(self,valor):
		self.pontos += valor
		Pontuacao.objects.filter(id = self.id).update(pontos = self.pontos)

	def inclementaPulosRestantes(self):
		self.pulosRestantes += 1
		Pontuacao.objects.filter(id = self.id).update(pulosRestantes = self.pulosRestantes)

	def inclementaPulosMaximo(self):
		self.pulosMaximo += 1
		Pontuacao.objects.filter(id = self.id).update(pulosMaximo = self.pulosMaximo)
		self.inclementaPulosRestantes(self)

	def inclementaAcertosSeguidos(self):
		self.acertos_seguidos += 1
		if self.acertos_seguidos == 3:
			self.pontos += self.pontos
			self.inclementaPulosRestantes()
			try:
				Pontuacao.objects.filter(id = self.id).update(pontos = self.pontos, 
														  pulosMaximo = self.pulosMaximo,
														  pulosRestantes = self.pulosRestantes,
														  ganhou_bonus = True,
														  acertos_seguidos = 0,
														  )
			except:
				return
		else:
			Pontuacao.objects.filter(id = self.id).update(acertos_seguidos = self.acertos_seguidos)

	def inclementaErrosSeguidos(self):
		self.erros_seguidos += 1

		Pontuacao.objects.filter(id = self.id).update(erros_seguidos = self.erros_seguidos)

	def declementaPontos(self,valor):
		self.pontos -= valor
		if self.pontos < 0:
			self.pontos = 0

		Pontuacao.objects.filter(id = self.id).update(pontos = self.pontos)

	def declementaPulosRestantes(self):
		self.pulosRestantes -= 1
		if self.pulosRestantes < 0:
			self.pulosRestantes = 0
		Pontuacao.objects.filter(id = self.id).update(pulosRestantes = self.pulosRestantes)

	def declementaPulosMaximo(self):
		self.pulosMaximo -= 1
		if self.pulosMaximo < 0:
			self.pulosMaximo = 0
		Pontuacao.objects.filter(id = self.id).update(pulosMaximo = self.pulosMaximo)
		self.declementaPulosRestantes()

	def zerarAcertosSeguidos(self):
		Pontuacao.objects.filter(id = self.id).update(acertos_seguidos = 0)

	def zerarErrosSeguidos(self):
		Pontuacao.objects.filter(id = self.id).update(erros_seguidos = 0)

class Secao(models.Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo , verbose_name="Conteudo")
	
	inicio = models.DateTimeField(default=datetime.now, blank=True,null = True, verbose_name="Inicio")
	fim = models.DateTimeField(blank=True,null = True, verbose_name="Fim")

	class Meta:
		ordering = ['-inicio']
		verbose_name = "Seção"
		verbose_name_plural = "Seções"

	def iniciou(self):
		self.inicio = datetime.now()
		Secao.objects.filter(id = self.id).update(inicio = self.inicio)

	def terminou(self):
		self.fim = datetime.now()
		Secao.objects.filter(id = self.id).update(fim = self.fim)

		

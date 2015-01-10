# -*- encoding: utf-8 -*-

from django.db import models
from datetime import datetime
import unicodedata
from spirit_user_profile.models import User
from ask.utils import *
from django.core.exceptions import ValidationError

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
		return str(self.id) + ": " +  self.first_name +" " + self.last_name

	class Meta:
		verbose_name = "Usuário"
		verbose_name_plural = "usuários"

class Conteudo(Model):
	turma = models.ManyToManyField('Turma', verbose_name="Turma", help_text="Escolha as turmas que esse conteudo pertence.")
	tema = models.CharField(max_length=255 , unique=True, verbose_name="Tema", help_text="Escolha um tema para o conteudo.")
	descricao = models.TextField(null=True , blank=True, verbose_name="Descrição", help_text="Escreva uma descriçao sobre o assunto do conteudo")
	pergunta_inicial = models.ForeignKey('Pergunta',  null=True , blank=True , verbose_name="Pergunta Inicial", on_delete = models.SET_NULL, help_text="Todo conteudo precisa ter uma pergunta inicial.")
	requisitos = models.ManyToManyField('Conteudo',related_name="Requisitos",null=True , blank=True, verbose_name="Requisitos", help_text="Escolha aqui os conteudo que e recomendado a concluçao antes de seguir para esse.")
	sugestao_estudo = models.ManyToManyField('Conteudo',related_name="Sugestoes",null=True , blank=True,verbose_name="Sugestao Estudo", help_text="Escolha aqui quais conteudo o usuario deve seguir apos concluir esse.")
	max_pulos = models.IntegerField(verbose_name="Maximo de Pulos", help_text="Coloque aqui a quantidade de pulos que o usuario pode realizar nesse conteudo.")
	
	POSICAOMETRO = (
		(1, "TOPO"),
		(2, "MEIO"),
		(3, "BAIXO"),
	)
	TAMANHOMETRO = (
		(1, "PEQUENO"),
		(2, "GRANDE"),
	)

	linha_metro = models.IntegerField(verbose_name="Posição Metro", null=False , blank=False, choices=POSICAOMETRO, help_text="Escolha em qual posicao esse conteudo sera exibido.");
	tamanho_metro = models.IntegerField(verbose_name="Tamanho Metro", null=False , blank=False, choices=TAMANHOMETRO, help_text="Escolha o tamanho do azulejo que esse conteudo sera exibido.");
	
	def __unicode__(self):
		return  str(self.id) + ": " +  self.tema
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


	#GETS
	def getQuantPerguntasTotal(self):
		p = Pergunta.objects.filter(conteudo_pertence = self.id)
		return len(p)

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
		for i in Pergunta.objects.filter(conteudo_pertence = self.id):
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
			for k in self.getPerguntasRespondidas(usuario):
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
	conteudo_pertence = models.ForeignKey(Conteudo, verbose_name="Conteudo Pertence",null=True , blank=True, on_delete = models.SET_NULL,  help_text="Escolha aqui o  conteudo ao qual esta pergunta esta associada.")
	descricao = models.TextField(verbose_name="Descrição",  help_text="Escreva uma descricao para a pergunta.")
	item_correto = models.ForeignKey('Item', null=True , blank=True, verbose_name="Item Correto", on_delete = models.SET_NULL, help_text="Diga qual dos itens dela e o correto.(Toda Pergunta tem que ter um item correto!!!)")
	pergunta_proximo = models.ForeignKey('Pergunta' ,related_name="proxima pergunta" , null=True , blank=True, verbose_name="Pergunta Proximo", on_delete = models.SET_NULL,  help_text="Escolha a pergunta na qual o usuario seguira apos responder essa.")
	ajuda = models.ForeignKey('Ajuda', null=True , blank=True, verbose_name="Ajuda", on_delete = models.SET_NULL,  help_text="Se desejar, adicioner uma ajuda para o usuario.")
	pontos = models.IntegerField(verbose_name="Pontos Valem",  help_text="Digite aqui a quantidade de pontos que a pergunta vale.")


	def __unicode__(self):
		return str(self.id) + ": " +  self.getDescricaoMin()
	
	class Meta:
		ordering = ['-conteudo_pertence']
		verbose_name = "Pergunta"
		verbose_name_plural = "Perguntas"

	def clean(self):
		if self.item_correto_id != None:
			item = Item.objects.get(id = self.item_correto_id)
			if self.id != item.pergunta_pertence_id:
				raise ValidationError('O Item Correto Não Pertence a Essa Pergunta.')
		if self.ajuda_id != None:
			ajuda = Ajuda.objects.get(id = self.ajuda_id)
			if self.conteudo_pertence_id != None:
				if ajuda.conteudo_id != self.conteudo_pertence_id:
					raise ValidationError('Essa ajuda não pertence ao conteúdo dessa pergunta.')
		if self.pergunta_proximo_id != None:
			pergunta = Pergunta.objects.get(id = self.pergunta_proximo_id)
			if pergunta.conteudo_pertence_id != self.conteudo_pertence_id:
				raise ValidationError('A Proxima Pergunta Não Pertence ao Conteúdo dessa Pergunta.')

	def pediuAjuda(self, usuario):
		b = Busca_Ajuda.objects.create(
				usuario = usuario.id,
				pergunta = self.id,
			)
		b.save()

	def getDescricao(self):
		quant = 0
		des = ""
		for i in self.descricao:
			if quant < 255:
				des += i
			else:
				break
			quant+=1
		des +="..."
		return string_to_latex(des)

	def getDescricaoMin(self):
		quant = 0
		des = ""
		for i in self.descricao:
			if quant < 50:
				des += i
			else:
				break
			quant+=1
		des +="..."
		return des

	def getItemCorreto(self):
		if self.item_correto_id == None:
			return None
		else:
			try:
				item = Item.objects.get(id = self.item_correto_id)
			except:
				return None
			return item



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


class Item(Model):
	descricao = models.TextField(verbose_name="Descrição",  help_text="Escreva uma descricao para este item.")
	pergunta_pertence = models.ForeignKey(Pergunta , related_name='pertence', verbose_name="Pergunta Pertence",  help_text="Escolha a pergunta da qual ele esta associado.")
	deficiencia = models.ForeignKey("Deficiencia", verbose_name="Deficiencia", null = True, blank=True, on_delete=models.SET_NULL, help_text="Todo item errado pode possuir uma deficiencia, quando um aluno responder erroneamente uma pergunta, precisamos saber qual a deficiencia em relacao ao conteudo que ele esta tendo, e para isso, usamos o item que ele respondeu, ou seja, todo item errado esta relacionado com uma possivel deficiencia apresentada pelo aluno.")
	def __unicode__(self):
		return str(self.id) + ": " +  self.getDescricaoMin() 
	
	class Meta:
		ordering = ['-criacao']
		verbose_name = "Item"
		verbose_name_plural = "Itens"
	def clean(self):
		if self.deficiencia_id != None:
			deficiencia = Deficiencia.objects.get(id = self.deficiencia_id)
			pergunta = Pergunta.objects.get(id = self.pergunta_pertence_id)
			
			if deficiencia.conteudo_id != None and pergunta.conteudo_pertence_id != None:
				if deficiencia.conteudo_id != pergunta.conteudo_pertence_id:
					raise ValidationError('O Conteúdo ao qual a Deficiência pertence não corresponde ao Conteúdo ao qual a Pergunta Pertence.')

	def getDescricao(self):
		quant = 0
		des = ""
		for i in self.descricao:
			if quant < 255:
				des += i
			else:
				break
			quant+=1
		des +="..."
		return  string_to_latex(des)
		
	def getDescricaoMin(self):
		quant = 0
		des = ""
		for i in self.descricao:
			if quant < 50:
				des += i
			else:
				break
			quant+=1
		des +="..."
		return des


class Deficiencia(Model):
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteúdo",  help_text="Escolha o conteudo ao qual esta deficiencia esta relacionada.")
	descricao = models.TextField(verbose_name="Descrição",  help_text="Escreva uma descricao para essa deficiencia.")

	def __unicode__(self):
		return str(self.id) + ": " +  self.getDescricaoMin()
	
	class Meta:
		ordering = ['-conteudo']
		verbose_name = "Deficiência"
		verbose_name_plural = "Deficiências"

	def getDescricaoMin(self):
		quant = 0
		des = ""
		for i in self.descricao:
			if quant < 50:
				des += i
			else:
				break
			quant+=1
		des +="..."
		return des

	

class Ajuda(Model):
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteúdo",help_text="Escolha o conteúdo ao qual esta ajuda esta relacionada." )
	descricao = models.TextField(verbose_name="Descrição", help_text="Escreva uma descrição para essa ajuda.")
	
	def __unicode__(self):
		return str(self.id) + ": " +  self.getDescricaoMin()
	class Meta:
		ordering = ['-conteudo']
		verbose_name = "Ajuda"
		verbose_name_plural = "Ajudas"

	def getDescricaoMin(self):
		quant = 0
		des = ""
		for i in self.descricao:
			if quant < 50:
				des += i
			else:
				break
			quant+=1
		des +="..."
		return des

class Busca_Ajuda(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuário", help_text="Escolha o usuário que pediu a ajuda.")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteudo", help_text="Escolha o conteúdo ao qual ele pediu a ajuda.")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta", help_text="Escolha a pergunta ao qual ele pediu ajuda.")

	def __unicode__(self):
		return str(self.id) + str(self.usuario)
	class Meta:
		ordering = ['-criacao']
		verbose_name = "Busca Ajuda"
		verbose_name_plural = "Busca Ajudas"

class Historico(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuário")
	turma = models.ForeignKey(Turma, verbose_name="Turma")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteúdo")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta")
	item = models.ForeignKey(Item, verbose_name="Item",null=True , blank=True, on_delete = models.SET_NULL)
	acertou = models.BooleanField(default=False, verbose_name="Acertou")

	def __unicode__(self):
		return  str(self.id) + ": " +  str(self.usuario)
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
		return str(self.id) + ": " +  str(self.usuario)
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
		return str(self.id) + ": " +  str(self.usuario)
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
		return str(self.id) + ": " + str(self.usuario)

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

		

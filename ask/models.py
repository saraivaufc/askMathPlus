# -*- encoding: utf-8 -*-

from django.db import models
from datetime import datetime
import unicodedata
from spirit_user_profile.models import User
from utils import *


class Model(models.Model):	
	criacao = models.DateTimeField(default=datetime.now, blank=True,null = True, verbose_name="Criacao")
	def __unicode__(self):
		return format(self.criacao, "%d/%m/%Y %H:%M:%S")

class Turma(Model):
	disciplina = models.CharField(max_length=255 , verbose_name="Disciplina")
	semestre = models.FloatField(verbose_name="Semestre");
	professor = models.CharField(max_length=255 , verbose_name="Professor")

	def __unicode__(self):
		return str(self.semestre) + ": " + self.disciplina + ":" + self.professor

	class Meta:
		ordering = ['-semestre']

class Usuario(User):
	turma = models.ForeignKey('Turma', null= True, blank= True, verbose_name="Turma", on_delete = models.SET_NULL)

	def __unicode__(self):
		return str(self.id) + ": " +  self.first_name +" " + self.last_name

class Conteudo(Model):
	turma = models.ManyToManyField('Turma', verbose_name="Turma")
	tema = models.CharField(max_length=255 , unique=True, verbose_name="Tema")
	descricao = models.TextField(null=True , blank=True, verbose_name="Descrição")
	pergunta_inicial = models.ForeignKey('Pergunta',  null=True , blank=True , verbose_name="Pergunta Inicial", on_delete = models.SET_NULL)
	requisitos = models.ManyToManyField('Conteudo',related_name="Requisitos",null=True , blank=True, verbose_name="Requisitos")
	sugestao_estudo = models.ManyToManyField('Conteudo',related_name="Sugestoes",null=True , blank=True,verbose_name="Sugestao Estudo")
	max_pulos = models.IntegerField(verbose_name="Maximo de Pulos")
	linha_metro = models.IntegerField(verbose_name="Posição Metro", null=False , blank=False);
	tamanho_metro = models.IntegerField(verbose_name="Tamanho Metro", null=False , blank=False);
	
	def __unicode__(self):
		return  str(self.id) + ": " +  self.tema
	class Meta:
		ordering = ['-criacao']

	def getTema(self):
		return transform_tema_revert(self.tema)


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
	conteudo_pertence = models.ForeignKey(Conteudo, verbose_name="Conteudo Pertence",null=True , blank=True, on_delete = models.SET_NULL)
	descricao = models.TextField(verbose_name="Descrição")
	item_correto = models.ForeignKey('Item', null=True , blank=True, verbose_name="Item Correto", on_delete = models.SET_NULL)
	pergunta_proximo = models.ForeignKey('Pergunta' ,related_name="proxima pergunta" , null=True , blank=True, verbose_name="Pergunta Proximo", on_delete = models.SET_NULL)
	ajuda = models.ForeignKey('Ajuda', null=True , blank=True, verbose_name="Ajuda", on_delete = models.SET_NULL)
	pontos = models.IntegerField(verbose_name="Pontos Valem")

	def __unicode__(self):
		return str(self.id) + ": " +  self.getDescricao()
	class Meta:
		ordering = ['-conteudo_pertence']

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
	descricao = models.TextField(verbose_name="Descrição")
	pergunta_pertence = models.ForeignKey(Pergunta , related_name='pertence', verbose_name="Pergunta Pertence")
	deficiencia = models.ForeignKey("Deficiencia", verbose_name="Deficiencia", null = True, blank=True, on_delete=models.SET_NULL)
	def __unicode__(self):
		return str(self.id) + ": " +  self.descricao 
	
	class Meta:
		ordering = ['-criacao']

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
		return des


class Deficiencia(Model):
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteúdo")
	descricao = models.TextField(verbose_name="Descrição")

	def __unicode__(self):
		return str(self.id) + ": " +  self.descricao 
	
	class Meta:
		ordering = ['-conteudo']	

class Ajuda(Model):
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteúdo")
	descricao = models.TextField(verbose_name="Descrição")
	def __unicode__(self):
		return str(self.id) + ": " +  self.descricao
	class Meta:
		ordering = ['-conteudo']

class Busca_Ajuda(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuário")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Pergunta")

	def __unicode__(self):
		return str(self.id) + str(self.usuario)
	class Meta:
		ordering = ['-criacao']

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

class Pulo(Model):
	turma  = models.ForeignKey(Turma, verbose_name="Turma")
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo , verbose_name="Conteudo")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta", null=True , blank=True, on_delete = models.SET_NULL)

	def __unicode__(self):
		return str(self.id) + ": " +  str(self.usuario)
	class Meta:
		ordering = ['usuario']

class Pontuacao(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteudo")
	pontos = models.IntegerField(default=0, verbose_name="Pontos", null= True, blank=True)
	pulosMaximo = models.IntegerField(default=0, verbose_name="Pulos Maximo", null= True, blank=True)
	pulosRestantes = models.IntegerField(default=0, verbose_name="Pulos Restantes", null= True, blank=True)
	ganhou_bonus = models.BooleanField(default = False, verbose_name="Ganhou Bonus", blank=True)
	acertos_seguidos = models.IntegerField(default=0, verbose_name="Acertos Seguidos", null= True, blank=True)
	erros_seguidos = models.IntegerField(default=0, verbose_name="Erros Seguidos", null= True, blank=True)


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

	def iniciou(self):
		self.inicio = datetime.now()
		Secao.objects.filter(id = self.id).update(inicio = self.inicio)

	def terminou(self):
		self.fim = datetime.now()
		Secao.objects.filter(id = self.id).update(fim = self.fim)

		

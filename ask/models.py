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
	nome = models.CharField(max_length=255 , verbose_name="Nome")
	semestre = models.FloatField(verbose_name="Semestre");

	def __unicode__(self):
		return str(self.id) + ": " + self.nome

	class Meta:
		ordering = ['-semestre']


class Usuario(User):
	turma = models.ForeignKey('Turma', null= True, blank= True, verbose_name="Turma")

	def __unicode__(self):
		return str(self.id) + ": " +  self.first_name +" " + self.last_name


class Conteudo(Model):
	turma = models.ManyToManyField('Turma', verbose_name="Turma")
	tema = models.CharField(max_length=255 , unique=True, verbose_name="Tema")
	descricao = models.TextField(null=True , blank=True, verbose_name="Descrição")
	pergunta_inicial = models.ForeignKey('Pergunta' , null=True , blank=True , verbose_name="Pergunta Inicial")
	requisitos = models.ManyToManyField('Conteudo',related_name="Requisitos",null=True , blank=True, verbose_name="Requisitos")
	sugestao_estudo = models.ManyToManyField('Conteudo',related_name="Sugestoes",null=True , blank=True,verbose_name="Sugestao Estudo")
	max_pulos = models.IntegerField(verbose_name="Maximo de Pulos")
	linha_metro = models.IntegerField(verbose_name="Posição Metro", null=False , blank=False);
	tamanho_metro = models.IntegerField(verbose_name="Tamanho Metro", null=False , blank=False);
	
	def __unicode__(self):
		return  str(self.id) + ": " +  self.tema
	class Meta:
		ordering = ['tema']

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
			pulos = UsuarioPontuacao.objects.get(usuario = usuario.id, conteudo = self.id)
		except:
			pulos = UsuarioPontuacao.objects.create(
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
			pulos = UsuarioPontuacao.objects.get(usuario = usuario.id, conteudo = self.id)
		except:
			print "Impossivel encontrar Pontuacao em Inclementar Pulos Restantes"
			return
		pulos.inclementaPulosRestantes()

	def declementaPulosRestantes(self, usuario):
		try:
			pulos = UsuarioPontuacao.objects.get(usuario = usuario.id, conteudo = self.id)
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
			pontuacao = UsuarioPontuacao.objects.get(usuario = usuario.id,
													 conteudo = self.id,
													 )
		except:
			pontuacao = UsuarioPontuacao.objects.create(usuario_id = usuario.id,
														conteudo_id = self.id,
														pulosMaximo = self.max_pulos,
														pulosRestantes = self.max_pulos)
			pontuacao.save()
		return pontuacao.pontos


	
class Pergunta(Model):
	conteudo_pertence = models.ForeignKey(Conteudo, verbose_name="Conteudo Pertence")
	descricao = models.TextField(verbose_name="Descrição")
	item_correto = models.ForeignKey('Item', null=True , blank=True, verbose_name="Item Correto")
	pergunta_proximo_acertou = models.ForeignKey('Pergunta' ,related_name="proximo_acertou" , null=True , blank=True, verbose_name="Pergunta Proximo Acertou")
	pergunta_proximo_errou = models.ForeignKey('Pergunta' ,related_name="proximo_errou" , null=True , blank=True, verbose_name="Pergunta Proximo Errou")
	ajuda = models.ForeignKey('Ajuda', null=True , blank=True, verbose_name="Ajuda")
	pontos = models.IntegerField(verbose_name="Pontos Valem")

	def __unicode__(self):
		return str(self.id) + ": " +  self.getDescricao()
	class Meta:
		ordering = ['-criacao']

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



	def acertou(self, usuario):
		pontuacao = None
		try:
			pontuacao = UsuarioPontuacao.objects.get(usuario = usuario.id, conteudo = self.conteudo_pertence )
		except:
			pontuacao = UsuarioPontuacao.objects.create(
				usuario = usuario.id,
				conteudo = self.conteudo_pertence,
				pulosRestantes = (Conteudo.objects.get(id = self.conteudo_pertence)).max_pulos,
			)
			pontuacao.save()
		finally:
			pontuacao.inclementaPontos(self.pontos)







class Item(Model):
	descricao = models.TextField(verbose_name="Descrição")
	pergunta_pertence = models.ForeignKey(Pergunta , related_name='pertence', verbose_name="Pergunta Pertence")

	def __unicode__(self):
		return str(self.id) + ": " +  self.descricao 
	
	class Meta:
		ordering = ['-criacao']



class Ajuda(Model):
	descricao = models.TextField(verbose_name="Descrição")
	def __unicode__(self):
		return str(self.id) + ": " +  self.descricao
	class Meta:
		ordering = ['-criacao']

class Busca_Ajuda(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuário")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Pergunta")

	def __unicode__(self):
		return str(self.id) + str(self.usuario)
	class Meta:
		ordering = ['usuario']

class Historico(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuário")
	turma = models.ForeignKey(Turma, verbose_name="Turma")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteúdo")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta")
	item = models.ForeignKey(Item, verbose_name="Item")
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
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta")

	def __unicode__(self):
		return str(self.id) + ": " +  str(self.usuario)
	class Meta:
		ordering = ['usuario']


class UsuarioPontuacao(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteudo")
	pontos = models.IntegerField(default=0, verbose_name="Pontos",null=True , blank=True)
	pulosMaximo = models.IntegerField(default=0, verbose_name="Pulos Maximo", null= True, blank=True)
	pulosRestantes = models.IntegerField(default=0, verbose_name="Pulos Restantes", null= True, blank=True)

	def __unicode__(self):
		return str(self.id) + ": " + str(self.usuario)

	def inclementaPontos(self,valor):
		self.pontos += valor
		UsuarioPontuacao.objects.filter(id = self.id).update(pontos = self.pontos)

	def inclementaPulosRestantes(self):
		self.pulosRestantes += 1 
		UsuarioPontuacao.objects.filter(id = self.id).update(pulosRestantes = self.pulosRestantes)

	def inclementaPulosMaximo(self):
		self.pulosMaximo += 1
		UsuarioPontuacao.objects.filter(id = self.id).update(pulosMaximo = self.pulosMaximo)
		self.inclementaPulosRestantes(self)

	def declementaPontos(self,valor):
		self.pontos -= valor
		if self.pontos < 0:
			self.pontos = 0

		UsuarioPontuacao.objects.filter(id = self.id).update(pontos = self.pontos)

	def declementaPulosRestantes(self):
		self.pulosRestantes -= 1
		if self.pulosRestantes < 0:
			self.pulosRestantes = 0
		UsuarioPontuacao.objects.filter(id = self.id).update(pulosRestantes = self.pulosRestantes)

	def declementaPulosMaximo(self):
		self.pulosMaximo -= 1
		if self.pulosMaximo < 0:
			self.pulosMaximo = 0
		UsuarioPontuacao.objects.filter(id = self.id).update(pulosMaximo = self.pulosMaximo)
		self.declementaPulosRestantes()




		

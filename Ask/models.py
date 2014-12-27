# -*- encoding: utf-8 -*-

from django.db import models
from datetime import datetime
import unicodedata
from spirit_user_profile.models import User


class Model(models.Model):	
	criacao = models.DateTimeField(default=datetime.now, blank=True,null = True, verbose_name="Criacao")
	def __unicode__(self):
		return format(self.criacao, "%d/%m/%Y %H:%M:%S")


class Turma(Model):
	nome = models.CharField(max_length=255 , verbose_name="Nome")
	semestre = models.FloatField(verbose_name="Semestre");

	def __unicode__(self):
		return self.nome

	class Meta:
		ordering = ['-semestre']


class Usuario(User):
	turma = models.ForeignKey('Turma', null= True, blank= True, verbose_name="Turma")

	def __unicode__(self):
		return self.first_name +" " + self.last_name


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
		return self.tema
	class Meta:
		ordering = ['tema']


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
			return self.max_pulos
		return  pulos.pulosRestantes

	def inclementaPulosRestantes(self, usuario):
		pulos = UsuarioPontuacao.objects.get(usuario = usuario.id, conteudo = self.id)
		pulos.inclementaPulos()

	def declementaPulosRestantes(self, usuario):
		pulos = UsuarioPontuacao.objects.get(usuario = usuario.id, conteudo = self.id)
		pulos.declementaPulos()


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
		print "\n\nPergunta que foram respondidas", len(respondidas)
		nao_respondidas = []
		for i in Pergunta.objects.filter(conteudo_pertence = self.id):
			existe = False
			for k in respondidas:
				if i.id == k.id:
					existe = True			
			if existe == False:
				nao_respondidas.append(i)
		print "Perguntas nao respondiasassaa", len(nao_respondidas)
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
		his = Historico.objects.filter(conteudo = self.id, usuario = usuario.id, acertou = False)
		per = []
		for i in his:
			existe = False
			for k in per:
				if k.id == i.pergunta_id:
					existe = True
			if existe == False:
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
		return res

	def getPerguntasRestantes(self, usuario):
		nao_respondidas = self.getPerguntasNaoRespondidas(usuario)
		erradas = self.getPerguntasErradas(usuario)
		print "\n\nDetalhe getPerguntasRestantes\n"
		print "Pergunta nao respondidas", len(nao_respondidas)
		print "Pergunta erradas", len(erradas)
		print "\n\n"

		todas = []
		for i in nao_respondidas:
			todas.append(i)
		for i in erradas:
			todas.append(i)

		print "Perguntas Restantes", len(todas)
		
		return todas


	
class Pergunta(Model):
	conteudo_pertence = models.ForeignKey(Conteudo, verbose_name="Conteudo Pertence")
	descricao = models.TextField(verbose_name="Descrição")
	item_correto = models.ForeignKey('Item', null=True , blank=True, verbose_name="Item Correto")
	pergunta_proximo_acertou = models.ForeignKey('Pergunta' ,related_name="proximo_acertou" , null=True , blank=True, verbose_name="Pergunta Proximo Acertou")
	pergunta_proximo_errou = models.ForeignKey('Pergunta' ,related_name="proximo_errou" , null=True , blank=True, verbose_name="Pergunta Proximo Errou")
	ajuda = models.ForeignKey('Ajuda', null=True , blank=True, verbose_name="Ajuda")
	pontos = models.IntegerField(verbose_name="Pontos Valem")

	def __unicode__(self):
		return self.descricao
	class Meta:
		ordering = ['-criacao']

	def pediuAjuda(self, usuario):
		b = Busca_Ajuda.objects.create(
				usuario = usuario.id,
				pergunta = self.id,
			)
		b.save()

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
		return self.descricao 
	
	class Meta:
		ordering = ['-criacao']



class Ajuda(Model):
	descricao = models.TextField(verbose_name="Descrição")
	def __unicode__(self):
		return self.descricao
	class Meta:
		ordering = ['-criacao']

class Busca_Ajuda(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuário")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta")

	def __unicode__(self):
		return str(self.usuario)
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
		return  str(self.usuario)
	class Meta:
		ordering = ['-criacao']

class Estado_Usuario(Model):
	turma  = models.ForeignKey(Turma, verbose_name="Turma")
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo , verbose_name="Conteudo")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta")

	def __unicode__(self):
		return str(self.usuario)
	class Meta:
		ordering = ['usuario']

class Pulo(Model):
	turma  = models.ForeignKey(Turma, verbose_name="Turma")
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo , verbose_name="Conteudo")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta")

	def __unicode__(self):
		return str(self.usuario)
	class Meta:
		ordering = ['usuario']


class UsuarioPontuacao(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteudo")
	pontos = models.IntegerField(default=0, verbose_name="Pontos",null=True , blank=True)
	pulosRestantes = models.IntegerField(default=0, verbose_name="Pulos Restantes", null= True, blank=True)

	def __unicode__(self):
		return str(self.usuario)

	def inclementaPontos(self,valor):
		self.pontos += valor
		UsuarioPontuacao.objects.filter(id = self.id).update(pontos = self.pontos)

	def inclementaPulos(self):
		self.pulosRestantes += 1 
		UsuarioPontuacao.objects.filter(id = self.id).update(pulosRestantes = self.pulosRestantes)

	def declementaPontos(self,valor):
		self.pontos -= valor
		if self.pontos < 0:
			self.pontos = 0

		UsuarioPontuacao.objects.filter(id = self.id).update(pontos = self.pontos)

	def declementaPulos(self):
		self.pulosRestantes -= 1
		if self.pulosRestantes < 0:
			self.pulosRestantes = 0
		UsuarioPontuacao.objects.filter(id = self.id).update(pulosRestantes = self.pulosRestantes)



		

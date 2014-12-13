# -*- encoding: utf-8 -*-

from django.db import models
from datetime import datetime
import unicodedata


class Model(models.Model):	
	criacao = models.DateTimeField(default=datetime.now, blank=True,null = True, verbose_name="Criacao")


class Turma(Model):
	nome = models.CharField(max_length=255 , verbose_name="Nome")
	semestre = models.FloatField(verbose_name="Semestre");

	def __unicode__(self):
		return format(self.criacao, "%m/%d/%Y %H:%M:%S") +" - "+ self.nome

	class Meta:
		ordering = ['-semestre']


class Usuario(Model):
	nome_usuario = models.CharField(max_length=255 , unique=True, verbose_name="Usuário")
	nome = models.CharField(max_length=255, verbose_name="Nome")
	email = models.EmailField(unique=True , verbose_name="Email")
	tipo  = models.BooleanField( default=True, verbose_name = "Tipo de Usuário")
	senha = models.CharField(max_length=255 , verbose_name="Senha")
	turma = models.ForeignKey('Turma', null= True, blank= True, verbose_name="Turma")

	def __unicode__(self):
		return format(self.criacao, "%m/%d/%Y %H:%M:%S") +" - "+ self.nome_usuario
	class Meta:
		ordering = ['nome']

class Conteudo(Model):
	tema = models.CharField(max_length=255 , unique=True, verbose_name="Tema")
	descricao = models.TextField(null=True , blank=True, verbose_name="Descrição")
	pergunta_inicial = models.ForeignKey('Pergunta' , null=True , blank=True , verbose_name="Pergunta Inicial")
	linha_metro = models.IntegerField(verbose_name="Posição Metro", null=False , blank=False);
	tamanho_metro = models.IntegerField(verbose_name="Tamanho Metro", null=False , blank=False);
	turma = models.ManyToManyField('Turma', verbose_name="Turma")
	def __unicode__(self):
		return format(self.criacao, "%m/%d/%Y %H:%M:%S") +" - "+ self.tema
	class Meta:
		ordering = ['tema']
	
class Pergunta(Model):
	descricao = models.TextField(verbose_name="Descrição")
	item_correto = models.ForeignKey('Item', null=True , blank=True, verbose_name="Item Correto")
	conteudo_pertence = models.ForeignKey(Conteudo, verbose_name="Conteudo Pertence")
	def __unicode__(self):
		return format(self.criacao, "%m/%d/%Y %H:%M:%S") +" - "+ self.descricao
	class Meta:
		ordering = ['-criacao']

class Ajuda(Model):
	descricao = models.TextField(verbose_name="Descrição")
	def __unicode__(self):
		return format(self.criacao, "%m/%d/%Y %H:%M:%S") +" - "+ self.descricao
	class Meta:
		ordering = ['-criacao']

class Item(Model):
	descricao = models.TextField(verbose_name="Descrição")
	pergunta_pertence = models.ForeignKey(Pergunta , related_name='pertence', verbose_name="Pergunta Pertence")
	tipo_proximo = models.IntegerField(default=1, verbose_name="Tipo Proximo")
	pergunta_proximo = models.ForeignKey(Pergunta ,related_name="proximo" , null=True , blank=True, verbose_name="Pergunta Proximo")
	ajuda_proximo = models.ForeignKey(Ajuda, null=True , blank=True, verbose_name="Ajuda Proximo")

	def __unicode__(self):
		return format(self.criacao, "%m/%d/%Y %H:%M:%S") +" - "+ self.descricao 
	
	class Meta:
		ordering = ['-criacao']

class Busca_Ajuda(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuário")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta")
	ajuda = models.ForeignKey(Ajuda, verbose_name="Ajuda")

	def __unicode__(self):
		return format(self.criacao, "%m/%d/%Y %H:%M:%S") +" - "+ self.usuario  + self.pergunta
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
		return format(self.criacao, "%m/%d/%Y %H:%M:%S") +" - "+ str(self.usuario) + " em " + str(self.data)
	class Meta:
		ordering = ['-criacao']

class Estado_Usuario(Model):
	turma  = models.ForeignKey(Turma, verbose_name="Turma")
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo , verbose_name="Conteudo")
	pergunta = models.ForeignKey(Pergunta, verbose_name="Pergunta")

	def __unicode__(self):
		return format(self.criacao, "%m/%d/%Y %H:%M:%S") +" - "+ str(self.usuario)
	class Meta:
		ordering = ['usuario']

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


class Conteudo(Model):
	turma = models.ManyToManyField('Turma', verbose_name="Turma")
	tema = models.CharField(max_length=255 , unique=True, verbose_name="Tema")
	descricao = models.TextField(null=True , blank=True, verbose_name="Descrição")
	pergunta_inicial = models.ForeignKey('Pergunta' , null=True , blank=True , verbose_name="Pergunta Inicial")
	requisitos = models.ManyToManyField('Requisito',related_name="Requisitos",null=True , blank=True, verbose_name="Requisitos")
	sugestao_estudo = models.ManyToManyField('SugestaoEstudo',related_name="Sugestoes",null=True , blank=True,verbose_name="Sugestao Estudo")
	max_pulos = models.IntegerField(verbose_name="Maximo de Pulos")
	linha_metro = models.IntegerField(verbose_name="Posição Metro", null=False , blank=False);
	tamanho_metro = models.IntegerField(verbose_name="Tamanho Metro", null=False , blank=False);
	

	def __unicode__(self):
		return self.tema
	class Meta:
		ordering = ['tema']
	
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

class Requisito(Model):
	conteudo = models.ForeignKey(Conteudo,related_name="Requisitos", verbose_name="Conteudo")

class SugestaoEstudo(Model):
	conteudo = models.ForeignKey(Conteudo,related_name="Sugestoes" , verbose_name="Conteudo")

class UsuarioPontuacao(Model):
	usuario = models.ForeignKey(Usuario, verbose_name="Usuario")
	conteudo = models.ForeignKey(Conteudo, verbose_name="Conteudo")
	
	questoes_total = models.IntegerField(verbose_name="Questoes Total",null=True , blank=True,)
	questoes_corretas = models.IntegerField(verbose_name="Questoes Corretas",null=True , blank=True,)
	questoes_saltadas = models.IntegerField(verbose_name="Questoes Corretas",null=True , blank=True,)
	
	pontos = models.IntegerField(verbose_name="Pontos",null=True , blank=True,)

	max_saltos = models.IntegerField(verbose_name="Maximo de Saltos",null=True , blank=True,)
	saltos = models.IntegerField(verbose_name="Saltos",null=True , blank=True,)


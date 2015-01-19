# -*- coding: utf-8 -*-

#IMPORTS PYTHON
from __future__ import unicode_literals
try:
	from hashlib import md5
except:
	from md5 import new as md5
import re
from random import randrange
import smtplib
from email.mime.text import MIMEText
import json


#IMPORTS DJANGO
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

#IMPORTS SPIRIT

#IMPORTS USER_PROFILE_SPIRIT

#IMPORTS ASK
from ask.models import *
from ask.utils import *
from ask.forms import *





@login_required
def principal_admin(request):
	if request.user.is_moderator == True:
		usuario = User.objects.get(username = request.user)

		conteudos1 = Conteudo.objects.filter(linha_metro = 1).order_by("tema");
		conteudos2 = Conteudo.objects.filter(linha_metro = 2).order_by("tema");
		conteudos3 = Conteudo.objects.filter(linha_metro = 3).order_by("tema");
		return render(request, "admin/principal_admin/principal_admin.php", locals())
	else:
		return HttpResponseRedirect("/principal/")

@login_required
def secundario_admin(request, tema_conteudo):
	if request.user.is_moderator == True:
		tema = transform_tema(tema_conteudo)
		usuario = User.objects.get(username = request.user)
		try:
			conteudo = Conteudo.objects.get(tema = tema)
		except:
			return HttpResponseRedirect("/principal_admin/")
		turmas = conteudo.turma.all()

		try:
			pergunta_inicial = Pergunta.objects.get(id = conteudo.pergunta_inicial_id)
		except:
			pass

		return render(request, "admin/secundario_admin/secundario_admin.php", locals())

	else:
		return HttpResponseRedirect("/principal/"+ tema_conteudo)

@login_required
def terciario_admin(request, tema_conteudo, id_pergunta):
	if request.user.is_moderator == True:
		tema = transform_tema(tema_conteudo)
		usuario = User.objects.get(username = request.user)
		try:
			conteudo = Conteudo.objects.get(tema = tema)
			pergunta = Pergunta.objects.get(id = id_pergunta)
		except:
			return HttpResponseRedirect("/principal_admin/")

		existeAnterior = False
		existeProximo = False
		existeAjuda = False
		try:
			perguntaAnterior = Pergunta.objects.get(pergunta_proximo_id = pergunta.id)
			existeAnterior = True
		except:
			existeAnterior = False
		try:
			perguntaProximo = Pergunta.objects.get(id = pergunta.pergunta_proximo_id)
			existeProximo = True
		except:
			existeProximo = False
		try:
			ajuda = Ajuda.objects.get(id = pergunta.ajuda_id)
			existeAjuda = True
		except:
			existeAjuda = False

		return render(request, "admin/terciario_admin/terciario_admin.php", locals())

	else:
		return HttpResponseRedirect("/principal/"+ tema_conteudo)


@login_required
def gerenciador(request):
	usuario = User.objects.get(username = request.user)
	return render(request, "admin/gerenciador/principal/principal.php", locals())


@login_required
def listOpcao(request, opcao):
	if opcao == "1":
		turmas = Turma.objects.all()
		return  render(request, "admin/gerenciador/opcao/turma/list.php", locals())
	elif opcao == "2":
		conteudos = Conteudo.objects.all()
		return  render(request, "admin/gerenciador/opcao/licao/list.php", locals())
	elif opcao == "3":
		perguntas = Pergunta.objects.all()
		return  render(request, "admin/gerenciador/opcao/pergunta/list.php", locals())
	elif opcao == "4":
		ajudas = Ajuda.objects.all()
		return  render(request, "admin/gerenciador/opcao/ajuda/list.php", locals())
	elif opcao == "5":
		itens = Item.objects.all()
		return  render(request, "admin/gerenciador/opcao/item/list.php", locals())
	elif opcao == "6":
		deficiencias = Deficiencia.objects.all()
		return  render(request, "admin/gerenciador/opcao/deficiencia/list.php", locals())
	else:
		return HttpResponseRedirect("/gerenciador/")

@login_required
def addOpcao(request, opcao):
	try:
		opcao = int(opcao)
	except:
		return HttpResponseRedirect("/gerenciador/")

	my_template = 'admin/gerenciador/opcao/opcao.php'

	if request.method == "POST":
		if opcao == 1:
			form = TurmaForm(request.POST)
		elif opcao == 2:
			form = ConteudoForm(request.POST)
		elif opcao == 3:
			form = PerguntaForm(request.POST)
		elif opcao == 4:
			form = AjudaForm(request.POST)
		elif opcao == 5:
			form = ItemForm(request.POST)
		elif opcao == 6:
			form = DeficienciaForm(request.POST)
		else:
			return  HttpResponseRedirect("/gerenciador/")

		if form.is_valid():
			print "Formulario Valido"
			if(form.save()):
				ok = True
				return render(request, "admin/gerenciador/opcao/avisos/adicionado.php", locals())
			else:
				ok = False
				return render(request, "admin/gerenciador/opcao/avisos/adicionado.php", locals())
		else:
			ok = False
			return render(request, "admin/gerenciador/opcao/avisos/adicionado.php", locals())
	else:
		if opcao == 1:
			form = PartialTurmaForm()
		elif opcao == 2:
			form = PartialConteudoForm()
		elif opcao == 3:
			form = PartialPerguntaForm()
		elif opcao == 4:
			form = PartialAjudaForm()
		elif opcao == 5:
			form = PartialItemForm()
		elif opcao == 6:
			form = PartialDeficienciaForm()
		else:
			return HttpResponseRedirect("/gerenciador/")

		return  render(request, "admin/gerenciador/opcao/add/add.php", locals())

@login_required
def remOpcao(request, opcao, id):
	try:
		opcao = int(opcao)
	except:
		return HttpResponse("Opcao nao e numeral")

	try:
		if opcao == 1:
			Turma.objects.filter(id = id).delete()
		elif opcao == 2:
			Conteudo.objects.filter(id = id).delete()
		elif opcao == 3:
			Pergunta.objects.filter(id = id).delete()
		elif opcao == 4:
			Ajuda.objects.filter(id = id).delete()
		elif opcao == 5:
			Item.objects.filter(id = id).delete()
		elif opcao == 6:
			Deficiencia.objects.filter(id = id).delete()
		else:
			return HttpResponseRedirect("/gerenciador/")
		return HttpResponse("True")
	except:
		return HttpResponse("False")


@login_required
def editOpcao(request, opcao, id):
	try:
		opcao = int(opcao)
	except:
		return HttpResponseRedirect("/gerenciador/")

	my_template = 'admin/gerenciador/opcao/opcao.php'
	if opcao == 1:
		try:
			turma = Turma.objects.get(id = id)
		except:
			return HttpResponse("falha")
		if request.method == 'POST':
			form = TurmaForm(request.POST,instance=turma)
			if form.is_valid():
				form.save()
				ok= True
				return render(request, "admin/gerenciador/opcao/avisos/editado.php", locals())
			else:
				ok = False
				return render(request, "admin/gerenciador/opcao/avisos/editado.php", locals())

		else:
			form = PartialTurmaForm(instance=turma)
		return  render(request, "admin/gerenciador/opcao/edit/edit.php", locals())
	elif opcao == 2:
		try:
			conteudo = Conteudo.objects.get(id = id)
		except:
			return HttpResponse("falha")
		if request.method == 'POST':
			form = ConteudoForm(request.POST,instance=conteudo)
			if form.is_valid():
				form.save()
				ok= True
				return render(request, "admin/gerenciador/opcao/avisos/editado.php", locals())
			else:
				ok = False
				return render(request, "admin/gerenciador/opcao/avisos/editado.php",locals())

		else:
			form = PartialConteudoForm(instance=conteudo)
		return  render(request, "admin/gerenciador/opcao/edit/edit.php", locals())
	elif opcao == 3:
		return  render(request, "admin/gerenciador/opcao/edit/edit.php", locals())
	elif opcao == 4:
		return  render(request, "admin/gerenciador/opcao/edit/edit.php", locals())
	elif opcao == 5:
		return  render(request, "admin/gerenciador/opcao/edit/edit.php", locals())
	elif opcao == 6:
		return  render(request, "admin/gerenciador/opcao/edit/edit.php", locals())
	else:
		return HttpResponseRedirect("/gerenciador/")



def ordenaPerguntas(request):
	if request.method == "POST":
		conteudo_id = request.POST['conteudo']
		perguntas = request.POST['perguntas']


		perguntas = json.loads(perguntas)
		
		if len(perguntas) == 0:
			Conteudo.objects.filter(id = conteudo_id).update(pergunta_inicial_id = None)
			return HttpResponse("Sem Perguntas Iniciais")
		
		quant_perguntas = len(perguntas.keys())

		for  i in range(quant_perguntas):
			pergunta_id = perguntas[str(i)]
			if i == 0:
				Conteudo.objects.filter(id = conteudo_id).update(pergunta_inicial_id = pergunta_id)
			else:
				pergunta_anterior_id = perguntas[str(i-1)]
				Pergunta.objects.filter(id = pergunta_anterior_id ).update(pergunta_proximo_id = pergunta_id)
				if i == (quant_perguntas-1):
					Pergunta.objects.filter(id = pergunta_id).update(pergunta_proximo_id = None)




	return HttpResponse("Success")


def zerarPerguntas(request):
	print "casaquista"
	if request.method == "POST":
		conteudo_id = request.POST['conteudo']
		perguntas = request.POST['perguntas']


		perguntas = json.loads(perguntas)

		quant_perguntas = len(perguntas.keys())

		for  i in range(quant_perguntas):
			pergunta_id = perguntas[str(i)]
			Pergunta.objects.filter(id = pergunta_id).update(pergunta_proximo_id = None)




	return HttpResponse("Success")


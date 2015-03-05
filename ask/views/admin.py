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
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page


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
		disciplinas = conteudo.disciplina.all()

		try:
			pergunta_inicial = conteudo.getPerguntasOrdenadas()[0]
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
			perguntaAnterior = pergunta.getPerguntaAnterior()
			if perguntaAnterior != None:
				existeAnterior = True
			else:
				existeAnterior = False
		except:
			existeAnterior = False
		try:
			perguntaProximo = pergunta.getPerguntaProxima()
			if perguntaProximo != None:
				existeProximo = True
			else:
				existeProximo = False
		except:
			existeProximo = False
		if pergunta.ajuda != '':
			existeAjuda = True
		else:
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
		disciplinas = Disciplina.objects.all()
		return  render(request, "admin/gerenciador/opcao/disciplina/list.php", locals())
	elif opcao == "2":
		conteudos = Conteudo.objects.all()
		return  render(request, "admin/gerenciador/opcao/licao/list.php", locals())
	elif opcao == "3":
		perguntas = Pergunta.objects.all()
		return  render(request, "admin/gerenciador/opcao/pergunta/list.php", locals())
	elif opcao == "4":
		usuarios = User.objects.all()
		return  render(request, "admin/gerenciador/opcao/usuario/list.php", locals())
	else:
		return HttpResponseRedirect("/gerenciador/")

@login_required
def addOpcao(request, opcao):
	try:
		opcao = int(opcao)
	except:
		return HttpResponseRedirect("/gerenciador/")


	if opcao == 1:
		my_template = 'admin/gerenciador/opcao/disciplina/list.php'
	elif opcao == 2:
		my_template = 'admin/gerenciador/opcao/licao/list.php'
	elif opcao == 3:
		my_template = 'admin/gerenciador/opcao/pergunta/list.php'
	elif opcao == 4:
		my_template = 'admin/gerenciador/opcao/usuario/list.php'
	else:
		my_template = 'admin/gerenciador/opcao/opcao.php'


	if request.method == "POST":
		if opcao == 1:
			form = PartialDisciplinaForm(request.POST)
		elif opcao == 2:
			form = PartialConteudoForm(request.POST)
		elif opcao == 3:
			form = PartialPerguntaForm(request.POST)
		elif opcao == 4:
			form = UserForm(request.POST)
		else:
			return  HttpResponseRedirect("/gerenciador/")

		if form.is_valid():
			print "Formulario Valido"
			if(form.save()):
				ok = True
				if opcao == 3:
					try:
						if atualizaPerguntasVisiveis(request.POST['conteudo_pertence']) == True:
							print "Perguntas visíveis atualizadas com sucesso."
					except:
						print "Erro ao atualizar perguntas visiveis."
						pass
				if opcao == 4:
					try:
						senha = request.POST['password']
						u = User.objects.get(username=request.POST['username'])
						u.set_password(senha)
						u.save()
					except:
						pass
				return render(request, "admin/gerenciador/opcao/avisos/adicionado.php", locals())
			else:
				ok = False
				return render(request, "admin/gerenciador/opcao/avisos/adicionado.php", locals())
		else:
			ok = False
			return render(request, "admin/gerenciador/opcao/avisos/adicionado.php", locals())
	else:
		if opcao == 1:
			form = PartialDisciplinaForm()
		elif opcao == 2:
			form = PartialConteudoForm()
		elif opcao == 3:
			form = PartialPerguntaForm()
		elif opcao == 4:
			form = UserForm()
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
			Disciplina.objects.filter(id = id).delete()
		elif opcao == 2:
			Conteudo.objects.filter(id = id).delete()
		elif opcao == 3:
			Pergunta.objects.filter(id = id).delete()
		elif opcao == 4:
			User.objects.filter(id = id).delete()
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


	if opcao == 1:
		my_template = 'admin/gerenciador/opcao/disciplina/list.php'
	elif opcao == 2:
		my_template = 'admin/gerenciador/opcao/licao/list.php'
	elif opcao == 3:
		my_template = 'admin/gerenciador/opcao/pergunta/list.php'
	elif opcao == 4:
		my_template = 'admin/gerenciador/opcao/usuario/list.php'
	else:
		my_template = 'admin/gerenciador/opcao/opcao.php'

	try:
		if opcao == 1:
			disciplina = Disciplina.objects.get(id = id)
		elif opcao == 2:
			conteudo = Conteudo.objects.get(id = id)
		elif opcao == 3:
			pergunta = Pergunta.objects.get(id = id)
		elif opcao == 4:
			usuario = User.objects.get(id = id)
		else:
			return HttpResponseRedirect("/gerenciador/")
	except:
		return HttpResponseRedirect("/gerenciador/")

	if request.method == 'POST':
		if opcao == 1:
			form = PartialDisciplinaForm(request.POST,instance=disciplina)
		elif opcao == 2:
			form = PartialConteudoForm(request.POST,instance=conteudo)
		elif opcao == 3:
			form = PartialPerguntaForm(request.POST,instance=pergunta)
		elif opcao == 4:
			form = UserForm(request.POST,instance=usuario)
		else:
			return HttpResponseRedirect("/gerenciador/")               

		if form.is_valid():
			form.save()
			ok= True
			if opcao == 3:
				try:
					senha = md5.new(request.POST['password']).hexdigest()
					User.objects.filter(username=request.POST['username']).update(password=senha)
				except:
					pass
			return render(request, "admin/gerenciador/opcao/avisos/editado.php", locals())
		else:
			ok = False
			return render(request, "admin/gerenciador/opcao/avisos/editado.php", locals())
	else:
		if opcao == 1:
			form = PartialDisciplinaForm(instance=disciplina)
		elif opcao == 2:
			form = PartialConteudoForm(instance=conteudo)
		elif opcao == 3:
			form = PartialPerguntaForm(instance=pergunta)
		elif opcao == 4:
			form = UserForm(instance=usuario)
		else:
			return HttpResponseRedirect("/gerenciador/")

		return render(request, 'admin/gerenciador/opcao/edit/edit.php', locals())


def ordenaPerguntas(request):
	if request.method == "POST":
		conteudo_id = request.POST['conteudo']
		perguntas = request.POST['perguntas']


		perguntas = json.loads(perguntas)
		
		if len(perguntas) == 0:
			return HttpResponse("Sem Perguntas Iniciais")
		
		quant_perguntas = len(perguntas.keys())

		for  i in range(quant_perguntas):
			pergunta_id = perguntas[str(i)]
			try:
				Pergunta.objects.filter(id = pergunta_id).update(posicao = i, visivel = True)
			except:
				continue




	return HttpResponse("Success")


def zerarPerguntas(request):
	if request.method == "POST":
		conteudo_id = request.POST['conteudo']
		perguntas = request.POST['perguntas']


		perguntas = json.loads(perguntas)

		quant_perguntas = len(perguntas.keys())

		for  i in range(quant_perguntas):
			pergunta_id = perguntas[str(i)]
			Pergunta.objects.filter(id = pergunta_id).update(posicao=None, visivel=False)



	return HttpResponse("Success")



def getNomeConteudo(request, id):
	try:
		conteudo = Conteudo.objects.get(id = id)
		print  conteudo.getTema()
		return  HttpResponse(conteudo.getTema())
	except:
		return HttpResponse("None")

def getNomeConteudoPerguntaPertence(request, id):
	try:
		pergunta = Pergunta.objects.get(id = id)
		conteudo = Conteudo.objects.get(id = pergunta.conteudo_pertence_id)
		return  HttpResponse(conteudo.getTema())
	except:
		return HttpResponse("None")

def atualizaPerguntasVisiveis(id_conteudo):
	try:
		conteudo = Conteudo.objects.get(id = id_conteudo)
	except:
		print "Falha ao pegar o conteúdo em atualizaPerguntasVisiveis()"
		return False;
	perguntas_visiveis = Pergunta.objects.filter(conteudo_pertence = id_conteudo, visivel=True, order_by="posicao")
	for i in range(len(perguntas_visiveis)):
		Pergunta.objects.filter(id = perguntas_visiveis[i].id ).update(posicao = i+1)
	










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
		turmas = Turma.objects.all()
		return  render(request, "admin/gerenciador/opcao/turma/list.php", locals())
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
		my_template = 'admin/gerenciador/opcao/turma/list.php'
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
			form = PartialTurmaForm(request.POST)
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
			Turma.objects.filter(id = id).delete()
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
		my_template = 'admin/gerenciador/opcao/turma/list.php'
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
			turma = Turma.objects.get(id = id)
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
			form = PartialTurmaForm(request.POST,instance=turma)
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
			return render(request, "admin/gerenciador/opcao/avisos/editado.php", locals())
		else:
			ok = False
			return render(request, "admin/gerenciador/opcao/avisos/editado.php", locals())
	else:
		if opcao == 1:
			form = PartialTurmaForm(instance=turma)
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
			Conteudo.objects.filter(id = conteudo_id).update(pergunta_inicial_id = None)
			return HttpResponse("Sem Perguntas Iniciais")
		
		quant_perguntas = len(perguntas.keys())

		for  i in range(quant_perguntas):
			pergunta_id = perguntas[str(i)]
			try:
				Pergunta.objects.filter(id = pergunta_id).update(visivel = True)
			except:
				pass
			if i == 0:
				Conteudo.objects.filter(id = conteudo_id).update(pergunta_inicial_id = pergunta_id)
			else:
				pergunta_anterior_id = perguntas[str(i-1)]
				Pergunta.objects.filter(id = pergunta_anterior_id ).update(pergunta_proximo_id = pergunta_id)
				if i == (quant_perguntas-1):
					Pergunta.objects.filter(id = pergunta_id).update(pergunta_proximo_id = None)




	return HttpResponse("Success")


def zerarPerguntas(request):
	if request.method == "POST":
		conteudo_id = request.POST['conteudo']
		perguntas = request.POST['perguntas']


		perguntas = json.loads(perguntas)

		quant_perguntas = len(perguntas.keys())

		for  i in range(quant_perguntas):
			pergunta_id = perguntas[str(i)]
			Pergunta.objects.filter(id = pergunta_id).update(pergunta_proximo_id = None, visivel=False)




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
	perguntas_visiveis = Pergunta.objects.filter(visivel = True)
	if conteudo.pergunta_inicial_id == None:
		pergunta_atual = None
		for i in perguntas_visiveis:
			if conteudo.pergunta_inicial_id != None:
				if pergunta_atual == None:
					pergunta_atual = Pergunta.objects.get(id = conteudo.pergunta_inicial_id)
					while pergunta_atual.pergunta_proximo_id != None:
						pergunta_atual = Pergunta.objects.get(id = pergunta_atual.pergunta_proximo_id)

				Pergunta.objects.filter(id = conteudo.pergunta_inicial_id).update(visivel = True)
				Pergunta.objects.filter(id = i.id).update(pergunta_proximo_id = conteudo.pergunta_inicial_id)
			else:
				Conteudo.objects.filter(id = conteudo.id).update(pergunta_inicial = i.id)
				pergunta_atual = Pergunta.objects.get(id = i.id)
			
		return True
	else:
		id_perguntas = []
		try:
			pergunta_atual = Pergunta.objects.get(id = conteudo.pergunta_inicial_id)
		except:
			print "Conteúdo não possui pergunta inicial em atualizaPerguntasVisiveis()"
			return False	
		id_perguntas.append(pergunta_atual.id)
		while pergunta_atual.pergunta_proximo_id != None :
			try:
				Pergunta.objects.filter(id = pergunta_atual.id).update(visivel = True)
				pergunta_atual = Pergunta.objects.get(id = pergunta_atual.pergunta_proximo_id)
				id_perguntas.append(pergunta_atual.id)
			except:
				print "Não existe mais Próxima Pergunta"
				break
		for i in perguntas_visiveis:
			esta = False
			for k in id_perguntas:
				if i.id == k:
					esta = True
			if esta == False:
				try:
					try:
						pergunta_inicial = Pergunta.objects.get(id = Conteudo.pergunta_inicial_id)
					except:
						Conteudo.objects.filter(id = conteudo.id).update(pergunta_inicial = i.id)
						continue
					while pergunta_inicial.pergunta_proximo_id != None:
						pergunta_inicial = Pergunta.objects.get(id = pergunta_inicial.pergunta_proximo_id)
					Pergunta.objects.filter(id = pergunta_inicial.id).update(pergunta_proximo_id = i.id)
					Pergunta.objects.filter(id = i.id).update(pergunta_proximo_id = None)
				except:
					print "Falha ao deixar Pergunta visivel"
					continue
		return True










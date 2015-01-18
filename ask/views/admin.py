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
	return render(request, "admin/gerenciador/principal.php", locals())

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


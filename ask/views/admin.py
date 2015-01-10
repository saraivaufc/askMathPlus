# -*- encoding=utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from ask.models import *
from django.core.mail import send_mail
try:
	from hashlib import md5
except:
	from md5 import new as md5

import re
from random import randrange
import smtplib
from email.mime.text import MIMEText
from django.contrib.auth.decorators import login_required

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
		
		existePerguntaInicial = False
		if conteudo.pergunta_inicial_id != None:
			existePerguntaInicial = True
		else:
			return render(request, "admin/secundario_admin/secundario_admin.php", locals())
		perguntas = []
		try:
			pergunta_inicial = Pergunta.objects.get(id = conteudo.pergunta_inicial_id)
		except:
			 return render(request, "admin/secundario_admin/secundario_admin.php", locals())

		perguntas.append(pergunta_inicial)
		while perguntas[len(perguntas)-1].pergunta_proximo_id != None:
			pergunta_proximo = Pergunta.objects.get(id = perguntas[len(perguntas)-1].pergunta_proximo_id)
			perguntas.append(pergunta_proximo)

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
			itens = Item.objects.filter(pergunta_pertence_id = pergunta.id)
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

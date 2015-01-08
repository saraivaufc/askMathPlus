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
from django.contrib.auth.views import login as login_view
from spirit.forms.user import LoginForm
from django.contrib.auth.views import logout as logout_sys
from spirit.utils.ratelimit.decorators import ratelimit
from spirit_user_profile import models

from django.test import Client
from classes import *
from utils import *

def principal_admin(request):
	if request.user.is_authenticated():
		if request.user.is_moderator == True:
			usuario = User.objects.get(username = request.user)

			conteudos1 = Conteudo.objects.filter(linha_metro = 1).order_by("tema");
			conteudos2 = Conteudo.objects.filter(linha_metro = 2).order_by("tema");
			conteudos3 = Conteudo.objects.filter(linha_metro = 3).order_by("tema");
			return render(request, "admin/principal_admin/principal_admin.php", locals())
		else:
			return HttpResponseRedirect("/principal/")
	else:
		return HttpResponseRedirect("/login/")

def secundario_admin(request, tema_conteudo):
	if request.user.is_authenticated():
		if request.user.is_moderator == True:
			tema = transform_tema(tema_conteudo)
			usuario = User.objects.get(username = request.user)
			try:
				conteudo = Conteudo.objects.get(tema = tema)
			except:
				return HttpResponseRedirect("/principal_admin/")
			turmas = conteudo.turma.all()
			perguntas = Pergunta.objects.filter(conteudo_pertence_id = conteudo.id)
			pergunta_inicial = conteudo.pergunta_inicial_id
			if pergunta_inicial != None:
				pergunta_inicial = Pergunta.objects.get(id = pergunta_inicial)
			return render(request, "admin/secundario_admin/secundario_admin.php", locals())

		else:
			return HttpResponseRedirect("/principal/"+ tema_conteudo)
	else:
		return HttpResponseRedirect("/login/")

# -*- coding: utf-8 -*-

#IMPORTS PYTHON
from __future__ import unicode_literals
try:
	from hashlib import md5
except:
	from md5 import new as md5

import json
#IMPORTS DJANGO
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers

#IMPORTS SPIRIT

#IMPORTS USER_PROFILE_SPIRIT

#IMPORTS ASK
from ask.models import *
from ask.utils import *
from ask.forms import *

tipo_saida = 'json'

@login_required
def getDisciplinas(request):
	disciplinas = serializers.serialize(tipo_saida , Disciplina.objects.all(), fields=('semestre','nome'))
	return HttpResponse(disciplinas)
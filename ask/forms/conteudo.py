# encoding: utf-8
from __future__ import unicode_literals
import hashlib, os
from django import forms
from django.contrib.auth import authenticate
import datetime
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import ModelForm
from ask.models import *



class ConteudoForm(ModelForm):
	class Meta:
		model= Conteudo
		fields = '__all__'



class PartialConteudoForm(ModelForm):
	class Meta:
		model=Conteudo
		exclude  = ['pergunta_inicial','criacao']

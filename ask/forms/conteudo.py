# encoding: utf-8
from __future__ import unicode_literals
import hashlib, os
from django import forms
from django.contrib.auth import authenticate
import datetime
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import ModelForm, Textarea, TextInput, NumberInput, Select
from ask.models import *



class ConteudoForm(ModelForm):
	class Meta:
		model= Conteudo
		fields = '__all__'



class PartialConteudoForm(ModelForm):
	class Meta:
		model=Conteudo
		exclude  = ['pergunta_inicial','criacao']

		widgets = {
			'tema': TextInput(attrs={'required': 'required'}),
			'descricao': Textarea(attrs={'required': 'required'}),
			'max_pulos': NumberInput(attrs={'required': 'required'}),
			'linha_metro': Select(attrs={'required': 'required'}),
			'tamanho_metro': Select(attrs={'required': 'required'}),


		}

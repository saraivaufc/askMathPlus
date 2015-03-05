# encoding: utf-8
from __future__ import unicode_literals
import hashlib, os
from django import forms
from django.contrib.auth import authenticate
import datetime
from django.forms.formsets import formset_factory, BaseFormSet
from ask.models import *
from django.forms import ModelForm, Textarea, TextInput, NumberInput


class DisciplinaForm(ModelForm):
	class Meta:
		model= Disciplina
		fields = '__all__'

class PartialDisciplinaForm(ModelForm):
	class Meta:
		model= Disciplina
		exclude = ['criacao',]

		widgets = {
			'disciplina': TextInput(attrs={'required': 'required'}),
			'semestre': NumberInput(attrs={'required': 'required'}),
			'professor': TextInput(attrs={'required': 'required'}),

		}


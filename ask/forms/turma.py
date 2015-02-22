# encoding: utf-8
from __future__ import unicode_literals
import hashlib, os
from django import forms
from django.contrib.auth import authenticate
import datetime
from django.forms.formsets import formset_factory, BaseFormSet
from ask.models import *
from django.forms import ModelForm, Textarea, TextInput, NumberInput


class TurmaForm(ModelForm):
	class Meta:
		model= Turma
		fields = '__all__'

class PartialTurmaForm(ModelForm):
	class Meta:
		model= Turma
		exclude = ['criacao',]

		widgets = {
			'disciplina': TextInput(attrs={'required': 'required'}),
			'semestre': NumberInput(attrs={'required': 'required'}),
			'professor': TextInput(attrs={'required': 'required'}),

		}


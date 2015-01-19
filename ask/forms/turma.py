# encoding: utf-8
from __future__ import unicode_literals
import hashlib, os
from django import forms
from django.contrib.auth import authenticate
import datetime
from django.forms.formsets import formset_factory, BaseFormSet
from ask.models import *
from django.forms import ModelForm


class TurmaForm(ModelForm):
	class Meta:
		model= Turma
		fields = '__all__'

class PartialTurmaForm(ModelForm):
	class Meta:
		model= Turma
		exclude = ['criacao',]


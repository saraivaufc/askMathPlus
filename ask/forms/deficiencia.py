# encoding: utf-8
from __future__ import unicode_literals
import hashlib, os
from django import forms
from django.contrib.auth import authenticate
import datetime
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import ModelForm
from ask.models import *

class DeficienciaForm(ModelForm):
	class Meta:
		model= Deficiencia
		fields = '__all__'



class PartialDeficienciaForm(ModelForm):
	class Meta:
		model=Deficiencia
		exclude  = ['criacao',]

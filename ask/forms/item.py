# encoding: utf-8
from __future__ import unicode_literals
import hashlib, os
from django import forms
from django.contrib.auth import authenticate
import datetime
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import ModelForm
from ask.models import *

class ItemForm(ModelForm):
	class Meta:
		model= Item
		fields = '__all__'



class PartialItemForm(ModelForm):
	class Meta:
		model=Item
		exclude  = ['criacao','deficiencia']
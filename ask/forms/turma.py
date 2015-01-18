# encoding: utf-8
from __future__ import unicode_literals
import hashlib, os
from django import forms
from django.contrib.auth import authenticate
import datetime
from django.forms.formsets import formset_factory, BaseFormSet
from ask.models import *
from django.forms import ModelForm
from django.utils.image import Image


class TurmaForm(forms.Form):
	disciplina = forms.CharField(label="Disciplina", max_length=255,  widget=forms.TextInput(attrs={ 'required': 'true' , "autofocus":'true',}),)
	semestre =  forms.FloatField(label="Semestre",  widget=forms.TextInput(attrs={ 'required': 'true' }),)
	professor = forms.CharField(label="Professor", max_length=255, widget=forms.TextInput(attrs={ 'required': 'true' }),)

	def __init__(self, *args, **kwargs):
		super(TurmaForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Turma
		exclude = ['likes',]
		fields = ['instituicao','nome', 'sobrenome', 'idade', 'peso', 'relacionamento',
				  'imagem_perfil', 'facebook',  ]
	def clean(self):
		cleaned_data = super(TurmaForm,self).clean()
		disciplina = self.cleaned_data.get('disciplina')
		semestre = self.cleaned_data.get('semestre')
		professor = self.cleaned_data.get('professor')


		return self.cleaned_data

	def save(self):
		disciplina = self.cleaned_data['disciplina']
		semestre = self.cleaned_data['semestre']
		professor = self.cleaned_data['professor']

		try:
			turma = Turma.objects.create(
				disciplina = disciplina,
				semestre = semestre,
				professor = professor,
				)
			turma.save()
			return True
		except:
			return False

	def update(self, id):
		disciplina = self.cleaned_data['disciplina']
		semestre = self.cleaned_data['semestre']
		professor = self.cleaned_data['professor']

		try:
			turma = Turma.objects.filter(id = id).update(
								disciplina = disciplina,
								semestre = semestre,
								professor = professor,
						)
			return True
		except:
			return False

class TurmaFormToModel(ModelForm):
	class Meta:
		model = Turma
		fields = ['disciplina', 'semestre','professor',]

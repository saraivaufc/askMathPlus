# encoding: utf-8
from __future__ import unicode_literals
import hashlib, os
from django import forms
from django.contrib.auth import authenticate
import datetime
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import ModelForm
from ask.models import *

#CHOICES
POSICAOMETRO = (
		(1, "TOPO"),
		(2, "MEIO"),
		(3, "BAIXO"),
	)
TAMANHOMETRO = (
	(1, "PEQUENO"),
	(2, "GRANDE"),
)

class ConteudoForm(forms.Form):
	turma = forms.MultipleChoiceField( label="Turma",queryset=Turma.objects.all(), required= True, widget=forms.TextInput(attrs={ 'required': 'true' , "autofocus":'true',}),)
	tema = forms.CharField(label="Tema",max_length=255 , required = True, widget=forms.TextInput(attrs={ 'required': 'true' ,}),)
	descricao = forms.TextField(label="Descricao", required = False)
	requisitos = forms.ModelChoiceField( label="Requisitos",queryset=Conteudo.objects.all(), required = False)
	sugestao_estudo = forms.ModelChoiceField( label="Sugestoes",queryset=Conteudo.objects.all(), required = False)
	max_pulos = forms.IntegerField(initial = 0, label="Maximo de Pulos", required=False)
	linha_metro = forms.IntegerField(label="Linha no Metro", choices=POSICAOMETRO, required = True,  widget=forms.TextInput(attrs={ 'required': 'true' ,}))
	tamanho_metro = forms.IntegerField(label="Tamanho do Tile", choices=TAMANHOMETRO, required= True,  widget=forms.TextInput(attrs={ 'required': 'true' ,}))

	def __init__(self, *args, **kwargs):
		super(ConteudoForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Conteudo
		fields = ['turma', 'tema', 'descricao','requisitos','sugestao_estudo','max_pulos','linha_metro','tamanho_metro',]
		widgets = {
		            'turma' : forms.CheckboxSelectMultiple(),
		            'requisitos' : forms.CheckboxSelectMultiple(),
		            'sugestao_estudo' : forms.CheckboxSelectMultiple(),
		 }

	def clean(self):
		cleaned_data = super(ConteudoForm,self).clean()
		turma = self.cleaned_data.get('turma')
		tema = self.cleaned_data.get('tema')
		descricao = self.cleaned_data.get('descricao')
		requisitos = self.cleaned_data.get('requisitos')
		sugestao_estudo = self.cleaned_data.get('sugestao_estudo')
		max_pulos = self.cleaned_data.get('max_pulos')
		linha_metro = self.cleaned_data.get('linha_metro')
		tamanho_metro = self.cleaned_data.get('tamanho_metro')


		return self.cleaned_data

	def save(self):
		turma = self.cleaned_data['turma']
		tema = self.cleaned_data['tema']
		descricao = self.cleaned_data['descricao']
		requisitos = self.cleaned_data['requisitos']
		sugestao_estudo = self.cleaned_data['sugestao_estudo']
		max_pulos = self.cleaned_data['max_pulos']
		linha_metro = self.cleaned_data['linha_metro']
		tamanho_metro = self.cleaned_data['tamanho_metro']

		try:
			Conteudo.objects.create(

			)

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


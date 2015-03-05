# encoding: utf-8
from __future__ import unicode_literals
import hashlib, os
from django import forms
from django.contrib.auth import authenticate
import datetime
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from ask.models import *

class PerguntaForm(ModelForm):
	class Meta:
		model= Pergunta
		fields = '__all__'



class PartialPerguntaForm(ModelForm):
	class Meta:
		model=Pergunta
		exclude  = ['criacao', 'posicao',]
		localized_fields = ('__all__',)
		widgets = {
			'item_a': Textarea(attrs={'cols': 40, 'rows': 3}),
			'item_b': Textarea(attrs={'cols': 40, 'rows': 3}),
			'item_c': Textarea(attrs={'cols': 40, 'rows': 3}),
			'item_d': Textarea(attrs={'cols': 40, 'rows': 3}),
			'item_e': Textarea(attrs={'cols': 40, 'rows': 3}),

            'ajuda': Textarea(attrs={'cols': 40, 'rows': 4}),


            #required
            'conteudo_pertence': Select(attrs={'required': 'required'}),
            'item_correto': Select(attrs={'required': 'required'}),
            'descricao': Textarea(attrs={'required': 'required'}),
            'pontos': NumberInput(attrs={'required': 'required'}),

		}
#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, HiddenInput, Textarea
from django.utils.translation import ugettext_lazy as _

from askmath.models.category import Category

class CategoryForm(ModelForm):
    class Meta:
        model= Category
        fields = ("title","description","person")

        widgets = {
            'person': HiddenInput(attrs={'class':'hidden'}),      
            'title': TextInput(attrs={'required': 'required', 'autofocus': 'True'}),
         	'description': Textarea(attrs={'required': 'required'}),    
        }
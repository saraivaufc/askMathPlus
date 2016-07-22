#-*- encoding=utf-8 -*-

from askmath.models.category import Category
from django.forms import ModelForm, TextInput, HiddenInput, Textarea

class CategoryForm(ModelForm):
    class Meta:
        model= Category
        fields = ("title","description","person")

        widgets = {
            'person': HiddenInput(attrs={'class':'hidden'}),      
            'title': TextInput(attrs={'required': 'required', 'autofocus': 'True'}),
         	'description': Textarea(attrs={}),
        }
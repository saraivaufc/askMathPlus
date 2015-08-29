#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, HiddenInput
from django.utils.translation import ugettext_lazy as _

from askmath.models.category import Category

class CategoryForm(ModelForm):
    class Meta:
        model= Category
        fields = ("title","person")

        widgets = {
            'person': HiddenInput(attrs={'class':'input-control hidden full-size'}),      
            'title': TextInput(attrs={'required': 'required', 'class':'input-control text', 'autofocus': 'True'}),
        }
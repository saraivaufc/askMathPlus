#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput
from django.utils.translation import ugettext_lazy as _

from askmath.models.discipline import Discipline


class DisciplineForm(ModelForm):
    class Meta:
        model= Discipline
        fields = ("title", "responsible", "visible")

        widgets = {
            'title': TextInput(attrs={'required': 'required', 'autofocus': 'True'}),
            'responsible': TextInput(attrs={'required': 'required'}),
            'visible': CheckboxInput(attrs={}),
        }
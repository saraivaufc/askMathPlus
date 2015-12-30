#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput, Select
from django.utils.translation import ugettext_lazy as _

from askmath.models.discipline import Discipline


class DisciplineForm(ModelForm):
    class Meta:
        model= Discipline
        fields = ("title", "responsible", "color", "visible")

        widgets = {
            'title': TextInput(attrs={'autofocus': 'True'}),
            'responsible': TextInput(attrs={}),
            'color': Select(attrs={}),
            'visible': CheckboxInput(attrs={}),
        }
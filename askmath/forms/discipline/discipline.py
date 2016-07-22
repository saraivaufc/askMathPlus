# -*- encoding=utf-8 -*-

from askmath.models.discipline import Discipline
from django.forms import ModelForm, TextInput, CheckboxInput


class DisciplineForm(ModelForm):
    class Meta:
        model = Discipline
        fields = ("title", "visible")

        widgets = {
            'title': TextInput(attrs={'autofocus': 'True'}),
            'visible': CheckboxInput(attrs={}),
        }

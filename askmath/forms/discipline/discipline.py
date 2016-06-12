#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput
from django.utils.translation import ugettext_lazy as _

from askmath.models.discipline import Discipline
from askmath.models.users.teacher import Teacher as TeacherModel


class DisciplineForm(ModelForm):
    class Meta:
        model= Discipline
        fields = ( "title", "visible")

        widgets = {
            'title': TextInput(attrs={'autofocus': 'True'}),
            'visible': CheckboxInput(attrs={}),
        }
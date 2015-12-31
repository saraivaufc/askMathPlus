#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput, Select
from django.utils.translation import ugettext_lazy as _

from askmath.models.discipline import Discipline
from askmath.models.users.teacher import Teacher as TeacherModel


class DisciplineForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (DisciplineForm,self ).__init__(*args,**kwargs)
        self.fields['responsible'].queryset = TeacherModel.objects.filter(exists=True)
    class Meta:
        model= Discipline
        fields = ("title", "responsible", "color", "visible")

        widgets = {
            'title': TextInput(attrs={'autofocus': 'True'}),
            'responsible': Select(attrs={}),
            'color': Select(attrs={'required':'required'}),
            'visible': CheckboxInput(attrs={}),
        }
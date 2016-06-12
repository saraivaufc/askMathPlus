#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput, Select, SelectMultiple, ClearableFileInput, NumberInput
from django.utils.translation import ugettext_lazy as _

from askmath.models.classe import Classe
from askmath.models.discipline import Discipline
from askmath.models.users.teacher import Teacher as TeacherModel


class ClasseForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (ClasseForm,self ).__init__(*args,**kwargs)
        self.fields['responsible'].queryset = TeacherModel.objects.filter(exists=True)
        self.fields['disciplines'].queryset = Discipline.objects.filter(exists=True)
    class Meta:
        model= Classe
        fields = ( "name", "responsible","semester", "plan","disciplines" , "visible")

        widgets = {
            'name': TextInput(attrs={'autofocus': 'True'}),
            'responsible': Select(attrs={}),
            'semester': NumberInput(attrs={'required':'required'}),
            'plan': ClearableFileInput(attrs={}),
            'disciplines' : SelectMultiple(attrs={'class':'full-size'}),
            'visible': CheckboxInput(attrs={}),
        }

    def clean_plan(self):
        file = self.cleaned_data["plan"]
        try:
            if file and file.name.find('askmath_') == -1:
                hash = hashlib.md5(file.read()).hexdigest()
                file.name = "askmath_" + "".join((hash, ".", file.name.split(".")[-1]))
        except:
            pass
        return file
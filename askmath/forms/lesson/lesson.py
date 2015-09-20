#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput, Textarea, SelectMultiple, NumberInput, ModelMultipleChoiceField,Select
from django.utils.translation import ugettext_lazy as _

from askmath.models import Lesson, Discipline
class LessonForm(ModelForm):
	def __init__(self,*args,**kwargs):
		super (LessonForm,self ).__init__(*args,**kwargs)
		self.fields['discipline'].queryset = Discipline.objects.filter(exists=True)
		self.fields['requirements'].queryset = Lesson.objects.filter(exists=True)
		self.fields['sugestions'].queryset = Lesson.objects.filter(exists=True)
		
	class Meta:
		model= Lesson
		fields = ("discipline","title", "description", "requirements", "sugestions", "maximum_hops","color", "visible")
		widgets = {
			'discipline': Select(attrs={'required':'required','class':'full-size','autofocus': 'True'}),
			'title': TextInput(attrs={'required': 'required'}),
			'description': Textarea(attrs={'cols': 50, 'rows': 6,'class':'latex','required': 'required'}),
			'requirements': SelectMultiple(attrs={'class':'full-size'}),
			'sugestions': SelectMultiple(attrs={'class':'full-size'}),
			'maximum_hops': NumberInput(attrs={'required':'required', 'min': '0'}),
			'color': Select(attrs={'required': 'required','class':'full-size'}),
			'visible': CheckboxInput(attrs={}),
		}
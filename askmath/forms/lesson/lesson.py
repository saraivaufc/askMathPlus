#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput, Textarea, SelectMultiple, NumberInput, ModelMultipleChoiceField
from django.utils.translation import ugettext_lazy as _

from askmath.models import Lesson, Discipline
class LessonForm(ModelForm):
	def __init__(self,*args,**kwargs):
		super (LessonForm,self ).__init__(*args,**kwargs)
		self.fields['disciplines'].queryset = Discipline.objects.filter(exists=True)
		self.fields['requirements'].queryset = Lesson.objects.filter(exists=True)
		self.fields['sugestions'].queryset = Lesson.objects.filter(exists=True)
		
	class Meta:
		model= Lesson
		fields = ("disciplines","title", "description", "requirements", "sugestions", "maximum_hops", "visible")
		widgets = {
			'disciplines': SelectMultiple(attrs={'required':'required'}),
			'title': TextInput(attrs={'required': 'required', 'autofocus': 'True'}),
			'description': Textarea(attrs={'cols': 50, 'rows': 6,'required': 'required'}),
			'requirements': SelectMultiple(attrs={}),
			'sugestions': SelectMultiple(attrs={}),
			'maximum_hops': NumberInput(attrs={'required':'required', 'min': '0'}),
			'visible': CheckboxInput(attrs={}),
		}
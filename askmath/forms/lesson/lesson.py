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
			'disciplines': SelectMultiple(attrs={'class':'input-control select', 'required':'required'}),
			'title': TextInput(attrs={'required': 'required', 'autofocus': 'True', 'class':'input-control text', 'x-webkit-speech': 'x-webkit-speech'}),
			'description': Textarea(attrs={'cols': 50, 'rows': 6,'required': 'required', 'class':'latex input-control textarea full-size', 'x-webkit-speech': 'x-webkit-speech'}),
			'requirements': SelectMultiple(attrs={'class':'input-control select'}),
			'sugestions': SelectMultiple(attrs={'class':'input-control select'}),
			'maximum_hops': NumberInput(attrs={'required':'required', 'class':'input-control number'}),
			'visible': CheckboxInput(attrs={'class':'input-control checkbox switch'}),
		}
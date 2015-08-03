#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput, Textarea, SelectMultiple, NumberInput, HiddenInput
from django.utils.translation import ugettext_lazy as _

from askmath.models import Item, Discipline, Lesson

class ItemForm(ModelForm):
	def __init__(self,*args,**kwargs):
		super (ItemForm,self ).__init__(*args,**kwargs)
		self.fields['deficiencys'].queryset = Lesson.objects.filter(exists=True)

	class Meta:
		model= Item
		fields = ("position", "description", "correct", "deficiencys")
		widgets = {
			'position': HiddenInput(attrs={'class':'input-control hidden'}),
			'description': Textarea(attrs={'required': 'required', 'class':'latex input-control  textarea full-size', 'x-webkit-speech': 'x-webkit-speech'}),
			'correct': CheckboxInput(attrs={'class':'input-control checkbox'}),
			'deficiencys': SelectMultiple(attrs={'class':'input-control select'}),
		}
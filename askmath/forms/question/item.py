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
			'position': HiddenInput(attrs={'class':'hidden'}),
			'description': Textarea(attrs={'required': 'required', 'class':'latex'}),
			'correct': CheckboxInput(attrs={}),
			'deficiencys': SelectMultiple(attrs={}),
		}
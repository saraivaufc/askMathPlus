#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput, Textarea, SelectMultiple, NumberInput, HiddenInput, Select
from django.utils.translation import ugettext_lazy as _

from askmath.models import Question, Discipline


class QuestionForm(ModelForm):  
    class Meta:
        model= Question
        fields = ("lesson", "position", "description", "items", "help", "scores", "visible")
        widgets = {
            'lesson': HiddenInput(attrs={'class':'hidden'}),
            'position': HiddenInput(attrs={'class':'hidden'}),
            'description': Textarea(attrs={'required': 'required', 'class':'latex'}),
            'help': Textarea(attrs={'class':'latex'}),
            'items': HiddenInput(attrs={'class':'hidden'}),
            'scores': Select(attrs={'required':'required'}),
            'visible': CheckboxInput(attrs={}),
        }
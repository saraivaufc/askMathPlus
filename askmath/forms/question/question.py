#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput, Textarea, SelectMultiple, NumberInput, HiddenInput
from django.utils.translation import ugettext_lazy as _

from askmath.models import Question, Discipline


class QuestionForm(ModelForm):  
    class Meta:
        model= Question
        fields = ("lesson", "position", "description", "items", "help", "scores", "visible")
        widgets = {
            'lesson': HiddenInput(attrs={'class':'input-control hidden full-size'}),
            'position': HiddenInput(attrs={'class':'input-control hidden full-size'}),
            'description': Textarea(attrs={'required': 'required', 'class':'input-control  textarea full-size', 'x-webkit-speech': 'x-webkit-speech'}),
            'help': Textarea(attrs={'class':'input-control  textarea full-size', 'x-webkit-speech': 'x-webkit-speech'}),
            'items': HiddenInput(attrs={'class':'input-control hidden'}),
            'scores': NumberInput(attrs={'required':'required', 'class':'input-control number'}),
            'visible': CheckboxInput(attrs={'class':'input-control checkbox'}),
        }
# -*- encoding=utf-8 -*-

from askmath.models import Question
from django.forms import ModelForm, CheckboxInput, Textarea, HiddenInput, Select, FileInput


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ("lesson", "position", "description","image", "items", "help", "scores", "visible")
        widgets = {
            'lesson': HiddenInput(attrs={'class': 'hidden'}),
            'position': HiddenInput(attrs={'class': 'hidden'}),
            'description': Textarea(attrs={'required': 'required', 'class': 'latex','rows': '1'}),
            'help': Textarea(attrs={'class': 'latex','rows': '1'}),
            'items': HiddenInput(attrs={'class': 'hidden'}),
            'scores': Select(attrs={'required': 'required'}),
            'visible': CheckboxInput(),
        }

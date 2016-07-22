# -*- encoding=utf-8 -*-

from askmath.models.comment import Comment
from django.forms import ModelForm, HiddenInput, Textarea


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("person", "topic", "description")
        widgets = {
            'person': HiddenInput(attrs={'class': 'hidden'}),
            'topic': HiddenInput(attrs={'class': 'hidden'}),
            'description': Textarea(attrs={'required': 'required', 'rows': '3', 'cols': '100%'}),
        }

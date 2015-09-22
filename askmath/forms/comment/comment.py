#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, HiddenInput, Textarea
from django.utils.translation import ugettext_lazy as _
import hashlib

from askmath.models.comment import Comment

class CommentForm(ModelForm):
    class Meta:
        model= Comment
        fields = ("person", "topic", "description")
        widgets = {
            'person': HiddenInput(attrs={'class':'hidden'}),
            'topic': HiddenInput(attrs={'class':'hidden'}),
            'description': Textarea(attrs={'required': 'required','rows':'3','cols':'100%'}),
            
        }
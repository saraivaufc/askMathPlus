#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, HiddenInput, Textarea
from django.utils.translation import ugettext_lazy as _
import hashlib

from askmath.models.comment import Comment

class CommentForm(ModelForm):
    class Meta:
        model= Comment
        fields = ("person", "topic", "description","file")
        widgets = {
            'person': HiddenInput(attrs={'class':'input-control hidden full-size'}),
            'topic': HiddenInput(attrs={'class':'input-control hidden full-size'}),
            'description': Textarea(attrs={'required': 'required','rows':'4', 'class':'input-control  textarea'}),
            
        }
        
    def clean_file(self):
        file = self.cleaned_data["file"]
        try:
            if file and file.name.find('hash_') == -1:
                hash = hashlib.md5(file.read()).hexdigest()
                file.name = "hash_" + "".join((hash, ".", file.name.split(".")[-1]))
        except:
            pass
        return file
        
#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, HiddenInput, Textarea
from django.utils.translation import ugettext_lazy as _
import hashlib

from askmath.models.topic import Topic

class TopicForm(ModelForm):
    class Meta:
        model= Topic
        fields = ("person", "category", "description","file")
        widgets = {
            'person': HiddenInput(attrs={'class':'input-control hidden full-size'}),
            'category': HiddenInput(attrs={'class':'input-control hidden full-size'}),
            'description': Textarea(attrs={'required': 'required','rows':'3','cols':'100%','autofocus':'true' ,'class':'latex input-control  textarea full-size'}),
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
        
#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, HiddenInput, Textarea, Select
from django.utils.translation import ugettext_lazy as _
import hashlib

from askmath.models.topic import Topic

class TopicForm(ModelForm):
    class Meta:
        model= Topic
        fields = ("person", "category", "title", "description","file")
        widgets = {
            'person': HiddenInput(attrs={'class':'hidden'}),
            'category': HiddenInput(attrs={'class':'hidden'}),
            'title': TextInput(attrs={'required': 'required','autofocus':'true'}),
            'description': Textarea(attrs={'required': 'required','rows':'3','cols':'100%' ,'class':'latex'}),
        }
        
    def clean_file(self):
        file = self.cleaned_data["file"]
        try:
            if file and file.name.find('askmath_') == -1:
                hash = hashlib.md5(file.read()).hexdigest()
                file.name = "askmath_" + "".join((hash, ".", file.name.split(".")[-1]))
        except:
            pass
        return file
        
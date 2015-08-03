#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput, Textarea, HiddenInput, FileInput
import hashlib

from askmath.models.video import Video


class VideoForm(ModelForm):
    class Meta:
        model= Video
        fields = ("lesson", "position","title", "description","file" , "visible")
        widgets = {
            'lesson': HiddenInput(attrs={'class':'input-control hidden'}),
            'position': HiddenInput(attrs={'class':'input-control hidden'}),
            'title': TextInput(attrs={'class':'input-control text', 'required': 'required', 'x-webkit-speech': 'x-webkit-speech'}),
            'description': Textarea(attrs={'cols': 50, 'rows': 6,'required': 'required', 'class':'latex input-control  textarea full-size', 'x-webkit-speech': 'x-webkit-speech'}),
            'visible': CheckboxInput(attrs={'class':'input-control checkbox'}),
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
        
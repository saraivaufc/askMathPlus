#-*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput, Textarea, HiddenInput, ClearableFileInput, Select
import hashlib

from askmath.models.video import Video


class VideoForm(ModelForm):
    class Meta:
        model= Video
        fields = ("lesson", "position","title", "description","file", "visible")
        widgets = {
            'lesson': HiddenInput(attrs={'class':'hidden'}),
            'position': HiddenInput(attrs={'class':'hidden'}),
            'title': TextInput(attrs={'required': 'required'}),
            'description': Textarea(attrs={'cols': 50, 'rows': 6,'class':'latex'}),
            'file': ClearableFileInput(attrs={'required': 'required'}),
            'visible': CheckboxInput(attrs={}),
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
        
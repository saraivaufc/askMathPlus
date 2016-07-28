# -*- encoding=utf-8 -*-

from django.forms import ModelForm, TextInput, CheckboxInput, Textarea, SelectMultiple, NumberInput, HiddenInput

from askmath.models import Lesson, Discipline


class LessonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        self.fields['discipline'].queryset = Discipline.objects.filter(exists=True)
        self.fields['requirements'].queryset = Lesson.objects.filter(exists=True)
        self.fields['sugestions'].queryset = Lesson.objects.filter(exists=True)

    class Meta:
        model = Lesson
        fields = (
        "discipline", "title", "description", "requirements", "sugestions", "maximum_hops", "errors_followed_to_obstacle", "errors_to_deficiency",
        "visible")
        widgets = {
            'discipline': HiddenInput(attrs={}),
            'title': TextInput(attrs={'required': 'required'}),
            'description': Textarea(attrs={'cols': 50, 'rows': 6, 'class': 'latex', 'required': 'required'}),
            'requirements': SelectMultiple(attrs={'class': 'full-size'}),
            'sugestions': SelectMultiple(attrs={'class': 'full-size'}),
            'maximum_hops': NumberInput(attrs={'required': 'required', 'min': '0'}),
            'errors_followed_to_obstacle': NumberInput(attrs={'required': 'required', 'min': '-1'}),
            'errors_to_deficiency': NumberInput(attrs={'required': 'required', 'min': '-1'}),
            'visible': CheckboxInput(attrs={}),
        }

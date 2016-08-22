# -*- encoding=utf-8 -*-

from askmath.models import Item, Lesson
from django.forms import ModelForm, CheckboxInput, Textarea, SelectMultiple, HiddenInput


class ItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['deficiencies'].queryset = Lesson.objects.filter(exists=True)

    class Meta:
        model = Item
        fields = ("position", "description", "correct", "deficiencies")
        widgets = {
            'position': HiddenInput(attrs={'class': 'hidden'}),
            'description': Textarea(attrs={'required': 'required', 'class': 'latex', 'rows': '1'}),
            'correct': CheckboxInput(attrs={}),
            "deficiencies": SelectMultiple(attrs={'class': 'full-size'}),
        }

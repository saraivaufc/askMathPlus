import datetime

from django import forms
from django.utils.translation import ugettext as _

from forum.models import *

class CreateThreadForm(forms.ModelForm):
    forum = forms.IntegerField(widget=forms.HiddenInput)
    title = forms.CharField(label=_("Title"), max_length=100)
    body = forms.CharField(label=_("Body"), widget=forms.Textarea(attrs={'rows':8, 'cols':50}))

    def __init__(self, forum, *args, **kw):
        super(CreateThreadForm, self).__init__(*args, **kw)
        self._forum = forum
        self.initial['forum'] = self._forum.id

    class Meta:
        model = Thread
        fields = ('forum', 'title', 'body', )


class ReplyForm(forms.Form):
    body = forms.CharField(label=_("Body"), widget=forms.Textarea(attrs={'rows':8, 'cols':50}))


class EditPost(forms.ModelForm):
    body = forms.CharField(label=_("Body"), widget=forms.Textarea(attrs={'rows':18, 'cols':50}))

    class Meta:
        model = Post
        fields = ('body',)

    def clean(self):
        if self.instance.thread.closed:
            raise forms.ValidationError(_('Editing posts is disabled in closed threads'))
        return super(EditPost, self).clean()

    def save(self, commit=True):
        instance = super(EditPost, self).save(commit=commit)
        instance.edited_at = datetime.datetime.now()
        if commit:
            instance.save()
        return instance

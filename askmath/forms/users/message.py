#-*- encoding=utf-8 -*-

from django import forms
from django.forms import ModelForm, TextInput, EmailInput, FileInput, Textarea
from django.utils.translation import ugettext_lazy as _
import hashlib

from askmath.models.users import Message
from nocaptcha_recaptcha.fields import NoReCaptchaField


class MessageForm(ModelForm):
	class Meta:
		model= Message
		fields = ("name", "email","message", "file")

		widgets = {
			'name': TextInput(attrs={'required': 'required', 'class':'input-control text full-size'}),
			'email': EmailInput(attrs={'required': 'required', 'class':'input-control email full-size'}),
			'message': Textarea(attrs={'required': 'required', 'class':'input-control textarea full-size'}),
		}


	def clean_file(self):
		file = self.cleaned_data["file"]
		try:
			if file and file.name.find('askmath') == -1:
				hash = hashlib.md5(file.read()).hexdigest()
				file.name = "askmath_" + "".join((hash, ".", file.name.split(".")[-1]))
		except:
			pass
		return file

class MessageFormRecaptcha(MessageForm):
	captcha = NoReCaptchaField()
	class Meta:
		model= MessageForm.Meta.model
		fields = ("name", "email","message", "file","captcha")
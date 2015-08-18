#-*- encoding=utf-8 -*-

from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput
from django.utils.translation import ugettext_lazy as _
import hashlib

from askmath.models.users import Person

class PersonForm(ModelForm):
	class Meta:
		model= Person
		fields = ("username", "name", "email","password", "profile_image")

		widgets = {
			'username': TextInput(attrs={'required': 'required', 'class':'input-control text full-size', 'autofocus': 'True', 'x-webkit-speech': 'x-webkit-speech'}),
			'name': TextInput(attrs={'required': 'required', 'class':'input-control text full-size' , 'x-webkit-speech': 'x-webkit-speech'}),
			'email': EmailInput(attrs={'required': 'required', 'class':'input-control email full-size', 'x-webkit-speech': 'x-webkit-speech'}),
			'password': PasswordInput(attrs={'required': 'required', 'class':'input-control password full-size', 'x-webkit-speech': 'x-webkit-speech'}),
		}


	def clean_profile_image(self):
		image = self.cleaned_data["profile_image"]
		try:
			if image and image.name.find('hash_') == -1:
				hash = hashlib.md5(image.read()).hexdigest()
				image.name = "hash_" + "".join((hash, ".", image.name.split(".")[-1]))
		except:
			pass
		return image
	
class PersonLoginForm(forms.Form):
	username = forms.CharField(label=_('Username'), help_text=_("Please enter you username."),
		widget=forms.TextInput(attrs={'required': 'required','autofocus': 'True' , 'class':'input-control text full-size'}), 
		error_messages={'required': _('Please enter you username.')} )
	password = forms.CharField(label=_('Password'), help_text=_('Please enter you password.'),
		widget=forms.PasswordInput(attrs={'required': 'required', 'class':'input-control password full-size'}),
		error_messages={'required': _('Please enter you password.')})

class PersonProfile(PersonForm):
	class Meta:
		model= Person
		fields = ("username", "name", "email","profile_image")
		widgets = {
			'username': TextInput(attrs={'required': 'required', 'class':'input-control text full-size', 'autofocus': 'True'}),
			'name': TextInput(attrs={'required': 'required', 'class':'input-control text full-size'}),
			'email': EmailInput(attrs={'required': 'required', 'class':'input-control email full-size'}),
		}

class PersonRecoverPassword(forms.Form):
	username = forms.CharField(label=_('Username'),help_text=_("Please enter you username."),
		widget=forms.TextInput(attrs={'required': 'required','autofocus': 'True' , 'class':'input-control text full-size'}), 
		error_messages={'required': _('Please enter you username.')})
	email = forms.EmailField(label=_('Email'), help_text=_("Please enter you email."),
		widget=forms.EmailInput(attrs={'required': 'required', 'class':'input-control email full-size'}),
		error_messages={'required': _('Please enter your email.')})
	
class PersonAlterPassword(forms.Form):
	old_password = forms.CharField(label=_('Old Password'),help_text=_("Please enter you old password."),
		widget=forms.PasswordInput(attrs={'required': 'required','autofocus': 'True' , 'class':'input-control text full-size'}), 
		error_messages={'required': _('Please enter you old password.')} )
	new_password = forms.CharField(label=_('New Password'),help_text=_("Please enter you new password."), 
		widget=forms.PasswordInput(attrs={'required': 'required', 'class':'input-control password full-size'}),
		error_messages={'required': _('Please enter you new password.')})
	confirm_password = forms.CharField(label=_('Confirm Password'), help_text=_("Please enter you new password."),
		widget=forms.PasswordInput(attrs={'required': 'required', 'class':'input-control password full-size'}),
		error_messages={'required': _('Please repeat your new password.')})



#-*- encoding=utf-8 -*-

from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput
from django.utils.translation import ugettext_lazy as _
import hashlib

from askmath.models.users import Person
from askmath.widgets.fields import AdvancedFileInput
from nocaptcha_recaptcha.fields import NoReCaptchaField

class PersonForm(ModelForm):
	#captcha = NoReCaptchaField()
	confirm_password = forms.CharField(label=_('Confirm Password'), help_text=_('Please enter you password.'), 
		widget=PasswordInput(attrs={'required': 'required', 'onchange':'validConfirmPassword();'}))
	class Meta:
		model= Person
		fields = ("name", "email","username", "password","confirm_password")
		widgets = {
			'username': TextInput(attrs={'required': 'required', 'autofocus': 'True'}),
			'name': TextInput(attrs={'required': 'required'}),
			'email': EmailInput(attrs={'required': 'required'}),
			'password': PasswordInput(attrs={'required': 'required'}),
			'confirm_password': PasswordInput(attrs={'required': 'required', 'onchange':'validConfirmPassword();'})
		}
	
class PersonLoginForm(forms.Form):
	username = forms.CharField(label=_('Username'), help_text=_("Please enter you username."),
		widget=forms.TextInput(attrs={'required': 'required','autofocus': 'True'}), 
		error_messages={'required': _('Please enter you username.')} )
	password = forms.CharField(label=_('Password'), help_text=_('Please enter you password.'),
		widget=forms.PasswordInput(attrs={'required': 'required'}),
		error_messages={'required': _('Please enter you password.')})
	#captcha = NoReCaptchaField(label=_("Captcha"), help_text=_('Check the option.'))

class PersonProfile(ModelForm):
	class Meta:
		model= Person
		fields = ("username", "name", "email","profile_image")
		widgets = {
			'username': TextInput(attrs={'required': 'required', 'autofocus': 'True'}),
			'name': TextInput(attrs={'required': 'required'}),
			'email': EmailInput(attrs={'required': 'required'}),
			'profile_image': AdvancedFileInput(attrs={}),
		}

	def clean_profile_image(self):
		profile_image = self.cleaned_data["profile_image"]
		try:
			if profile_image and profile_image.name.find('askmath') == -1:
				hash = hashlib.md5(profile_image.read()).hexdigest()
				profile_image.name = "askmath_" + "".join((hash, ".", profile_image.name.split(".")[-1]))
		except:
			pass
		return profile_image

class PersonRecoverPassword(forms.Form):
	email = forms.EmailField(label=_('Email'), help_text=_("Please enter you email."),
		widget=forms.EmailInput(attrs={'required': 'required'}),
		error_messages={'required': _('Please enter your email.')})
	#captcha = NoReCaptchaField()
	
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



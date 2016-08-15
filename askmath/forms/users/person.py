# -*- encoding=utf-8 -*-

import hashlib

from askmath.models.users import Person
from askmath.widgets.fields import AdvancedFileInput
from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from django.utils.translation import ugettext_lazy as _
from nocaptcha_recaptcha.fields import NoReCaptchaField

GROUPS = [
	('student', _('Student')),
	('assistant', _('Assistant')),
	('teacher', _('Teacher')),
	('administrator', _('Administrator')),
]

class LoginForm(forms.Form):
	email = forms.CharField(label=_('Email'), help_text=_("Please enter you email."),
							widget=forms.EmailInput(),
							error_messages={'required': _('Please enter you email.')})
	password = forms.CharField(label=_('Password'), help_text=_('Please enter you password.'),
							   widget=forms.PasswordInput(),
							   error_messages={'required': _('Please enter you password.')})
	#captcha = NoReCaptchaField(label=_('Captcha'), help_text=_("Please enter code of captcha."), error_messages={'required': _('Please enter you code of captcha.')})

	class Meta:
		fields = ("email", "password",)


class RegisterForm(ModelForm):
	#captcha = NoReCaptchaField()
	email = forms.EmailField(label=_('Email'), help_text=_("Please enter you email."), widget=forms.EmailInput(attrs={'required': 'required'}), error_messages={'required': _('Please enter your email.')})
	password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)
	group = forms.ChoiceField(label=_("Group"), choices=GROUPS)
	key = forms.CharField(label=_("Key"), max_length=6, required=False, widget=forms.PasswordInput(), help_text=_( "If you want to create a record in this group should have an access key for this, please contact the administrator."))

	class Meta:
		model = Person
		fields = ("first_name", "last_name", "email", "password", "group", "key", )


class ProfileForm(ModelForm):
	email = forms.EmailField(label=_('Email'), help_text=_("Please enter you email."), widget=forms.EmailInput(attrs={'required': 'required'}), error_messages={'required': _('Please enter your email.')})
	class Meta:
		model = Person
		fields = ("first_name", "last_name", "email", "profile_image")
		widgets = {
			'first_name': TextInput(attrs={'required': 'required', 'autofocus': 'True'}),
			'last_name': TextInput(attrs={'required': 'required'}),
			'name': TextInput(attrs={'required': 'required'}),
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


class RecoverPassword(forms.Form):
	email = forms.EmailField(label=_('Email'), help_text=_("Please enter you email."),
							 widget=forms.EmailInput(attrs={'required': 'required'}),
							 error_messages={'required': _('Please enter your email.')})
	#captcha = NoReCaptchaField()


class AlterPassword(forms.Form):
	old_password = forms.CharField(label=_('Old Password'), help_text=_("Please enter you old password."),
								   widget=forms.PasswordInput(attrs={'required': 'required', 'autofocus': 'True',
																	 'class': 'input-control text full-size'}),
								   error_messages={'required': _('Please enter you old password.')})
	new_password = forms.CharField(label=_('New Password'), help_text=_("Please enter you new password."),
								   widget=forms.PasswordInput(
									   attrs={'required': 'required', 'class': 'input-control password full-size'}),
								   error_messages={'required': _('Please enter you new password.')})
	confirm_password = forms.CharField(label=_('Confirm Password'), help_text=_("Please enter you new password."),
									   widget=forms.PasswordInput(
										   attrs={'required': 'required', 'class': 'input-control password full-size'}),
									   error_messages={'required': _('Please repeat your new password.')})

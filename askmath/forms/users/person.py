#-*- encoding=utf-8 -*-

from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput, Select
from django.utils.translation import ugettext_lazy as _
import hashlib

from askmath.models.users import Person
from askmath.widgets.fields import AdvancedFileInput
from nocaptcha_recaptcha.fields import NoReCaptchaField
from askmath.entities import person_types
from django.contrib.auth.hashers import make_password



class LoginForm(forms.Form):
    #captcha = NoReCaptchaField()
    email = forms.CharField(label=_('Email'), help_text=_("Please enter you email."),
        widget=forms.EmailInput(), 
        error_messages={'required': _('Please enter you email.')} )
    password = forms.CharField(label=_('Password'), help_text=_('Please enter you password.'),
        widget=forms.PasswordInput(),
        error_messages={'required': _('Please enter you password.')})

    class Meta:
        fields = ("email", "password")

class RegisterForm(ModelForm):
    #captcha = NoReCaptchaField()
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_(u'Password confirmation'), widget=forms.PasswordInput)
    GROUPS = [
        ('student',_('Student')),
        ('assistent',_('Assistent')),
        ('teacher',_('Teacher')),
        ('administrator',_('Administrator')),
    ]
    group = forms.ChoiceField(label=_("Group"), choices=GROUPS)
    key = forms.CharField(label=_("Key"), max_length=6, required=False,
        widget=forms.PasswordInput(), help_text=_("If you want to create a record in this group should have an access key for this, please contact the administrator."))
    class Meta:
        model= Person
        fields = ("first_name", "last_name","email","password", "password2", "group","key")

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2


class ProfileForm(ModelForm):
    class Meta:
        model= Person
        fields = ("first_name","last_name","email","profile_image")
        widgets = {
            'first_name': TextInput(attrs={'required': 'required', 'autofocus': 'True'}),
            'last_name': TextInput(attrs={'required': 'required'}),
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

class RecoverPassword(forms.Form):
    email = forms.EmailField(label=_('Email'), help_text=_("Please enter you email."),
        widget=forms.EmailInput(attrs={'required': 'required'}),
        error_messages={'required': _('Please enter your email.')})
    #captcha = NoReCaptchaField()
    
class AlterPassword(forms.Form):
    old_password = forms.CharField(label=_('Old Password'),help_text=_("Please enter you old password."),
        widget=forms.PasswordInput(attrs={'required': 'required','autofocus': 'True' , 'class':'input-control text full-size'}), 
        error_messages={'required': _('Please enter you old password.')} )
    new_password = forms.CharField(label=_('New Password'),help_text=_("Please enter you new password."), 
        widget=forms.PasswordInput(attrs={'required': 'required', 'class':'input-control password full-size'}),
        error_messages={'required': _('Please enter you new password.')})
    confirm_password = forms.CharField(label=_('Confirm Password'), help_text=_("Please enter you new password."),
        widget=forms.PasswordInput(attrs={'required': 'required', 'class':'input-control password full-size'}),
        error_messages={'required': _('Please repeat your new password.')})



#-*- encoding=utf-8 -*-

from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput, Select
from django.utils.translation import ugettext_lazy as _
import hashlib

from askmath.models.users import Person
from askmath.widgets.fields import AdvancedFileInput
from nocaptcha_recaptcha.fields import NoReCaptchaField
from askmath.entities import person_types 


class PersonForm(ModelForm):
    #captcha = NoReCaptchaField()
    confirm_password = forms.CharField(label=_('Confirm Password'), 
                                        help_text=_('Please enter you password.'),)
    user_type = forms.ChoiceField(label=_("User Type"), 
                             help_text=_('Please enter you type user.'), 
                             choices=person_types.TYPES, 
                             initial='STUDENT',)
    key = forms.CharField(label=_('Access Key'), help_text=_(u'Please enter you access key.'), required=False) 
    class Meta:
        model= Person
        fields = ("first_name","last_name", "email","username", "password","confirm_password","user_type", "key")
        widgets = {
            'first_name': TextInput(attrs={'autofocus': 'True'}),
            'last_name': TextInput(),
            'email': EmailInput(),
            'username': TextInput(),
            'password': PasswordInput(attrs={}),
            'confirm_password': PasswordInput(attrs={'onkeyup':'validConfirmPassword();'}),
            'user_type' : Select(attrs={''}),
        }
    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return password2
    
class PersonLoginForm(forms.Form):
    username = forms.CharField(label=_('Username'), help_text=_("Please enter you username."),
        widget=forms.TextInput(attrs={'required': 'required','autofocus': 'True'}), 
        error_messages={'required': _('Please enter you username.')} )
    password = forms.CharField(label=_('Password'), help_text=_('Please enter you password.'),
        widget=forms.PasswordInput(attrs={'required': 'required'}),
        error_messages={'required': _('Please enter you password.')})

    def clean_username(self):
        data = self.cleaned_data['username']
        if Person.objects.filter(username=data).exists():
            raise ValidationError(_(u'Username already taken.'))
        return data
            

class PersonProfile(ModelForm):
    class Meta:
        model= Person
        fields = ("first_name","last_name", "username","email","profile_image")
        widgets = {
            'first_name': TextInput(attrs={'required': 'required', 'autofocus': 'True'}),
            'last_name': TextInput(attrs={'required': 'required', 'autofocus': 'True'}),
            
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



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



class PersonForm(ModelForm):
    #captcha = NoReCaptchaField()
    password = forms.CharField(label=_('Password'), 
                                help_text=_('Please enter you password.'),
                                widget=forms.PasswordInput)
    confirm_password = forms.CharField(label=_('Confirm Password'), 
                                        help_text=_('Please confirm you password.'),
                                        widget=forms.PasswordInput(attrs={'onkeyup':'validConfirmPassword();'}))
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
            'username': TextInput(attrs={}),
            'password': PasswordInput(attrs={}),
        }
    def clean_password(self):
        password = str(self.cleaned_data.get('password'))
        print "Password=",password
        return make_password(password=password,
                                          salt='50000',
                                          hasher='md5')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        print "Confirm passowrd=",confirm_password
        confirm_password = make_password(password=confirm_password,
                                          salt='50000',
                                          hasher='md5')

        print password, '==', confirm_password

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return confirm_password
    
class PersonLoginForm(forms.Form):
    username = forms.CharField(label=_('Username'), help_text=_("Please enter you username."),
        widget=forms.TextInput(attrs={'required': 'required','autofocus': 'True'}), 
        error_messages={'required': _('Please enter you username.')} )
    password = forms.CharField(label=_('Password'), help_text=_('Please enter you password.'),
        widget=forms.PasswordInput(attrs={'required': 'required'}),
        error_messages={'required': _('Please enter you password.')})

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



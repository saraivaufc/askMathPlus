# -*- coding: utf-8 -*-


#IMPORTS PYTHON
from __future__ import unicode_literals

#IMPORTS DJANGO
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.template import defaultfilters
from django.forms import ModelForm
from django.contrib.auth.models import User

#IMPORTS SPIRIT

#IMPORTS USER_PROFILE_SPIRIT

#IMPORTS ASK



User = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_("Username or Email"), max_length=254)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email","username", "password","is_administrator", "is_staff", "is_moderator")
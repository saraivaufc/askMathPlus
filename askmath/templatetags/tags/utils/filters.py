# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.forms import CheckboxInput, RadioSelect, ClearableFileInput, Select, SelectMultiple, TextInput, \
    PasswordInput, EmailInput, Textarea
from django.utils.translation import ugettext as _
from .. import register


@register.filter(name='range')
def range_filter(number):
    return range(int(number))


@register.filter(name='is_false')
def is_false(arg):
    return arg is False


@register.filter(name='replace_to_space')
def replace_to_space(text, arg):
    return text.replace(arg, " ")


@register.filter(name='class_exists')
def class_exists(field, cl):
    pass


@register.filter(name='translate')
def translate(text):
    try:
        return _(text)
    except:
        return text


@register.filter(name='settings')
def settings_value(name):
    return getattr(settings, name, "")


@register.filter(name='parameters')
def parameters(function, *args):
    print args


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__


@register.filter(name='is_radio')
def is_radio(field):
    return field.field.widget.__class__.__name__ == RadioSelect().__class__.__name__


@register.filter(name='is_file')
def is_file(field):
    return field.field.widget.__class__.__name__ == ClearableFileInput().__class__.__name__


@register.filter(name='is_password')
def is_password(field):
    return field.field.widget.__class__.__name__ == PasswordInput().__class__.__name__


@register.filter(name='is_select')
def is_select(field):
    return field.field.widget.__class__.__name__ == Select().__class__.__name__ or field.field.widget.__class__.__name__ == SelectMultiple().__class__.__name__


@register.filter(name='is_text')
def is_text(field):
    return field.field.widget.__class__.__name__ == TextInput().__class__.__name__


@register.filter(name='is_email')
def is_email(field):
    return field.field.widget.__class__.__name__ == EmailInput().__class__.__name__


@register.filter(name='is_textarea')
def is_textarea(field):
    return field.field.widget.__class__.__name__ == Textarea().__class__.__name__

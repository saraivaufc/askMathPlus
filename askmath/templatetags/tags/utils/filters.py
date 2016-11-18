# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.forms import CheckboxInput, RadioSelect, ClearableFileInput, Select, SelectMultiple, TextInput, \
	PasswordInput, EmailInput, Textarea
from django.utils.translation import ugettext as _
from askmath.utils.lesson_sorting import LessonSorting
from askmath.models.state import StudentLessonState
import collections
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

@register.filter(name='show_signal_number')
def show_signal_number(number):
	if number > 0:
		return "+"+ str(number)
	else:
		return number


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

@register.filter(name='shuffle')
def shuffle(arg):
	tmp = list(arg)[:]
	random.shuffle(tmp)
	return tmp
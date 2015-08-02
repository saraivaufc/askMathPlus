# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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


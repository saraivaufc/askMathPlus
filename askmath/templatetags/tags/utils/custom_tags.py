# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .. import register
from django.conf import settings

@register.simple_tag(name='SETTINGS') 
def settings_value(name):
    return getattr(settings, name, "")
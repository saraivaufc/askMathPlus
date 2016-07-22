# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from .person import Person


class Administrator(Person):
    class Meta(Person.Meta):
        verbose_name = _(u"Administrator")
        verbose_name_plural = _(u"Administrators")

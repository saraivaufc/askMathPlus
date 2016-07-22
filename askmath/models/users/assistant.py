# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from .person import Person


class Assistant(Person):
		
	class Meta(Person.Meta):
		verbose_name = _(u"Assistant")
		verbose_name_plural = _(u"Assistants")
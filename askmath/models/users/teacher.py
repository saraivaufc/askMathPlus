# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models
from person import Person


class Teacher(Person):

	class Meta(Person.Meta):
		verbose_name = _('teacher')
		verbose_name_plural = _('teachers')
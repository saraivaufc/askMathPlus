from askmath.models import RegisterKey
from django.db import models
from django.utils.translation import ugettext as _


class PersonKey(RegisterKey):
	person = models.ForeignKey("Person", related_name="Person", null=True, blank=True)

	def get_person(self):
		return self.person

	def add_user(self, user):
		self.person = person
		self.in_use = True
		self.save()

	class Meta:
		ordering = ['person']
		verbose_name = _(u"Person Key")
		verbose_name_plural = _(u"Persons Key")
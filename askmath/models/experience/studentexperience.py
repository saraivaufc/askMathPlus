from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.conf import settings


class StudentExperience(models.Model):
	student = models.ForeignKey('Student', verbose_name=_(u"Student"))
	scores = models.IntegerField(default=0, verbose_name=_(u"Scores"))
	full_scores = models.IntegerField(default=0, verbose_name=_(u"Full Scores"))
	new_scores = models.IntegerField(default=0, verbose_name=_(u"New Scores"))
	max_scores = models.IntegerField(default=10, verbose_name=_(u"Max Scores"))
	level = models.IntegerField(default=1, verbose_name=_(u"Level"))
	stars = models.IntegerField(default=0, verbose_name=_(u"Stars"))
	new_round = models.BooleanField(default=True)
	creation = models.DateTimeField(_('Creation'), default=timezone.now)
	exists = models.BooleanField(default=True)

	def get_student(self):
		return self.student

	def get_scores(self):
		return self.scores

	def get_full_scores(self):
		return self.full_scores	

	def get_new_scores(self):
		return self.new_scores

	def get_max_scores(self):
		return self.max_scores

	def get_level(self):
		return self.level

	def get_stars(self):
		return self.stars

	def is_new_round():
		return self.new_round

	def up_scores(self, scores):
		self.full_scores += scores
		self.scores += scores
		if self.scores >= self.max_scores:
			self.scores = self.scores - self.max_scores
			self.max_scores += self.max_scores
			self.up_stars()
		self.save()

	def down_scores(self, scores):
		self.scores = self.scores - scores
		if self.scores < 0:
			self.scores = 0
			self.down_stars()
		self.save()

	def up_stars(self):
		self.stars = self.stars + 1
		if self.stars >= 10:
			self.stars = 0
			self.up_level()
		self.save()

	def down_stars(self):
		self.stars = self.stars - 1
		if self.stars < 0:
			self.stars = 0
			self.down_level()
		self.save()

	def up_level(self):
		self.level += 1
		if self.level > 6:
			self.level = 6;
		self.max_scores += self.max_scores * 2
		self.save()

	def down_level(self):
		self.level = self.level - 1
		self.stars = 0
		if self.level == 0:
			self.level = 1
		self.save()

	def delete(self):
		self.exists = False
		self.save()

	def restore(self):
		self.exists = True
		self.save()

	def __unicode__(self):
		return unicode(self.student)

	class Meta:
		ordering = ['creation']
		verbose_name = _(u"Student Experience")
		verbose_name_plural = _(u"Student Experiences")

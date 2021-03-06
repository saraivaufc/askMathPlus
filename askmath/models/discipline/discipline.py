from askMathPlus.settings import generate_color, COLORS_ALL
from askmath.models.lesson import Lesson
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class Discipline(models.Model):
	title = models.CharField(verbose_name=_(u"Title"), max_length=100, help_text=_(u"Choose a title for the discipline."))
	visible = models.BooleanField(verbose_name=_(u"Visible"), default=False, help_text=_(u"Select this option to leave visible discipline at all."))
	color = models.CharField(verbose_name=_('Color'), max_length=50, default=generate_color, choices=COLORS_ALL, help_text=_(u"Choose a color for the discipline."))
	creation = models.DateTimeField(verbose_name=_('Creation'), default=timezone.now)
	exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)

	def get_title(self):
		return self.title

	def get_lessons(self):
		lessons = Lesson.objects.filter(exists=True, discipline=self.id).order_by('title')
		return lessons

	def get_lessons_visibles(self):
		lessons = Lesson.objects.filter(exists=True, visible=True, discipline=self.id).order_by('title')
		return lessons

	def get_lessons_removed(self):
		lessons = Lesson.objects.filter(exists=False, discipline=self.id).order_by('title')
		return lessons

	def delete(self):
		self.exists = False
		self.save()

	def restore(self):
		self.exists = True
		self.save()

	def is_visible(self):
		return self.visible

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['title']
		verbose_name = _(u"Content")
		verbose_name_plural = _(u"Content")

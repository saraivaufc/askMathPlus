#-*- encoding=UTF-8 -*-

from datetime import datetime
from django.db import models
from django.utils.translation import ugettext as _
from askMathPlus.settings import generate_color
import os

class Video(models.Model):
	lesson = models.ForeignKey('Lesson', verbose_name=_("Lesson"),
		help_text=_("Choose the lesson which is video belongs."))
	position = models.IntegerField(verbose_name=_("Position"),null=True,blank=True, 
		help_text=_("Choose the position which is video belongs."))
	title = models.CharField(verbose_name=_("Title"), max_length=50,
		help_text=_("Choose a title for video is."))
	description = models.TextField(verbose_name=_("Description"),null=True, blank=True, 
		 help_text=_("Choose a description for video is."))
	file = models.FileField(verbose_name=_("File"), upload_to = 'documents/video/%Y/%m/%d',
		help_text=_("Perform upload a file."))
	
	color = models.CharField(verbose_name=_('Color'), max_length=50, default=generate_color)
	visible = models.BooleanField(verbose_name=_("Visible"), default=False,
		help_text=_("Select this option to leave visible video at all."))
	creation = models.DateTimeField(verbose_name=_('Creation'), default=datetime.now)
	exists = models.BooleanField(verbose_name=_("Exists"), default=True)
	
	def get_lesson(self):
		return self.lesson
	
	def get_position(self):
		videos_all = list(self.lesson.get_videos_visibles())
		if videos_all:
			videos_all.sort()
			for index, i in enumerate(videos_all):
				if i.id == self.id:
					return index+1
		else:
			return -1
	
	def get_title(self):
		return self.title
	
	def get_description(self):
		return self.description
	
	def get_file(self):
		return self.file
	
	def delete(self):
		self.exists = False
		self.save()
		
	def restore(self):
		self.exists = True
		self.save()	

	def is_visible(self):
		return self.visible

	def get_extension(self):
		basename, extension = os.path.splitext(self.file.url) 
		return extension

	def __unicode__(self):
		return self.title
	
	
	def __ge__(self, other):
		return self.position >= other.position
	
	def __gt__(self, other):
		return self.position > other.position
	
	def __le__(self, other):
		return self.position <= other.position 
	
	def __lt__(self, other):
		return self.position < other.position

	class Meta:
		ordering = ['position']
		verbose_name = _("Video")
		verbose_name_plural = _("Videos")

# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .person import Person

class Student(Person):

	classes = models.ManyToManyField('Classe', verbose_name=_(u"Classes"), related_name="Classes", null=True, blank=True,
		 help_text=_(u"Choose classe that this student.")) 
	current_classe = models.ForeignKey('Classe', verbose_name=_(u"Current Classe"), related_name="Current Classe", null=True, blank=True,
		help_text=_(u"Choose the current classe to this student."))

	def get_classes(self):
		return self.classes.filter(exists = True, visible = True)
		

	def get_current_classe(self):
		if self.current_classe != None and self.current_classe.exists and  self.current_classe.visible and self.current_classe in self.get_classes():
			return self.current_classe
		else:
			return None

	def set_current_classe(self, classe):
		if classe in self.get_classes():
			self.current_classe = classe
			self.save()
			return True
		else:
			return False

	def join_classe(self, student , classe):
		if not classe in self.get_classes():
			self.classes.add(classe)
			classe.add_student(student)
			self.set_current_classe(classe)
			return True
		else:
			return False

	def out_classe(self, student ,  classe):
		if classe in self.get_classes():
			current_classe = self.get_current_classe()
			self.classes.remove(classe)
			classe.remove_student(student)
			if classe == current_classe:
				classes = self.get_classes()
				if len(classes) > 0:
					self.set_current_classe(classes[0])
			return True
		else:
			return False

	class Meta(Person.Meta):
		verbose_name = _(u'Student')
		verbose_name_plural = _(u'Students')
from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from askMathPlus.settings import generate_color, COLORS_ALL
from askmath.models.users import Student as StudentModel

class Classe(models.Model):
	name = models.CharField(verbose_name=_(u"Name"), max_length=100,
		help_text=_(u"Choose a name for the classe."))
	
	responsible = models.ForeignKey('Teacher',related_name="Responsible", verbose_name=_('Responsible'), null=True, blank=True,
		help_text=_(u"Choose responsible for the classe."))
	
	semester = models.FloatField(verbose_name=_(u"Semester"), 
		help_text=_(u"Choose semester of this classe."), null=False, blank=False)

	plan = models.FileField(verbose_name=_(u"Plan"), upload_to = 'documents/plans/%Y/%m/%d',
		help_text=_(u"Perform upload a file."), null=True, blank=True)
	
	disciplines = models.ManyToManyField('Discipline', verbose_name=_(u"Disciplines"), null=True, blank=True,
         help_text=_(u"Choose disciplines that this classe."))

	students = models.ManyToManyField('Student', verbose_name=_(u"Students"), null=True, blank=True,
         help_text=_(u"Choose students that this classe."))

	visible = models.BooleanField(verbose_name=_(u"Visible"), default=False,
		help_text=_(u"Select this option to leave visible classe at all."))

	color = models.CharField(verbose_name=_('Color'), max_length=50, default=generate_color, choices=COLORS_ALL,
		help_text=_(u"Choose a color for the classe."))
	
	creation = models.DateTimeField(verbose_name=_('Creation'), default=timezone.now)
	exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)
	
	def get_name(self):
		return self.name
	
	def get_responsible(self):
		return self.responsible
	
	def get_semester(self):
		return self.semester

	def get_disciplines(self, visible=True): 
		return self.disciplines.filter(exists=True, visible=visible)

	def get_students(self):
		return self.students.filter(exists=True)

	def add_student(self, student):
		if not student in self.get_students():
			self.students.add(student)
			return True
		else:
			return False
	def remove_student(self, student):
		if student in self.get_students():
			self.students.remove(student)
			return True
		else:
			return False

	def delete(self):
		self.exists = False
		self.save()
		
	def restore(self):
		self.exists = True
		self.save()
		
	def is_visible(self):
		return self.visible
	
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _(u"Classe")
		verbose_name_plural = _(u"Classes")

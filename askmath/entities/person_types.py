#-*- encoding=UTF-8 -*-
from askmath.models.users import Administrator, Teacher, Assistant, Student
from askmath.forms.users import AdministratorForm, TeacherForm, AssistantForm, StudentForm
from django.utils.translation import ugettext as _
class PersonTypes():
	ADMIN = _(u"administrator")
	TEACHER = _(u"teacher")
	ASSISTANT = _(u"assistant")
	STUDENT = _(u"student")
	
	def __init__(self, PERSONTYPE=None):
		self.PERSONTYPE = PERSONTYPE
		self.types = {self.ADMIN : {"color": "bg-indigo"}, 
					  self.TEACHER : {"color":"bg-yellow"},
					  self.ASSISTANT : {"color": "bg-emerald"},
					  self.STUDENT : {"color": "bg-darkCyan"},}
	
	def get_types(self):
		return self.types

	def get_persons(self):
		if self.PERSONTYPE == self.ADMIN:
			return Administrator.objects.filter(exists=True)
		elif self.PERSONTYPE == self.TEACHER:
			return Teacher.objects.filter(exists=True)
		elif self.PERSONTYPE == self.ASSISTANT:
			return Assistant.objects.filter(exists=True)
		elif self.PERSONTYPE == self.STUDENT:
			return Student.objects.filter(exists=True)
		else:
			return []
	
	def get_persons_removed(self):
		if self.PERSONTYPE == self.ADMIN:
			return Administrator.objects.filter(exists=False)
		elif self.PERSONTYPE == self.TEACHER:
			return Teacher.objects.filter(exists=False)
		elif self.PERSONTYPE == self.ASSISTANT:
			return Assistant.objects.filter(exists=False)
		elif self.PERSONTYPE == self.STUDENT:
			return Student.objects.filter(exists=False)
		else:
			return []
		
	def get_person_form(self, method=None, files=None, instance=None):
		if self.PERSONTYPE == self.ADMIN:
			return AdministratorForm(method, files, instance=instance)
		elif self.PERSONTYPE == self.TEACHER:
			return TeacherForm(method, files, instance=instance)
		elif self.PERSONTYPE == self.ASSISTANT:
			return AssistantForm(method, files, instance=instance)
		elif self.PERSONTYPE == self.STUDENT:
			return StudentForm(method, files, instance=instance)
		else:
			return None
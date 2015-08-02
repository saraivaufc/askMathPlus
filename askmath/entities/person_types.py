#-*- encoding=UTF-8 -*-
from askmath.models.users import Administrator, Teacher, Assistant, Student
from askmath.forms.users import AdministratorForm, TeacherForm, AssistantForm, StudentForm
from django.utils.translation import ugettext as _

class PersonTypes():
    ADMIN = _("administrator")
    TEACHER = _("teacher")
    ASSISTANT = _("assistant")
    STUDENT = _("student")
    
    def __init__(self, PERSONTYPE=None):
        self.PERSONTYPE = PERSONTYPE
    
    def get_types(self):
        types = []
        types.append(self.ADMIN)
        types.append(self.TEACHER)
        types.append(self.ASSISTANT)
        types.append(self.STUDENT)
        return types
    
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
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group
from askMathPlus.settings import COLORS_ALL
from askmath.entities import Message, TextMessage, TypeMessage
from django.utils.translation import ugettext_lazy as _

try:
    from hashlib import md5
except:
    from md5 import new as md5


from askmath.entities import PersonTypes
from askmath.forms import PersonForm
from askmath.models.access import AdministratorKey, TeacherKey, AssistantKey

from .iperson import IPerson


class Person(IPerson):
    
    def choose_person_types(self, request, message=None):
        person_types = PersonTypes()
        return render(request, "askmath/manager/person/manager_choose_person_types.html",
            {'request':request,'person_types': person_types.get_types(), 'colors': COLORS_ALL, 'message': message})
    
    
    def view_persons(self, request, PERSONTYPE, message=None):
        person_types = PersonTypes(PERSONTYPE)
        if PERSONTYPE == person_types.ADMIN:
            write_person = request.user.has_perm('askmath.write_administrator')
        elif PERSONTYPE == person_types.TEACHER:
            write_person = request.user.has_perm('askmath.write_teacher')
        elif PERSONTYPE == person_types.ASSISTANT:
            write_person = request.user.has_perm('askmath.write_assitant')
        elif PERSONTYPE == person_types.STUDENT:
            write_person = request.user.has_perm('askmath.write_student')
        else:
            write_person = False
            
        persons = person_types.get_persons()
        return render(request, "askmath/manager/person/manager_view_persons.html",
            {'request':request,'persons': persons,'person_type': PERSONTYPE,'write_person': write_person, 'colors': COLORS_ALL, 'message': message})
    
    def view_persons_removed(self, request, PERSONTYPE, message=None):
        person_types = PersonTypes(PERSONTYPE)
        if PERSONTYPE == person_types.ADMIN:
            write_person = request.user.has_perm('askmath.write_administrator')
        elif PERSONTYPE == person_types.TEACHER:
            write_person = request.user.has_perm('askmath.write_teacher')
        elif PERSONTYPE == person_types.ASSISTANT:
            write_person = request.user.has_perm('askmath.write_assitant')
        elif PERSONTYPE == person_types.STUDENT:
            write_person = request.user.has_perm('askmath.write_student')
        else:
            write_person = False
        persons = person_types.get_persons_removed()
        return render(request, "askmath/manager/person/manager_view_persons.html",
            {'request':request,'persons': persons,'person_type': PERSONTYPE,'write_person': write_person ,'is_removed': True , 'colors': COLORS_ALL, 'message': message})
        
    def view_person(self,request, PERSONTYPE,person, message=None ):
        person_types = PersonTypes(PERSONTYPE)
        if PERSONTYPE == person_types.ADMIN:
            write_person = request.user.has_perm('askmath.write_administrator')
        elif PERSONTYPE == person_types.TEACHER:
            write_person = request.user.has_perm('askmath.write_teacher')
        elif PERSONTYPE == person_types.ASSISTANT:
            write_person = request.user.has_perm('askmath.write_assitant')
        elif PERSONTYPE == person_types.STUDENT:
            write_person = request.user.has_perm('askmath.write_student')
        else:
            write_person = False
        return render(request, "askmath/manager/person/manager_view_person.html", 
            {'request':request,'person': person,'person_type': PERSONTYPE,'write_person': write_person,'message': message, 'colors': COLORS_ALL })
    
    
    def add_person(self,request, PERSONTYPE,message=None ):
        person_types = PersonTypes(PERSONTYPE)
        new_register_key = None
        register_keys = None
        if PERSONTYPE == person_types.ADMIN:
            if request.method == "POST":
                new_register_key =  AdministratorKey.objects.create(creator=request.user)
            register_keys = AdministratorKey.objects.filter(exists = True)
        elif PERSONTYPE == person_types.TEACHER:
            if request.method == "POST":
                new_register_key =  TeacherKey.objects.create(creator=request.user)
            register_keys = TeacherKey.objects.filter(exists = True)
        elif PERSONTYPE == person_types.ASSISTANT:
            if request.method == "POST":
                new_register_key =  AssistantKey.objects.create(creator=request.user)
            register_keys = AssistantKey.objects.filter(exists = True)
        else:
            register_keys = None
        return render(request, "askmath/manager/person/manager_view_keys.html", 
            {'request':request, 'person_type': PERSONTYPE ,'new_register_key': new_register_key ,'register_keys': register_keys, 'message': message})

    
    def remove_person(self, request, PERSONTYPE, person,message=None ):
        person.delete()
        message = Message(TextMessage.PERSON_SUCCESS_REM, TypeMessage.SUCCESS)
        return self.view_persons(request,PERSONTYPE, message)
    
    def remove_registerkey(self, request, PERSONTYPE, registerkey,message=None ):
        if not registerkey.get_user():
            registerkey.delete()
        else:
            message = Message(TextMessage.KEY_ERROR_REMOVE_USED, TypeMessage.WARNING)
        return self.add_person(request, PERSONTYPE, message)

    def restore_person(self, request, PERSONTYPE, person):
        person.restore()
        message = Message(TextMessage.PERSON_SUCCESS_RESTORE, TypeMessage.SUCCESS)
        return self.view_persons(request,PERSONTYPE, message)
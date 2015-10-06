from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group
from askmath.entities import TextMessage
from django.contrib import messages
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
    
    def choose_person_types(self, request):
        person_types = PersonTypes()
        return render(request, "askmath/manager/person/manager_choose_person_types.html",
            {'request':request,'person_types': person_types})
    
    
    def view_persons(self, request, PERSONTYPE):
        person_types = PersonTypes(PERSONTYPE)
        if PERSONTYPE == person_types.ADMIN:
            print "ADMIN"
            write_person = request.user.has_perm('askmath.write_administrator')
        elif PERSONTYPE == person_types.TEACHER:
            print "TEACHER"
            write_person = request.user.has_perm('askmath.write_teacher')
        elif PERSONTYPE == person_types.ASSISTANT:
            print "ASSISTANT"
            write_person = request.user.has_perm('askmath.write_assistant')
        elif PERSONTYPE == person_types.STUDENT:
            write_person = False
            print "STUDENT"
        else:
            print "OTHER"
            write_person = False
            
        persons = person_types.get_persons()
        return render(request, "askmath/manager/person/manager_view_persons.html",
            {'request':request,'persons': persons,'person_type': PERSONTYPE,'write_person': write_person})
    
    def view_persons_removed(self, request, PERSONTYPE):
        person_types = PersonTypes(PERSONTYPE)
        if PERSONTYPE == person_types.ADMIN:
            write_person = request.user.has_perm('askmath.write_administrator')
        elif PERSONTYPE == person_types.TEACHER:
            write_person = request.user.has_perm('askmath.write_teacher')
        elif PERSONTYPE == person_types.ASSISTANT:
            write_person = request.user.has_perm('askmath.write_assistant')
        elif PERSONTYPE == person_types.STUDENT:
            write_person = False
        else:
            write_person = False
        persons = person_types.get_persons_removed()
        return render(request, "askmath/manager/person/manager_view_persons.html",
            {'request':request,'persons': persons,'person_type': PERSONTYPE,'write_person': write_person ,'is_removed': True })
        
    def view_person(self,request, PERSONTYPE,person ):
        person_types = PersonTypes(PERSONTYPE)
        if PERSONTYPE == person_types.ADMIN:
            write_person = request.user.has_perm('askmath.write_administrator')
        elif PERSONTYPE == person_types.TEACHER:
            write_person = request.user.has_perm('askmath.write_teacher')
        elif PERSONTYPE == person_types.ASSISTANT:
            write_person = request.user.has_perm('askmath.write_assistant')
        elif PERSONTYPE == person_types.STUDENT:
            write_person = request.user.has_perm('askmath.write_student')
        else:
            write_person = False
        return render(request, "askmath/manager/person/manager_view_person.html", 
            {'request':request,'person': person,'person_type': PERSONTYPE,'write_person': write_person})
    
    
    def add_person(self,request, PERSONTYPE):
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
            {'request':request, 'person_type': PERSONTYPE ,'new_register_key': new_register_key ,'register_keys': register_keys})

    
    def remove_person(self, request, PERSONTYPE, person):
        person.delete()
        messages.success(request,TextMessage.USER_SUCCESS_REM)
        return self.view_persons(request,PERSONTYPE)
    
    def remove_registerkey(self, request, PERSONTYPE, registerkey):
        if not registerkey.get_user():
            registerkey.delete()
        else:
            messages.warning(request, TextMessage.KEY_ERROR_REMOVE_USED)
        return self.add_person(request, PERSONTYPE)

    def restore_person(self, request, PERSONTYPE, person):
        person.restore()
        messages.success(request,TextMessage.USER_SUCCESS_RESTORE)
        return self.view_persons(request,PERSONTYPE)
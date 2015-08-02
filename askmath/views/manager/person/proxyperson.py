from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.entities import PersonTypes
from askmath.models.users import Person as PersonModel
from askmath.views.initial import Home

from .iperson import IPerson
from .person import Person



class ProxyPerson(IPerson):
    def __init__(self):
        self.__person = Person()
        self.__home = Home()
        
    def choose_person_types(self, request, message=None):
        if request.user.has_perm("askmath.read_person"):
            try:
                return self.__person.choose_person_types(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__home.index(request, message)
    
    def view_persons(self, request, PERSONTYPE, message=None):
        if request.user.has_perm("askmath.read_person"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types():
                    return self.__person.view_persons(request, PERSONTYPE, message)
                else:
                    message = Message(TextMessage.ERROR, TypeMessage.ERROR)
            except:
                message = Message(TextMessage.ERROR_GET_PARAMETERS, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.choose_person_types(request, message)
    
    def view_persons_removed(self, request, PERSONTYPE, message=None):
        if request.user.has_perm("askmath.read_person"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types():
                    return self.__person.view_persons_removed(request, PERSONTYPE, message)
                else:
                    message = Message(TextMessage.ERROR, TypeMessage.ERROR)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.choose_person_types(request, message)
    
    def view_person(self, request, PERSONTYPE, id_person, message=None):
        if request.user.has_perm("askmath.read_person"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types():
                    person = PersonModel.objects.get(id = id_person)
            except:
                message = Message(TextMessage.PERSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_persons(request, PERSONTYPE, message)
            try:
                return self.__person.view_person(request, PERSONTYPE, person)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_persons(request, PERSONTYPE, message)
    
    def add_person(self, request, PERSONTYPE, message=None):
        if request.user.has_perm("askmath.write_person"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types():
                    return self.__person.add_person(request, PERSONTYPE)
            except:
                message = Message(TextMessage.PERSON_ERROR_ADD, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_persons(request, PERSONTYPE, message)
    
    
    def remove_person(self, request, PERSONTYPE, id_person, message=None):
        if request.user.has_perm("askmath.write_person"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types():
                    person = PersonModel.objects.get(id = id_person)
            except:
                message = Message(TextMessage.PERSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_persons(request, PERSONTYPE, message)
            try:
                return self.__person.remove_person(request, PERSONTYPE, person)
            except:
                message = Message(TextMessage.PERSON_ERROR_REM, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_persons(request, PERSONTYPE, message)
    
    def restore_person(self, request, PERSONTYPE, id_person, message=None):
        if request.user.has_perm("askmath.write_person"):
            try:
                person_types = PersonTypes()
                if PERSONTYPE in person_types.get_types():
                    person = PersonModel.objects.get(id = id_person)
            except:
                message = Message(TextMessage.PERSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_persons(request, PERSONTYPE, message)
            try:
                return self.__person.restore_person(request, PERSONTYPE, person)
            except:
                message = Message(TextMessage.PERSON_ERROR_RESTORE, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_persons(request, PERSONTYPE, message)
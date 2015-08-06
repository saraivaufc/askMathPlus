from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage

from askmath.forms.users import PersonAlterPassword

from .iperson import IPerson
from .person import Person
from .home import Home


class ProxyPerson(IPerson):
    def __init__(self):
        self.__person = Person()
        self.__home = Home()
        
    def view_profile(self, request, message=None):
        if request.user.is_authenticated():
            try:
                person = request.user
                return self.__person.view_profile(request, person, message=None)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_AUTHENTICATED, TypeMessage.ERROR)
        return self.__home.index(request, message)
    
    def edit_profile(self, request):
        if request.user.is_authenticated():
            #try:
            person = request.user
            return self.__person.edit_profile(request, person, message=None)
            #except:
            #   message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_AUTHENTICATED, TypeMessage.ERROR)
        return self.__home.index(request, message)
    
    def alter_password(self, request, message = None):
        if not request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        else:
            return self.__person.alter_password(request, message)
            
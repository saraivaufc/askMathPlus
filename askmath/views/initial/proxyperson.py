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
                return self.__person.view_profile(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_AUTHENTICATED, TypeMessage.ERROR)
        return self.__home.index(request, message)
    
    def edit_profile(self, request, message=None):
        if request.user.is_authenticated():
            #try:
            return self.__person.edit_profile(request, message)
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
            
    def remove_account(self, request, message=None):
        if not request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        else:
            if request.method == "POST":
                try:
                    password = request.POST['password']
                    return self.__person.remove_account(request, password, message)
                except:
                    message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
            else:
                message = Message(TextMessage.METHOD_NOT_POST, TypeMessage.ERROR)
        return self.view_profile(request, message)
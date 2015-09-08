from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from django.utils.translation import ugettext_lazy as _

from .iaccount import IAccount
from .account import Account
from askmath.models.users.student import Student
from askmath.forms.users import PersonLoginForm, PersonRecoverPassword

class ProxyAccount(IAccount):
    def __init__(self):
        self.__account = Account()
    
    def options(self, request, message=None):
        if request.user.is_authenticated():
            try:
                return redirect(request.GET['next'])
            except:
                return HttpResponseRedirect('/home/')

        if request.method == "POST":
            try:
                option = request.POST['option']
                if option == 'sign_in':
                    return self.signin(request, message)
                elif option == 'sign_up':
                    return self.signup(request, message)
                elif option == 'recover_password':
                    return self.recover_password(request, message)
                else:
                    return self.__account.options(request, message)
            except:
                pass
        try:
            return self.__account.options(request, message)
        except:
            return HttpResponseRedirect('/home/')
        
    
    def signin(self, request, message = None):
        if request.method == 'POST':
            form = PersonLoginForm(request.POST)
            if form.is_valid():
                try:
                    return self.__account.signin(request, form)
                except:
                    return self.options(request, message)
            else:
                pass
        request.method = 'GET'
        return self.options(request, message)
    
    def logout(self, request, message=None):
        if not request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        try:
            return self.__account.logout(request, message)
        except:
            message = Message(TextMessage.LOGOUT_ERROR, TypeMessage.ERROR)
        request.method = 'GET'
        return self.options(request, message)
    
    def signup(self, request, message=None):
        if request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        else:
            try:
                return self.__account.signup(request)
            except:
                message = Message(TextMessage.USER_CREATED_ERROR, TypeMessage.ERROR)
        request.method = 'GET'
        return self.options(request, message)
        
    def recover_password(self, request, message = None):
        if request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        else:
            if request.method == "POST":
                try:
                    _username = request.POST['username']
                    _email    = request.POST['email']
                    try:
                        user = Student.objects.get(username = str(_username), email = str(_email))
                        if user:
                            try:
                                return self.__account.recover_password(request, user)
                            except:
                                message = Message(TextMessage.EMAIL_RECOVER_PASSWORD_ERROR, TypeMessage.ERROR)    
                        else:
                            message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
                    except:
                        message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
                except:
                    message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
        request.method = 'GET'
        return self.options(request, message)
    
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
            return HttpResponseRedirect("/home/")
        return self.__account.options(request, message)
        
    
    def signin(self, request, message = None):
        if request.method == 'POST':
            form = PersonLoginForm(request.POST)
            if form.is_valid():
                return self.__account.signin(request, form)
            else:
                return render(request, 'askmath/authentication/login.html',
                    {'request': request,'form':form, 'message': message})
        return self.__account.options(request, message)
    
    def logout(self, request, message=None):
        if not request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        try:
            return self.__account.logout(request, message)
        except:
            pass
        return self.options(request, message)
    
    def signup(self, request, message=None):
        if request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        else:
            try:
                return self.__account.signup(request)
            except:
                pass
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
                            return self.__account.recover_password(request, user)
                        else:
                            message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
                    except:
                        message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
                except:
                    message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
        return self.options(request, message)
    
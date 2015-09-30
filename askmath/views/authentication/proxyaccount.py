from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import TextMessage
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .iaccount import IAccount
from .account import Account
from askmath.models.users.student import Student
from askmath.forms.users import PersonLoginForm, PersonRecoverPassword

class ProxyAccount(IAccount):
    def __init__(self):
        self.__account = Account()
    
    def options(self, request):
        if request.user.is_authenticated():
            try:
                return redirect(request.GET['next'])
            except Exception, e:
                print e
                return HttpResponseRedirect('/home/')

        if request.method == "POST":
            try:
                option = request.POST['option']
                if option == 'sign_in':
                    return self.signin(request)
                elif option == 'sign_up':
                    return self.signup(request)
                elif option == 'recover_password':
                    return self.recover_password(request)
                else:
                    return self.__account.options(request)
            except Exception, e:
                print e
        try:
            return self.__account.options(request)
        except Exception, e:
            print e
            return HttpResponseRedirect('/home/')
        
    
    def signin(self, request):
        if request.method == 'POST':
            form = PersonLoginForm(request.POST)
            if form.is_valid():
                try:
                    return self.__account.signin(request, form)
                except Exception, e:
                    print e
                    return self.options(request)
            else:
                messages.error(request, TextMessage.ERROR_FORM)
        request.method = 'GET'
        return self.options(request)
    
    def logout(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        try:
            return self.__account.logout(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.LOGOUT_ERROR)
        request.method = 'GET'
        return self.options(request)
    
    def signup(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        else:
            try:
                return self.__account.signup(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_CREATED_ERROR)
        request.method = 'GET'
        return self.options(request)
        
    def recover_password(self, request):
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
                                messages.error(request, TextMessage.EMAIL_RECOVER_PASSWORD_ERROR)
                        else:
                            messages.error(request, TextMessage.USER_NOT_FOUND)
                    except:
                        messages.error(request, TextMessage.USER_NOT_FOUND)
                except:
                    messages.error(request, TextMessage.ERROR_FORM)
        request.method = 'GET'
        return self.options(request)
    
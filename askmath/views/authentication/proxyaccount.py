from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import TextMessage
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from .iaccount import IAccount
from .account import Account
from askmath.models.users.student import Student
from askmath.forms.users import PersonLoginForm, PersonRecoverPassword
from askmath.views.index import ProxyHome

class ProxyAccount(IAccount):
    def __init__(self):
        self.__account = Account()
        self.__proxy_home = ProxyHome()
    
    def options(self, request):
        if request.user.is_authenticated():
            try:
                return redirect(request.GET['next'])
            except Exception, e:
                print e
                return self.__proxy_home.index(request)

        if request.method == "POST":
            try:
                option = request.POST['option']
                if option == 'sign_in':
                    return self.signin(request)
                elif option == 'sign_up':
                    return self.signup(request)
                elif option == 'recover_password':
                    return self.recover_password(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        return self.__account.options(request) 
    
    def signin(self, request):
        form = PersonLoginForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                return self.__account.signin(request, form)
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_CREATED_ERROR)
                return self.__account.options(request)
        else:
            print "signin - FORM INVALID"
            messages.error(request, TextMessage.ERROR_FORM)
        return self.__account.options(request)
    
    def signup(self, request):
        try:
            return self.__account.signup(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.USER_CREATED_ERROR)
            return self.__account.options(request)
        else:
            messages.error(request, TextMessage.ERROR_FORM)
        return self.__account.options(request)
        
    def recover_password(self, request):
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
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_NOT_FOUND)
        except Exception, e:
            print e
            messages.error(request, TextMessage.ERROR_FORM)

        return self.__account.options(request)

    def logout(self, request):
        try:
            return self.__account.logout(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.LOGOUT_ERROR)
        return self.__account.options(request)
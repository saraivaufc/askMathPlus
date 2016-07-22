from askmath.entities import TextMessage
from askmath.forms.users import LoginForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .account import Account
from .iaccount import IAccount


class ProxyAccount(IAccount):
    def __init__(self):
        self.__account = Account()

    def options(self, request):
        if request.user.is_authenticated():
            try:
                return redirect(request.GET['next'])
            except Exception, e:
                print e
                return HttpResponseRedirect(reverse('askmath:home'))
        if request.method == "POST":
            try:
                option = request.POST['option']
                if option == 'sign_in':
                    return self.signin(request)
                elif option == 'sign_up':
                    return self.signup(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        return self.__account.options(request)

    def signin(self, request):
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                return self.__account.signin(request, form)
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_CREATED_ERROR)
                return HttpResponseRedirect(reverse('askmath:authentication_options'))
        else:
            messages.error(request, TextMessage.ERROR_FORM)
        return HttpResponseRedirect(reverse('askmath:authentication_options'))

    def signup(self, request):
        try:
            return self.__account.signup(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.USER_CREATED_ERROR)
            return self.__account.options(request)
        else:
            messages.error(request, TextMessage.ERROR_FORM)
        return HttpResponseRedirect(reverse('askmath:authentication_options'))

    def logout(self, request):
        try:
            return self.__account.logout(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.LOGOUT_ERROR)
        return HttpResponseRedirect(reverse('askmath:authentication_options'))

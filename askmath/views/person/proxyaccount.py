from askmath.entities import TextMessage
from askmath.views.index import ProxyHome
from askmath.views.person.account import Account
from askmath.views.person.iaccount import IAccount
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProxyAccount(IAccount):
    def __init__(self):
        self.__account = Account()
        self.__proxy_home = ProxyHome()

    @method_decorator(login_required)
    def view_profile(self, request):
        try:
            return self.__account.view_profile(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.ERROR)
        return self.__proxy_home.index(request)

    @method_decorator(login_required)
    def edit_profile(self, request):
        try:
            return self.__account.edit_profile(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.ERROR)
        return self.__proxy_home.index(request)

    @method_decorator(login_required)
    def alter_password(self, request):
        try:
            return self.__account.alter_password(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.ERROR)
        return self.__proxy_home.index(request)

    @method_decorator(login_required)
    def remove_account(self, request):
        if request.method == "POST":
            try:
                password = request.POST['password']
                return self.__account.remove_account(request, password)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR_FORM)
        return self.view_profile(request)

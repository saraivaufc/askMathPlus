from askmath.entities import TextMessage
from askmath.forms import ProfileForm
from askmath.forms.users import AlterPassword
from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

try:
    from hashlib import md5
except:
    from md5 import new as md5
    
from askmath.views.person.iaccount import IAccount

class Account(IAccount):
    def view_profile(self, request):
        return render(request, "askmath/person/account/view_profile.html",
            {'request': request, 'person': request.user})
    
    def edit_profile(self, request):
        person = request.user
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=person)
            if form.is_valid():
                form.save()
                messages.success(request, TextMessage.USER_SUCCESS_EDIT)
                return self.view_profile(request)
        else:
            form = ProfileForm(instance=person)
        return render(request, "askmath/person/account/edit_profile.html",
            {'request': request, 'form': form, 'title_form': _("Edit Profile")})
        
    def alter_password(self, request):
        if request.method == "POST":
            form = AlterPassword(request.POST)
            if form.is_valid():
                old_Password = form.cleaned_data['old_password']
                new_Password = form.cleaned_data['new_password']
                if request.user.check_password(old_Password):
                    request.user.change_password(new_Password)
                    messages.success(request, TextMessage.CHANGED_PASSWORD_SUCCESS)
                else:
                    messages.warning(request, TextMessage.PASSWORD_INCORRECT)
            else:
                messages.error(request, TextMessage.ERROR_FORM)
            return self.view_profile(request)
        else:
            form = AlterPassword()
        return render(request, 'askmath/person/account/alter_password.html',
            {'request': request,'form': form, 'title_form': _("Alter Password")})
    
    def remove_account(self, request, password):
        if request.user.check_password(password):
            request.user.delete()
            from askmath.views.authentication.proxyaccount import ProxyPerson
            proxy_account = ProxyPerson()
            messages.success(request, TextMessage.ACCOUNT_SUCCESS_REMOVED)
            request.method = "GET"
            return proxy_account.logout(request)
        else:
            messages.warning(request, TextMessage.PASSWORD_INCORRECT)
        return self.view_profile(request)
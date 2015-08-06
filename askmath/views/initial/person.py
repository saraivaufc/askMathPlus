from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.forms import PersonProfile
from askmath.forms.users import PersonAlterPassword
from askmath.entities import Message, TextMessage, TypeMessage
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login as login_user

try:
    from hashlib import md5
except:
    from md5 import new as md5
    
from .iperson import IPerson

class Person(IPerson):
    def view_profile(self, request, person, message=None):
        return render(request, "askmath/home/person/view_profile.html",
            {'request': request, 'person': person, 'message': message})
    
    def edit_profile(self, request, person, message):
        if request.method == "POST":
            username = request.POST['username']
            form = PersonProfile(request.POST, request.FILES, instance=person)
            if form.is_valid():
                form.save()
                message = Message(TextMessage.PERSON_SUCCESS_EDIT, TypeMessage.SUCCESS)
                return self.view_profile(request, person, message)
        else:
            form = PersonProfile(instance=person)
        return render(request, "askmath/home/person/edit_profile.html",
            {'request': request, 'form': form, 'title_form': _("Edit Profile"), 'message': message})
        
    def alter_password(self, request, message=None):
        if request.method == "POST":
            form = PersonAlterPassword(request.POST)
            if form.is_valid():
                print "Form valid"
                old_Password = form.cleaned_data['old_password']
                new_Password = form.cleaned_data['new_password']
                if request.user.check_password(old_Password):
                    print "ok"
                    request.user.change_password(new_Password)
                    message = Message(TextMessage.CHANGED_PASSWORD_SUCCESS, TypeMessage.SUCCESS)
                else:
                    print "errro"
                    message = Message(TextMessage.PASSWORD_INCORRECT, TypeMessage.WARNING)
            else:
                print "Form invalid"
                message = Message(TextMessage.ERROR_FORM, TypeMessage.SUCCESS)
            return self.view_profile(request, request.user, message)
        else:
            form = PersonAlterPassword()
        return render(request, 'askmath/home/person/alter_password.html',
            {'request': request,'form': form, 'title_form': _("Alter Password"), 'message': message})
    
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.forms import PersonProfile
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
    
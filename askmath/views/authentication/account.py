from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import Group
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from askMathPlus.settings import LOGIN_URL
from askmath.entities import TextMessage
from askmath.forms import StudentForm, AssistantForm, TeacherForm, AdministratorForm, PersonForm
from askmath.forms.users import PersonLoginForm, PersonRecoverPassword, PersonAlterPassword
from askmath.models.access import AdministratorKey, TeacherKey, AssistantKey
from askmath.models.users import Student, Person as PersonModel

from .iaccount import IAccount


try:
    from hashlib import md5
except:
    from md5 import new as md5


class Account(IAccount):
    def options(self, request):
        form_signin = None
        form_signup = None
        form_recover_password = None
        tab_actived = None

        if request.method == 'POST':
            try:
                option = request.POST['option']
                if option == 'sign_in':
                    form_signin = PersonLoginForm(request.POST)
                    tab_actived = 'sign_in'
                elif option == 'sign_up':
                    form_signup = PersonForm(request.POST)
                    tab_actived = 'sign_up'
                elif option == 'recover_password':
                    form_recover_password = PersonRecoverPassword(request.POST)
                    tab_actived = 'recover_password'
            except Exception, e:
                print e
        if not form_signin:
            form_signin = PersonLoginForm()
        if not form_signup:
            form_signup = PersonForm()
        if not form_recover_password:
            form_recover_password = PersonRecoverPassword()

        return render(request, "askmath/authentication/options.html",
            {'request': request, 
            'form_signin': form_signin, 
            'form_signup':form_signup,
            'tab_actived': tab_actived})
    
    
    def signin(self, request, form=None):
        try:
            if request.method == 'GET': next = request.GET['next']
            elif request.method == 'POST': next = request.POST['next']
            else: next = None
        except Exception, e:
            print e
        if request.method == "POST":
            try:
                username =  form.cleaned_data['username']
                password =  form.cleaned_data['password']
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR_FORM)
                return self.options(request)
            
            person = authenticate(username=username, password=password)
            if person:
                login_user(request, person)
                if request.user.is_authenticated():
                    if next:
                        return HttpResponseRedirect(next)
                    else:
                        return HttpResponseRedirect("/home/")
                else:
                    messages.error(request, TextMessage.USER_NOT_AUTHENTICATED)
            else:
                messages.error(request, TextMessage.USERNAME_OR_PASSWORD_INCORRECT)
        return self.options(request)
    
    def signup(self, request):
        request.POST = request.POST.copy()
        request.POST['password'] =  md5(request.POST['password'] ).hexdigest()
        
        type = request.POST['user_type']
        form = None
        register_key = None
        
        if type == "STUDENT":
            form = StudentForm(request.POST, request.FILES)
            group_name = "student"
        else:
            key = request.POST['key']
            if type == "ASSISTANT":
                try:
                    register_key = AssistantKey.objects.get(key=key, exists=True, in_use=False)
                    form = AssistantForm(request.POST, request.FILES)
                    group_name = "assistant"
                except Exception, e:
                    print e
                    messages.error(request, TextMessage.KEY_NOT_FOUND)
                    return self.options(request)
            elif type == "TEACHER":
                try:
                    register_key = TeacherKey.objects.get(key=key, exists=True, in_use=False)
                    form = TeacherForm(request.POST, request.FILES)
                    group_name = "teacher"
                except Exception, e:
                    print e
                    messages.error(request, TextMessage.KEY_NOT_FOUND)
                    return self.options(request)
            elif type == "ADMINISTRATOR":
                try:
                    register_key = AdministratorKey.objects.get(key=key, exists=True, in_use=False)
                    form = AdministratorForm(request.POST, request.FILES)
                    group_name = "administrator"
                except Exception, e:
                    print e
                    messages.error(request, TextMessage.KEY_NOT_FOUND)
                    return self.options(request)
            else:
                messages.error(request, TextMessage.USER_TYPE_NOT_FOUND)
                return self.options(request)
        if form and form.is_valid():
            user=form.save(commit=False)
            user.save(group=group_name)
            if register_key:
                register_key.add_user(user)
            messages.success(request, TextMessage.USER_CREATED_SUCCESS)
            request.method="GET"
            return self.signin(request,form)

        return self.options(request)

    def logout(self, request):
        try:
            auth_logout(request)
        except Exception, e:
            print e
        return HttpResponseRedirect('/authentication/options/')
        
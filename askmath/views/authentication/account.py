from .iaccount import IAccount
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth import logout as auth_logout
from django.http.response import HttpResponseRedirect
from askmath.forms import StudentForm, AssistantForm, TeacherForm, AdministratorForm, PersonForm
from askMathPlus.settings import LOGIN_URL
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.models.users import Student, Person as PersonModel
from askmath.models.access import AdministratorKey, TeacherKey, AssistantKey
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from askmath.forms.users import PersonLoginForm, PersonRecoverPassword, PersonAlterPassword

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
            'form_recover_password':form_recover_password,
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
        
        type = request.POST['type']
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
            user=form.save()
            if register_key:
                register_key.add_user(user)
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            messages.success(request, TextMessage.USER_CREATED_SUCCESS)
            request.method="GET"
            return self.signin(request,form)

        return self.options(request)
        
    def recover_password(self, request, user=None):
        if request.method == "POST":
            import random, string
            try:
                new_password = ''.join(random.choice(string.ascii_letters) for x in range(10))
                user.change_password(new_password)
                msn =  _("Dean " + str(user.get_full_name()) + ",<br><br>username = " + str(user.username) + "<br>new password = " + str(new_password) + "<br>Sincerely, Team Askmath.")
                from askmath.utils.user import send_recover_password
                if send_recover_password():
                    messages.success(request, TextMessage.EMAIL_RECOVER_PASSWORD_SUCCESS)
                else:
                    messages.error(request, TextMessage.EMAIL_RECOVER_PASSWORD_ERROR)
            except Exception, e:
                print e
                messages.error(request, TextMessage.EMAIL_RECOVER_PASSWORD_ERROR)
            form = PersonRecoverPassword()
        else:
            return self.options(request)
    
    def logout(self, request):
        print "magaiver"
        try:
            auth_logout(request)
        except Exception, e:
            print e
        return self.options(request)
        
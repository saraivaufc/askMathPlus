from .iaccount import IAccount
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.views import logout as logout_sys
from django.http.response import HttpResponseRedirect
from askmath.forms import StudentForm, AssistantForm, TeacherForm, AdministratorForm, PersonForm
from askMathPlus.settings import LOGIN_URL
from askmath.entities import Message, TextMessage, TypeMessage
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
    def options(self, request, message=None):
        form_signin = PersonLoginForm()
        form_signup = PersonForm()
        form_recover_password = PersonRecoverPassword()
        return render(request, "askmath/authentication/options.html",
            {'request': request,'form_signin': form_signin, 'form_signup':form_signup,'form_recover_password':form_recover_password,'message':message})
    
    
    def signin(self, request, form=None, message=None):
        if request.method == "POST":
            try:
                username =  form.cleaned_data['username']
                password =  form.cleaned_data['password']
                try:
                    person = PersonModel.objects.get(username=username, exists=True)
                except:
                    person = False
                    message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
                if person:
                    user = authenticate(username=username, password=password)
                    if user:
                        login_user(request, user)
                        if request.user.is_authenticated():
                            print "Password correct"
                            return HttpResponseRedirect("/home/")
                        else:
                            message = Message(TextMessage.USER_NOT_AUTHENTICATED, TypeMessage.ERROR)
                    else:
                        message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
            except:
                message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
        else:
            return self.options(request, message)
    
    def logout(self, request, message=None):
        try:
            logout_sys(request)
        except:
            pass
        return self.options(request, message)
    
    def signup(self, request, message=None):
        if request.method == "POST":
            request.POST = request.POST.copy()
            try:
                request.POST['password'] =  md5(request.POST['password'] ).hexdigest()
                type = request.POST['type']
                form = None
                register_key = None
                
                if type == "STUDENT":
                    form = StudentForm(request.POST, request.FILES)
                    group_name = "student"
                elif type == "ASSISTANT":
                    try:
                        key = request.POST['key']
                        register_key = AssistantKey.objects.get(key=key, exists=True, in_use=False)
                        form = AssistantForm(request.POST, request.FILES)
                        group_name = "assistant"
                    except:
                        message = Message(TextMessage.KEY_NOT_FOUND, TypeMessage.ERROR)
                elif type == "TEACHER":
                    try:
                        key = request.POST['key']
                        register_key = TeacherKey.objects.get(key=key, exists=True, in_use=False)
                        form = TeacherForm(request.POST, request.FILES)
                        group_name = "teacher"
                    except:
                        message = Message(TextMessage.KEY_NOT_FOUND, TypeMessage.ERROR)
                elif type == "ADMINISTRATOR":
                    try:
                        key = request.POST['key']
                        register_key = AdministratorKey.objects.get(key=key, exists=True, in_use=False)
                        form = AdministratorForm(request.POST, request.FILES)
                        group_name = "administrator"
                    except:
                        message = Message(TextMessage.KEY_NOT_FOUND, TypeMessage.ERROR)
                else:
                    message = Message(TextMessage.USER_TYPE_NOT_FOUND, TypeMessage.ERROR)
                
                if form and form.is_valid():
                    user=form.save()
                    if register_key:
                        register_key.add_user(user)
                    group = Group.objects.get(name=group_name)
                    user.groups.add(group)
                    message = Message(TextMessage.USER_CREATED_SUCCESS, TypeMessage.SUCCESS)
                    request.method="GET"
                    return self.login(request,None, message)
                else:
                    if not message:
                        message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
            except:
                message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
        return self.options(request, message)
        
    def recover_password(self, request, user=None, message=None):
        if request.method == "POST":
            import random, string
            try:
                new_password = ''.join(random.choice(string.ascii_letters) for x in range(10))
                user.change_password(new_password)
                msn =  _("Dean " + str(user.get_full_name()) + ",<br><br>username = " + str(user.username) + "<br>new password = " + str(new_password) + "<br>Sincerely, Team Askmath.")
                if user.email_user(_('AskMath - Recover Password'), str(msn)) :
                    message = Message(TextMessage.EMAIL_RECOVER_PASSWORD_SUCCESS, TypeMessage.SUCCESS)
                else:
                    message = Message(TextMessage.EMAIL_RECOVER_PASSWORD_ERROR, TypeMessage.ERROR)
            except:
                message = Message(TextMessage.EMAIL_RECOVER_PASSWORD_ERROR, TypeMessage.ERROR)
            form = PersonRecoverPassword()
        else:
            return self.options(request, message)
        
from .iperson import IPerson
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.views import logout as logout_sys
from django.http.response import HttpResponseRedirect
from askmath.forms import StudentForm
from askMathPlus.settings import LOGIN_URL
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.models.users import Student, Person as PersonModel
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from askmath.forms.users import PersonLoginForm, PersonRecoverPassword

try:
    from hashlib import md5
except:
    from md5 import new as md5


class Person(IPerson):
    def login(self, request, form=None, message=None):
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
        form = PersonLoginForm()
        return render(request, 'askmath/authentication/login.html',
            {'request':request,'form': form, 'message': message})
    
    def logout(self, request):
        try:
            logout_sys(request)
        except:
            pass
        return HttpResponseRedirect("/home/")
    
    def signup(self, request, message=None):
        if request.method == "POST":
            request.POST = request.POST.copy()
            try:
                request.POST['password'] =  md5(request.POST['password'] ).hexdigest()
                form = StudentForm(request.POST, request.FILES)
                if form.is_valid():
                    user=form.save()
                    group = Group.objects.get(name='student') 
                    user.groups.add(group)
                    message = Message(TextMessage.USER_CREATED_SUCCESS, TypeMessage.SUCCESS)
                    request.method="GET"
                    return self.login(request,None, message)
                else:
                    message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
            except:
                message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
            return render(request, 'askmath/authentication/signup.html',
                {'request': request,'message': message, 'form': form})
        else:
            form = StudentForm()
            return render(request, 'askmath/authentication/signup.html', 
                {'request': request,'message': message, 'form': form, 'title_form': _("Register Student")})
        
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
            form = PersonRecoverPassword()
        return render(request, 'askmath/authentication/recover_password.html',
            {'request': request,'form': form, 'title_form': _("Recover Password"), 'message': message})
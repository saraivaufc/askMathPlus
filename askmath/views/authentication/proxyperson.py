from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from django.utils.translation import ugettext_lazy as _

from .iperson import IPerson
from .person import Person
from askmath.models.users.student import Student
from askmath.forms.users import PersonLoginForm, PersonRecoverPassword

class ProxyPerson(IPerson):
    def __init__(self):
        self.__person = Person()
    
    def login(self, request, message = None):
        if request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        if request.method == 'POST':
            form = PersonLoginForm(request.POST)
            if form.is_valid():
                return self.__person.login(request, form)
            else:
                return render(request, 'askmath/authentication/login.html',
                    {'request': request,'form':form, 'message': message})
        return self.__person.login(request)
    
    def logout(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        
        return self.__person.logout(request)
    
    def signup(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        else:
            return self.__person.signup(request)
        
    def recover_password(self, request, message = None):
        if request.user.is_authenticated():
            return HttpResponseRedirect("/home/")
        else:
            if request.method == "POST":
                try:
                    _username = request.POST['username']
                    _email    = request.POST['email']
                    try:
                        user = Student.objects.get(username = str(_username), email = str(_email))
                        if user:
                            return self.__person.recover_password(request, user)
                        else:
                            message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
                    except:
                        message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
                except:
                    message = Message(TextMessage.ERROR_FORM, TypeMessage.ERROR)
        return self.__person.recover_password(request, message=message)
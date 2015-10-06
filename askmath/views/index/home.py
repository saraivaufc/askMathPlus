# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import TextMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from askmath.models import Discipline
from askmath.forms import MessageForm
from askMathPlus.settings import  EMAIL_ADMINS, SITE_TITLE
from askmath.models.lesson.lesson import Lesson
from django.core.mail import send_mail
from .ihome import IHome
from askmath.utils.user import send_password_reset

class Home(IHome):
    def index(self, request):
        if request.user.is_authenticated():
            if request.user.has_perm('askmath.access_manager'):
                return render(request, 'askmath/manager/manager_home.html', 
                    {'request':request})
            else:
                return HttpResponseRedirect("/home/content/disciplines/view/")
        else:
            return render(request, 'askmath/index/home.html',
                {'request': request})
        
    def about(self, request):
        return render(request, 'askmath/index/about.html',
            {'request': request})
    
    def message(self, request):
        
        if request.method == "POST":
            form =  MessageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                try:
                    send_password_reset(request)
                except Exception, e:
                    print e
                messages.success(request,TextMessage.MESSAGE_SUCCESS_SEND)
                return self.index(request)
            else:
                messages.error(request, TextMessage.ERROR_FORM)
        else:
            form = MessageForm()
        return render(request, 'askmath/index/message.html', 
             {'request': request,'form':form})

    def terms(self, request):
        return render(request, 'askmath/index/terms.html', 
             {'request': request})

    def policies(self, request):
        return render(request, 'askmath/index/policies.html', 
             {'request': request})

        
    def credits(self, request):
        return render(request, 'askmath/index/credits.html', 
             {'request': request})


    def contents(self, request, lesson=None):
        if lesson:
            return render(request, 'askmath/index/contents_details.html',
                {'request': request,'lesson': lesson})
        else:
            disciplines = Discipline.objects.filter(exists=True, visible=True)
            return render(request, 'askmath/index/contents.html', 
                {'request': request,'disciplines': disciplines})
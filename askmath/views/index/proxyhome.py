# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from django.shortcuts import render, redirect
from askmath.models import Discipline
from askmath.forms import ContactForm
from askMathPlus.settings import  EMAIL_ADMINS, SITE_TITLE
from django.core.mail import EmailMessage
from askmath.models.lesson.lesson import Lesson
from .ihome import IHome

class ProxyHome(IHome):
    def index(self, request,  message = None):
        if request.user.is_authenticated():
            if request.user.has_perm('askmath.access_manager'):
                return render(request, 'askmath/manager/manager_home.html', 
                    {'request':request, 'message': message})
            else:
                disciplines = Discipline.objects.filter(exists=True, visible=True)
                return render(request, 'askmath/content/discipline/content_view_disciplines.html',
                    {'request': request,'disciplines':  disciplines ,'message': message})
        else:
            return render(request, 'askmath/index/home.html',
                {'request': request, 'message': message})
        
    def about(self, request, message = None):
        return render(request, 'askmath/index/about.html',
            {'request': request, 'message': message})
    
    def contact(self, request, message = None):
        if request.method == "POST":
            form =  ContactForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                email = EmailMessage(SITE_TITLE, form.cleaned_data['message'], to=['saraiva@alu.ufc.br'])
                try:
                    email.send()
                except:
                    pass
                message = Message(TextMessage.MESSAGE_SUCCESS_SEND, TypeMessage.SUCCESS)
                return self.index(request, message)
        else:
            form = ContactForm()
        return render(request, 'askmath/index/contact.html', 
             {'request': request,'form':form,'message': message})

    def terms(self, request, message = None):
        return render(request, 'askmath/index/terms.html', 
             {'request': request, 'message': message})

    def policies(self, request, message = None):
        return render(request, 'askmath/index/policies.html', 
             {'request': request, 'message': message})

        
    def credits(self, request, message = None):
        return render(request, 'askmath/index/credits.html', 
             {'request': request, 'message': message})


    def contents(self, request, id_lesson=None, message = None):
        if id_lesson:
            lesson = Lesson.objects.filter(exists=True, visible=True, id=id_lesson)[0]
            if lesson:
                return render(request, 'askmath/index/contents_details.html',
                    {'request': request,'lesson': lesson,'message': message})
            else:
                message= message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.INFO)
                return self.contents(request, None, message)
        else:
            disciplines = Discipline.objects.filter(exists=True, visible=True)
            return render(request, 'askmath/index/contents.html', 
                {'request': request,'disciplines': disciplines,'message': message})
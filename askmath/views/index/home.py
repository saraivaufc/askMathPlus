# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from django.shortcuts import render, redirect
from askmath.models import Discipline
from askmath.forms import ContactForm
from askMathPlus.settings import COLORS_ALL

class Home():
    def index(self, request,  message = None):
        if request.user.is_authenticated():
            if request.user.has_perm('askmath.access_manager'):
                return render(request, 'askmath/manager/manager_home.html', 
                    {'request':request, 'colors': COLORS_ALL, 'message': message})
            else:
                disciplines = Discipline.objects.filter(exists=True, visible=True)
                return render(request, 'askmath/content/discipline/content_view_disciplines.html',
                    {'request': request,'disciplines':  disciplines ,'colors': COLORS_ALL,'message': message})
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
                message = Message(TextMessage.MESSAGE_SUCCESS_SEND, TypeMessage.SUCCESS)
                return self.index(request, message)
        else:
            form = ContactForm()
        return render(request, 'askmath/index/contact.html', 
             {'request': request,'form':form,'message': message})

    def terms(self, request, message = None):
        return render(request, 'askmath/index/terms.html', 
             {'request': request, 'message': message})


    def contents(self, request, message = None):
        disciplines = Discipline.objects.filter(exists=True, visible=True)
        return render(request, 'askmath/index/contents.html', 
             {'request': request,'disciplines': disciplines,'colors': COLORS_ALL,'message': message})
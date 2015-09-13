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
from askmath.utils.ratelimit.decorators import ratelimit
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .home import Home

class ProxyHome(IHome):
    def __init__(self):
        self.__home = Home()
    def index(self, request,  message = None):
        if request.user.is_authenticated():
            try:
                return self.__home.index(request, message)
            except:
                pass
        else:
            return render(request, 'askmath/index/home.html',
                {'request': request, 'message': message})
        
    def about(self, request, message = None):
        try:
            return self.__home.about(request, message)
        except:
            return self.index(request, message)
    
    def contact(self, request, message = None):
        try:
            return self.__home.contact(request, message)
        except:
            return self.index(request, message)

    def terms(self, request, message = None):
        try:
            return self.__home.terms(request, message)
        except:
            return self.index(request, message)

    def policies(self, request, message = None):
        try:
            return self.__home.policies(request, message)
        except:
            return self.index(request, message)

        
    def credits(self, request, message = None):
        try:
            return self.__home.credits(request, message)
        except:
            return self.index(request, message)


    def contents(self, request, id_lesson=None, message = None):
        try:
            lesson = Lesson.objects.filter(exists=True, visible=True, id=id_lesson)[0]
        except:
            lesson = None
        try:
            return self.__home.contents(request, lesson, message)
        except:
            return self.index(request, message)
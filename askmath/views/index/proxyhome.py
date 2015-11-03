# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import TextMessage
from django.shortcuts import render, redirect
from askmath.models import Discipline
from askmath.forms import MessageForm
from askMathPlus.settings import  EMAIL_ADMINS, SITE_TITLE
from django.core.mail import EmailMessage
from askmath.models.lesson.lesson import Lesson
from .ihome import IHome
from askmath.utils.ratelimit.decorators import ratelimit
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .home import Home

class ProxyHome(IHome):
    def __init__(self):
        self.__home = Home()
    def index(self, request):
        if request.user.is_authenticated():
            try:
                return self.__home.index(request)
            except Exception, e:
                print e
        return render(request, 'askmath/index/home.html',
                {'request': request})
        
    def about(self, request):
        try:
            return self.__home.about(request)
        except Exception, e:
            print e
            messages.error(request,TextMessage.ERROR)
            return self.index(request)
    
    def message(self, request):
        try:
            return self.__home.message(request)
        except Exception, e:
            print e
            messages.error(request,TextMessage.ERROR)
            return self.index(request)

    def terms(self, request):
        try:
            return self.__home.terms(request)
        except Exception, e:
            print e
            messages.error(request,TextMessage.ERROR)
            return self.index(request)

    def policies(self, request):
        try:
            return self.__home.policies(request)
        except Exception, e:
            print e
            messages.error(request,TextMessage.ERROR)
            return self.index(request)

        
    def credits(self, request):
        try:
            return self.__home.credits(request)
        except Exception, e:
            print e
            messages.error(request,TextMessage.ERROR)
            return self.index(request)


    def contents(self, request, id_lesson=None):
        try:
            lesson = Lesson.objects.filter(exists=True, visible=True, id=id_lesson)[0]
        except Exception, e:
            print e
            lesson = None
        try:
            return self.__home.contents(request, lesson)
        except Exception, e:
            print e
            messages.error(request,TextMessage.ERROR)
            return self.index(request)
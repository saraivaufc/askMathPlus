# -*- coding: UTF-8 -*-

from askmath.entities import TextMessage
from askmath.models.lesson.lesson import Lesson
from django.contrib import messages
from django.shortcuts import render
from .home import Home
from .ihome import IHome


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
            messages.error(request, TextMessage.ERROR)
        return self.index(request)

    def message(self, request):
        try:
            return self.__home.message(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.ERROR)
        return self.index(request)

    def terms(self, request):
        try:
            return self.__home.terms(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.ERROR)
        return self.index(request)

    def policies(self, request):
        try:
            return self.__home.policies(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.ERROR)
        return self.index(request)

    def credits(self, request):
        try:
            return self.__home.credits(request)
        except Exception, e:
            print e
            messages.error(request, TextMessage.ERROR)
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
            messages.error(request, TextMessage.ERROR)
        return self.index(request)

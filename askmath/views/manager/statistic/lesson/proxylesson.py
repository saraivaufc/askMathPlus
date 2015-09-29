#-*- encoding=UTF-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.models import Lesson as ContactModel


from ..istatistic import IStatistic
from .ilesson import ILesson
from .lesson import Lesson
from ..proxystatistic import ProxyStatistic
class ProxyLesson(IStatistic, ILesson):
    def __init__(self):
        self.__contact = Lesson()
        self.__statistic = ProxyStatistic()
    
    def choose_lesson(self, request):
        if request.user.has_perm("askmath.read_statistics")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__contact.choose_lesson(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_statistics(request)
    
    def view_statistics(self, request,id_lesson):
        if request.user.has_perm("askmath.read_statistics")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request, 'answered_questions')
            
            try:
                return self.__contact.view_statistics(request,lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__statistic.choose_type(request)
    
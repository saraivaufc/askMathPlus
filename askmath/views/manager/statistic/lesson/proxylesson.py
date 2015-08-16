#-*- encoding=UTF-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from askmath.entities import Message, TextMessage, TypeMessage

from askmath.models import Lesson as ContactModel


from ..istatistic import IStatistic
from .ilesson import ILesson
from .lesson import Lesson
from ..proxystatistic import ProxyStatistic
class ProxyLesson(IStatistic, ILesson):
    def __init__(self):
        self.__contact = Lesson()
        self.__statistic = ProxyStatistic()
    
    def choose_lesson(self, request,message=None):
        if request.user.has_perm("askmath.read_statistics")  and request.user.has_perm("askmath.access_manager"):
            #try:
            return self.__contact.choose_lesson(request,message)
            #except:
            #  message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_statistics(request, message)
    
    def view_statistics(self, request,id_lesson, message=None):
        if request.user.has_perm("askmath.read_statistics")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request, 'answered_questions', message)
            
            #try:
            return self.__contact.view_statistics(request,lesson, message)
            #except:
            #  message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__statistic.choose_type(request, message)
    
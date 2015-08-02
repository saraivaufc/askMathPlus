#-*- encoding=UTF-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from askmath.entities import Message, TextMessage, TypeMessage

from askmath.models import Lesson as LessonModel


from ..istatistic import IStatistic
from .ilesson import ILesson
from .lesson import Lesson
from ..proxystatistic import ProxyStatistic
class ProxyLesson(IStatistic, ILesson):
    def __init__(self):
        self.__lesson = Lesson()
        self.__statistic = ProxyStatistic()
    
    def choose_lesson(self, request,message=None):
        if request.user.has_perm("askmath.read_statistics"):
            #try:
            return self.__lesson.choose_lesson(request,message)
            #except:
            #  message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_statistics(request, message)
    
    def view_statistics(self, request,id_lesson, message=None):
        if request.user.has_perm("askmath.read_statistics"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request, 'answered_questions', message)
            
            #try:
            return self.__lesson.view_statistics(request,lesson, message)
            #except:
            #  message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__statistic.choose_type(request, message)
    
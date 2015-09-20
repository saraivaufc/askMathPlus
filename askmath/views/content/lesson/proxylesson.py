from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#MODELS
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel

from askmath.entities import Message, TextMessage, TypeMessage
from askmath.views.index import ProxyHome

from .ilesson import ILesson
from .lesson import Lesson

class ProxyLesson(ILesson):
    
    def __init__(self):
        self.__contact = Lesson()
        self.__proxy_home = ProxyHome()

    @method_decorator(login_required)
    def view_lessons(self, request, message = None):            
        if request.user.has_perm("askmath.read_lesson")  and request.user.has_perm("askmath.access_content"):
            try:
                return self.__contact.view_lessons(request, message)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__proxy_home.index(request, message)
    
    @method_decorator(login_required)
    def view_lesson(self, request,id_discipline=None, id_lesson=None, message=None):
        if request.user.has_perm("askmath.read_lesson")  and request.user.has_perm("askmath.access_content"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson, exists=True)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_lessons(request,message)
            
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                try:
                    discipline = lesson.get_discipline()
                except:
                    message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                    return self.__proxy_home.index(request, message)
            
            try:
                return self.__contact.view_lesson(request,discipline, lesson)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, id_discipline, message)
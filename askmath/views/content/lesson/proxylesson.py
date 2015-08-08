from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

#MODELS
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel

from askmath.entities import Message, TextMessage, TypeMessage
from askmath.views.index import Home

from .ilesson import ILesson
from .lesson import Lesson

class ProxyLesson(ILesson):
    
    def __init__(self):
        self.__lesson = Lesson()
        self.__home = Home()
  
    def view_lessons(self, request, id_discipline, message = None):
        if request.user.has_perm("askmath.read_lesson"):
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.__home.index(request, message)
            try:
                return self.__lesson.view_lessons(request,discipline, message)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__home.index(request, message)
    
    def view_lesson(self, request,id_discipline, id_lesson, message=None):
        if request.user.has_perm("askmath.read_lesson"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_lessons(request,message)
            
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                try:
                    discipline = lesson.disciplines.filter(exists=True, visible=True)[0]
                except:
                    message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                    return self.__home.index(request, message)
            
            try:
                return self.__lesson.view_lesson(request,discipline, lesson)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, id_discipline, message)
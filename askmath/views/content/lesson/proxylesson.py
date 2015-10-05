from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#MODELS
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.views.index import ProxyHome
from askmath.views.content.discipline import ProxyDiscipline

from .ilesson import ILesson
from .lesson import Lesson

class ProxyLesson(ILesson):
    
    def __init__(self):
        self.__lesson = Lesson()
        self.__proxy_home = ProxyHome()
        self.__proxy_discipline = ProxyDiscipline()

    @method_decorator(login_required)
    def view_lesson(self, request,id_discipline=None, id_lesson=None):
        if request.user.has_perm("askmath.read_lesson")  and request.user.has_perm("askmath.access_content"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson, exists=True)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_lessons(request)
            
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except Exception, e:
                print e
                try:
                    discipline = lesson.get_discipline()
                except Exception, e:
                    print e
                    messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                    return self.__proxy_home.index(request)
            
            try:
                return self.__lesson.view_lesson(request,discipline, lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_discipline.view_discipline(request, id_discipline)
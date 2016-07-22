# -*- encoding=UTF-8 -*-

from askmath.entities import TextMessage
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from askmath.views.index import ProxyHome
from askmath.views.manager.discipline import ProxyDiscipline
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .ilesson import ILesson
from .lesson import Lesson


class ProxyLesson(ILesson):
    def __init__(self):
        self.__lesson = Lesson()
        self.__proxy_home = ProxyHome()
        self.__proxy_discipline = ProxyDiscipline()

    @method_decorator(login_required)
    def view_lessons(self, request, id_discipline):
        if request.user.has_perm("askmath.read_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                self.__proxy_discipline.view_disciplines(request)
            try:
                return self.__lesson.view_lessons(request, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_home.index(request)

    @method_decorator(login_required)
    def view_lessons_removed(self, request, id_discipline):
        if request.user.has_perm("askmath.read_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                self.__proxy_discipline.view_disciplines(request)

            try:
                return self.__lesson.view_lessons_removed(request, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_lessons(request, id_discipline)

    @method_decorator(login_required)
    def add_lesson(self, request, id_discipline):
        if request.user.has_perm("askmath.write_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                self.__proxy_discipline.view_disciplines(request)

            try:
                return self.__lesson.add_lesson(request, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_lessons(request, id_discipline)

    @method_decorator(login_required)
    def remove_lesson(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_lessons(request, id_discipline)

            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                self.__proxy_discipline.view_disciplines(request)
            try:
                return self.__lesson.remove_lesson(request, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_lessons(request, id_lesson)

    @method_decorator(login_required)
    def edit_lesson(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_lessons(request, id_discipline)

            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                self.__proxy_discipline.view_disciplines(request)

            try:
                return self.__lesson.edit_lesson(request, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_EDIT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_lessons(request, id_discipline)

    @method_decorator(login_required)
    def restore_lesson(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_lessons(request, id_discipline)

            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                self.__proxy_discipline.view_disciplines(request)

            try:
                return self.__lesson.restore_lesson(request, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_lessons(request, id_discipline)

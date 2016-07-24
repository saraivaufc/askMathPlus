# -*- encoding=UTF-8 -*-

from askmath.entities import TextMessage
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from .ilesson import ILesson
from .lesson import Lesson


class ProxyLesson(ILesson):
    def __init__(self):
        self.__lesson = Lesson()

    @method_decorator(login_required)
    def view_lessons(self, request, id_discipline):
        if request.user.has_perm("askmath.read_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
            try:
                return self.__lesson.view_lessons(request, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

    @method_decorator(login_required)
    def view_lessons_removed(self, request, id_discipline):
        if request.user.has_perm("askmath.read_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

            try:
                return self.__lesson.view_lessons_removed(request, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))

    @method_decorator(login_required)
    def add_lesson(self, request, id_discipline):
        if request.user.has_perm("askmath.write_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

            try:
                return self.__lesson.add_lesson(request, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))

    @method_decorator(login_required)
    def remove_lesson(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))
            try:
                return self.__lesson.remove_lesson(request, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))

    @method_decorator(login_required)
    def edit_lesson(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))
            try:
                return self.__lesson.edit_lesson(request, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_EDIT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))

    @method_decorator(login_required)
    def restore_lesson(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_lesson") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))
            try:
                return self.__lesson.restore_lesson(request, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))

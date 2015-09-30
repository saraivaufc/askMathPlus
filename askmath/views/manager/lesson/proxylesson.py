#-*- encoding=UTF-8 -*- 

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models.lesson import Lesson as ContactModel
from askmath.models.discipline import Discipline as CategoryModel
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.views.index import ProxyHome
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .ilesson import ILesson
from .lesson import Lesson

class ProxyLesson(ILesson):
    
    def __init__(self):
        self.__contact = Lesson()
        self.__proxy_home = ProxyHome()

    @method_decorator(login_required)
    def view_lessons(self, request):
        if request.user.has_perm("askmath.read_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__contact.view_lessons(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_home.index(request)
    
    @method_decorator(login_required)
    def view_lessons_removed(self,request):
        if request.user.has_perm("askmath.read_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__contact.view_lessons_removed(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_lessons(request)

    @method_decorator(login_required)    
    def view_lesson(self, request, id_lesson):
        if request.user.has_perm("askmath.read_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_lessons(request)
            try:
                return self.__contact.view_lesson(request, lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_lessons(request)
    
    @method_decorator(login_required)
    def add_lesson(self, request):
        if request.user.has_perm("askmath.write_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__contact.add_lesson(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_lessons(request)

    @method_decorator(login_required)
    def remove_lesson(self, request, id_lesson):
        if request.user.has_perm("askmath.write_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_lessons(request)
            try:
                return self.__contact.remove_lesson(request,lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_lessons(request)
    
    @method_decorator(login_required)
    def edit_lesson(self, request, id_lesson):
        if request.user.has_perm("askmath.write_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_lessons(request)
            try:
                return self.__contact.edit_lesson(request, lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_EDIT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_lessons(request)
    
    @method_decorator(login_required)
    def restore_lesson(self, request, id_lesson):
        if request.user.has_perm("askmath.write_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_lessons(request)
            try:
                return self.__contact.restore_lesson(request, lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_lessons(request)
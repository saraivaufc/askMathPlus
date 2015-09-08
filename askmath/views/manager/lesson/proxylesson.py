#-*- encoding=UTF-8 -*- 

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models.lesson import Lesson as ContactModel
from askmath.models.discipline import Discipline as CategoryModel
from askmath.entities import Message, TextMessage, TypeMessage
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
    def view_lessons(self, request, message = None):
        if request.user.has_perm("askmath.read_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__contact.view_lessons(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__proxy_home.index(request, message)
    
    @method_decorator(login_required)
    def view_lessons_removed(self,request, message = None):
        if request.user.has_perm("askmath.read_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__contact.view_lessons_removed(request,  message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, message)

    @method_decorator(login_required)    
    def view_lesson(self, request, id_lesson, message=None):
        if request.user.has_perm("askmath.read_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_lessons(request,message)
            try:
                return self.__contact.view_lesson(request, lesson)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request,message)
    
    @method_decorator(login_required)
    def add_lesson(self, request, message=None):
        if request.user.has_perm("askmath.write_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__contact.add_lesson(request)
            except:
                message = Message(TextMessage.LESSON_ERROR_ADD, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, message)

    @method_decorator(login_required)
    def remove_lesson(self, request, id_lesson, message=None):
        if request.user.has_perm("askmath.write_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_lessons(request,message)
            try:
                return self.__contact.remove_lesson(request,lesson)
            except:
                message = Message(TextMessage.LESSON_ERROR_REM, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, message)
    
    @method_decorator(login_required)
    def edit_lesson(self, request, id_lesson, message=None):
        if request.user.has_perm("askmath.write_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_lessons(request,message)
            try:
                return self.__contact.edit_lesson(request, lesson)
            except:
                message = Message(TextMessage.LESSON_ERROR_EDIT, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, message)
    
    @method_decorator(login_required)
    def restore_lesson(self, request, id_lesson, message=None):
        if request.user.has_perm("askmath.write_lesson")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_lessons(request,message)
            try:
                return self.__contact.restore_lesson(request, lesson)
            except:
                message = Message(TextMessage.LESSON_ERROR_RESTORE, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, message)
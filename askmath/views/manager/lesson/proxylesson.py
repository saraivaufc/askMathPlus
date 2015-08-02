#-*- encoding=UTF-8 -*- 

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models.lesson import Lesson as LessonModel
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.views.initial import Home

from .ilesson import ILesson
from .lesson import Lesson

class ProxyLesson(ILesson):
    
    def __init__(self):
        self.__lesson = Lesson()
        self.__home = Home()
  
    def view_lessons(self, request, message = None):
        if request.user.has_perm("askmath.read_lesson"):
            try:
                return self.__lesson.view_lessons(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__home.index(request, message)
    
    def view_lessons_removed(self,request, message = None):
        if request.user.has_perm("askmath.read_lesson"):
            try:
                return self.__lesson.view_lessons_removed(request,  message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, message)
    
    def view_lesson(self, request, id_lesson, message=None):
        if request.user.has_perm("askmath.read_lesson"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_lessons(request,message)
            try:
                return self.__lesson.view_lesson(request, lesson)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request,message)
    
    
    def add_lesson(self, request, message=None):
        if request.user.has_perm("askmath.write_lesson"):
            try:
                return self.__lesson.add_lesson(request)
            except:
                message = Message(TextMessage.LESSON_ERROR_ADD, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, message)
   
    def remove_lesson(self, request, id_lesson, message=None):
        if request.user.has_perm("askmath.write_lesson"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_lessons(request,message)
            try:
                return self.__lesson.remove_lesson(request,lesson)
            except:
                message = Message(TextMessage.LESSON_ERROR_REM, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, message)
    
    def edit_lesson(self, request, id_lesson, message=None):
        if request.user.has_perm("askmath.write_lesson"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_lessons(request,message)
            try:
                return self.__lesson.edit_lesson(request, lesson)
            except:
                message = Message(TextMessage.LESSON_ERROR_EDIT, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, message)
    
    def restore_lesson(self, request, id_lesson, message=None):
        if request.user.has_perm("askmath.write_lesson"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_lessons(request,message)
            try:
                return self.__lesson.restore_lesson(request, lesson)
            except:
                message = Message(TextMessage.LESSON_ERROR_RESTORE, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_lessons(request, message)
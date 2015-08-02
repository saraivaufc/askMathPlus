from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
import json

from askmath.entities import Message, TextMessage, TypeMessage
from askmath.models.lesson import Lesson as LessonModel
from askmath.models.question import Question as QuestionModel
from askmath.views.initial import Home

from .iquestion import IQuestion
from .question import Question


class ProxyQuestion(IQuestion):
    
    def __init__(self):
        self.__question = Question()
        self.__home = Home()
    
    def choose_lesson(self, request, message = None):
        if request.user.has_perm("askmath.read_question"):
            try:
                return self.__question.choose_lesson(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__home.index(request, message)
    
    def view_questions(self, request, id_lesson, message = None):
        if request.user.has_perm("askmath.read_question"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                if lesson:
                    return self.__question.view_questions(request,lesson,  message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.choose_lesson(request , message)
    
    def view_questions_removed(self, request, id_lesson,  message = None):
        if request.user.has_perm("askmath.read_question"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                if lesson:
                    return self.__question.view_questions_removed(request,lesson,  message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_questions(request, id_lesson, message)
    
    def view_question(self, request, id_lesson, id_question, message=None):
        if request.user.has_perm("askmath.read_question"):
            lesson, question = None, None
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                question = QuestionModel.objects.get(id = id_question)
            except:
                message = Message(TextMessage.QUESTION_NOT_FOUND, TypeMessage.ERROR)
                return self.view_questions(request, id_lesson, message)
            
            try:
                if lesson != None and question != None:
                    return self.__question.view_question(request, lesson, question)
                else:
                    message = Message(TextMessage.ERROR,TypeMessage.ERROR)
            except:
                message = Message(TextMessage.ERROR,TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION,TypeMessage.ERROR)
        return self.view_questions(request, id_lesson, message)
    
    def add_question(self, request, id_lesson, quantity_items, message=None):
        if request.user.has_perm("askmath.write_question"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                if quantity_items:
                    return self.__question.add_question(request, lesson, int(quantity_items))
                else:
                    message = Message(TextMessage.ERROR, TypeMessage.ERROR)         
            except:
                message = Message(TextMessage.QUESTION_ERROR_ADD, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION,TypeMessage.ERROR)
        return self.view_questions(request, id_lesson, message)
    
    def remove_question(self, request, id_lesson, id_question, message=None):
        if request.user.has_perm("askmath.write_question"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                question = QuestionModel.objects.get(id = id_question)
            except:
                message = Message(TextMessage.QUESTION_NOT_FOUND, TypeMessage.ERROR)
                return self.view_questions(request, id_lesson, message)
            try:
                return self.__question.remove_question(request, lesson,question)
            except:
                message = Message(TextMessage.QUESTION_ERROR_REM,TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION,TypeMessage.ERROR)
        return self.view_questions(request, id_lesson, message)
    def edit_question(self, request, id_lesson, id_question):
        if request.user.has_perm("askmath.write_question"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                question = QuestionModel.objects.get(id = id_question)
            except:
                message = Message(TextMessage.QUESTION_NOT_FOUND, TypeMessage.ERROR)
                return self.view_questions(request, id_lesson, message)
            try:
                return self.__question.edit_question(request, lesson, question)
            except:
                message = Message(TextMessage.QUESTION_ERROR_EDIT,TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION,TypeMessage.ERROR)
        return self.view_questions(request, id_lesson, message)

    
    def restore_question(self, request, id_lesson,id_question):
        if request.user.has_perm("askmath.write_question"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                question = QuestionModel.objects.get(id = id_question)
            except:
                message = Message(TextMessage.QUESTION_NOT_FOUND, TypeMessage.ERROR)
                return self.view_questions(request, id_lesson, message)
            try:
                return self.__question.restore_question(request, lesson,question)
            except:
                message = Message(TextMessage.QUESTION_ERROR_RESTORE,TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION,TypeMessage.ERROR)
        return self.view_questions(request, id_lesson, message)
            
    def sort_questions(self, request, id_lesson, message = None):
        if request.user.has_perm("askmath.read_question"):
            try:
                lesson = LessonModel.objects.get(id = id_lesson)
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.choose_lesson(request , message)
            try:
                if lesson:
                    if request.method == "POST":
                        new_order = json.loads(request.POST['new_order'])
                        return self.__question.sort_questions(request,lesson,new_order, message)
                    else:
                        return self.__question.sort_questions(request,lesson,None, message)
            except:
                message = Message(TextMessage.QUESTION_ERROR_SORT, TypeMessage.ERROR)
        return self.view_questions(request, id_lesson, message)
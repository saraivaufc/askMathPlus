from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
import json
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from askmath.entities import TextMessage
from django.contrib import messages
from askmath.models.lesson import Lesson as ContactModel
from askmath.models.question import Question as QuestionModel
from askmath.views.index import ProxyHome

from .iquestion import IQuestion
from .question import Question


class ProxyQuestion(IQuestion):
    
    def __init__(self):
        self.__question = Question()
        self.__proxy_home = ProxyHome()
    
    @method_decorator(login_required)
    def choose_lesson(self, request):
        if request.user.has_perm("askmath.read_question")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__question.choose_lesson(request)
            except Exception, e:
                print e
                messages.error(request,TextMessage.ERROR)
        else:
            messages.error(request,TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_home.index(request)
    
    @method_decorator(login_required)
    def view_questions(self, request, id_lesson):
        if request.user.has_perm("askmath.read_question")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request )
            try:
                if lesson:
                    return self.__question.view_questions(request,lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.ERROR)
        else:
            messages.error(request,TextMessage.USER_NOT_PERMISSION)
        return self.choose_lesson(request)
    
    @method_decorator(login_required)
    def view_questions_removed(self, request, id_lesson):
        if request.user.has_perm("askmath.read_question")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request)
            try:
                if lesson:
                    return self.__question.view_questions_removed(request,lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.ERROR)
        else:
            messages.error(request,TextMessage.USER_NOT_PERMISSION)
        return self.view_questions(request, id_lesson)
    
    @method_decorator(login_required)
    def view_question(self, request, id_lesson, id_question):
        if request.user.has_perm("askmath.read_question")  and request.user.has_perm("askmath.access_manager"):
            lesson, question = None, None
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request)
            try:
                question = QuestionModel.objects.get(id = id_question)
            except Exception, e:
                print e
                messages.error(request,TextMessage.QUESTION_NOT_FOUND)
                return self.view_questions(request, id_lesson)
            
            try:
                if lesson != None and question != None:
                    return self.__question.view_question(request, lesson, question)
                else:
                    messages.error(request,TextMessage.ERROR)
            except Exception, e:
                print e
                messages.error(request,TextMessage.ERROR)
        else:
            messages.error(request,TextMessage.USER_NOT_PERMISSION)
        return self.view_questions(request, id_lesson)
    
    @method_decorator(login_required)
    def add_question(self, request, id_lesson, quantity_items):
        if request.user.has_perm("askmath.write_question")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request)
            try:
                if quantity_items:
                    return self.__question.add_question(request, lesson, int(quantity_items))
                else:
                    messages.error(request,TextMessage.ERROR)         
            except Exception, e:
                print e
                messages.error(request,TextMessage.QUESTION_ERROR_ADD)
        else:
            messages.error(request,TextMessage.USER_NOT_PERMISSION)
        return self.view_questions(request, id_lesson)
    
    @method_decorator(login_required)
    def remove_question(self, request, id_lesson, id_question):
        if request.user.has_perm("askmath.write_question")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request)
            try:
                question = QuestionModel.objects.get(id = id_question)
            except Exception, e:
                print e
                messages.error(request,TextMessage.QUESTION_NOT_FOUND)
                return self.view_questions(request, id_lesson)
            try:
                return self.__question.remove_question(request, lesson,question)
            except Exception, e:
                print e
                messages.error(request,TextMessage.QUESTION_ERROR_REM)
        else:
            messages.error(request,TextMessage.USER_NOT_PERMISSION)
        return self.view_questions(request, id_lesson)

    @method_decorator(login_required)
    def edit_question(self, request, id_lesson, id_question):
        if request.user.has_perm("askmath.write_question")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request )
            try:
                question = QuestionModel.objects.get(id = id_question)
            except Exception, e:
                print e
                messages.error(request,TextMessage.QUESTION_NOT_FOUND)
                return self.view_questions(request, id_lesson)
            try:
                return self.__question.edit_question(request, lesson, question)
            except Exception, e:
                print e
                messages.error(request,TextMessage.QUESTION_ERROR_EDIT)
        else:
            messages.error(request,TextMessage.USER_NOT_PERMISSION)
        return self.view_questions(request, id_lesson)

    @method_decorator(login_required)
    def restore_question(self, request, id_lesson,id_question):
        if request.user.has_perm("askmath.write_question")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request )
            try:
                question = QuestionModel.objects.get(id = id_question)
            except Exception, e:
                print e
                messages.error(request,TextMessage.QUESTION_NOT_FOUND)
                return self.view_questions(request, id_lesson)
            try:
                return self.__question.restore_question(request, lesson,question)
            except Exception, e:
                print e
                messages.error(request,TextMessage.QUESTION_ERROR_RESTORE)
        else:
            messages.error(request,TextMessage.USER_NOT_PERMISSION)
        return self.view_questions(request, id_lesson)
    
    @method_decorator(login_required)
    def sort_questions(self, request, id_lesson):
        if request.user.has_perm("askmath.read_question")  and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = ContactModel.objects.get(id = id_lesson)
            except Exception, e:
                print e
                messages.error(request,TextMessage.LESSON_NOT_FOUND)
                return self.choose_lesson(request)
            try:
                if lesson:
                    if request.method == "POST":
                        new_order = json.loads(request.POST['new_order'])
                        return self.__question.sort_questions(request,lesson,new_order)
                    else:
                        return self.__question.sort_questions(request,lesson,None)
            except Exception, e:
                print e
                messages.error(request,TextMessage.QUESTION_ERROR_SORT)
        return self.view_questions(request, id_lesson)
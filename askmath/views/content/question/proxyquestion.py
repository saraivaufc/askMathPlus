from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from askmath.entities import TextMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#MODELS
from askmath.models.discipline import Discipline as CategoryModel
from askmath.models.lesson import Lesson as ContactModel
from askmath.models.question import Question as QuestionModel
from askmath.models.question import Item as ItemModel

from askmath.views.index import ProxyHome

from .iquestion import IQuestion
from .question import Question


class ProxyQuestion(IQuestion):
    
    def __init__(self):
        self.__question = Question()
        self.__proxy_home = ProxyHome()
    
    @method_decorator(login_required)
    def view_question(self, request, id_discipline, id_lesson):
        if request.user.has_perm("askmath.read_question")  and request.user.has_perm("askmath.access_content"):
            try:
                discipline = CategoryModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.__proxy_home.index(request)
            try:
                lesson = ContactModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_initial_details(request, id_discipline, id_lesson)
            try:
                return self.__question.view_question(request, discipline, lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_home.index(request)
    
    @method_decorator(login_required)
    def answer_question(self, request, id_discipline, id_lesson, id_question):
        if request.user.has_perm("askmath.read_question")  and request.user.has_perm("askmath.access_content"):
            try:
                discipline = CategoryModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_question(request, id_discipline, id_lesson)
            try:
                lesson = ContactModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_question(request, id_discipline, id_lesson)
            try:
                question = QuestionModel.objects.filter(id = id_question, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return self.view_question(request, id_discipline, id_lesson)
            if not request.method == 'POST':
                return self.view_question(request, id_discipline, id_lesson)
            try:
                item = ItemModel.objects.get(id=int(request.POST['item']))
            except Exception, e:
                print e
                messages.error(request, TextMessage.ITEM_NOT_FOUND)
                return self.view_question(request, id_discipline, id_lesson)
            try:
                return self.__question.answer_question(request, discipline, lesson, question, item)
            except Exception, e:
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_question(request, id_discipline, id_lesson)
    
    @method_decorator(login_required)
    def jump_question(self, request, id_discipline, id_lesson, id_question):
        if request.user.has_perm("askmath.read_question")  and request.user.has_perm("askmath.access_content"):
            try:
                discipline = CategoryModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_question(request, id_discipline, id_lesson)
            try:
                lesson = ContactModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_question(request, id_discipline, id_lesson)
            try:
                question = QuestionModel.objects.get(id = id_question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return self.view_question(request, id_discipline, id_lesson)
            try:
                return self.__question.jump_question(request, discipline, lesson, question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_question(request, id_discipline, id_lesson)

    @method_decorator(login_required)
    def choose_skipped_question(self, request, id_discipline, id_lesson, id_question):
        if request.user.has_perm("askmath.read_question")  and request.user.has_perm("askmath.access_content"):
            try:
                discipline = CategoryModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_question(request, id_discipline, id_lesson)
            try:
                lesson = ContactModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_question(request, id_discipline, id_lesson)
            try:
                question = QuestionModel.objects.filter(id = id_question, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return self.view_question(request, id_discipline, id_lesson)
            try:
                return self.__question.choose_skipped_question(request, discipline, lesson, question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_question(request, id_discipline, id_lesson)
    
    @method_decorator(login_required)
    def reset_lesson(self,request, id_discipline, id_lesson):
        if request.user.has_perm("askmath.read_question")  and request.user.has_perm("askmath.access_content"):
            try:
                discipline = CategoryModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.__proxy_home.index(request)
            try:
                lesson = ContactModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.__proxy_home.index(request)
            try:
                return self.__question.reset_lesson(request, discipline, lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_initial_details(request, id_discipline, id_lesson)
    
    @method_decorator(login_required)
    def help_question(self,request, id_discipline, id_lesson,id_question):
        if request.user.has_perm("askmath.read_question")  and request.user.has_perm("askmath.access_content"):
            try:
                discipline = CategoryModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.__proxy_home.index(request)
            try:
                lesson = ContactModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.__proxy_home.index(request)
            try:
                question = QuestionModel.objects.filter(id = id_question, exists=True,visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return self.view_question(request, id_discipline, id_lesson)
            
            try:
                return self.__question.help_quetion(request, discipline, lesson, question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_initial_details(request, id_discipline, id_lesson)
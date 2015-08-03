from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from askmath.entities import Message, TextMessage, TypeMessage

#MODELS
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from askmath.models.question import Question as QuestionModel
from askmath.models.question import Item as ItemModel

from askmath.views.initial import Home

from .iquestion import IQuestion
from .question import Question


class ProxyQuestion(IQuestion):
    
    def __init__(self):
        self.__question = Question()
        self.__home = Home()
    
    def view_initial_details(self, request, id_discipline, id_lesson):
        if request.user.has_perm("askmath.read_question"):
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.__home.index(request, message)
            try:
                lesson = LessonModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.__home.index(request, message)
            #try:
            return self.__question.view_initial_details(request, discipline, lesson)
            #except:
                #message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__home.index(request, message)
        
    def view_question(self, request, id_discipline, id_lesson,message=None):
        if request.user.has_perm("askmath.read_question"):
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.__home.index(request, message)
            try:
                lesson = LessonModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_initial_details(request, id_discipline, id_lesson)
            #try:
            return self.__question.view_question(request, discipline, lesson, message)
            #except:
                #message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__home.index(request, message)
    
    def answer_question(self, request, id_discipline, id_lesson, id_question, message=None):
        if request.user.has_perm("askmath.read_question"):
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.view_question(request, id_discipline, id_lesson, message)
            try:
                lesson = LessonModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_question(request, id_discipline, id_lesson, message)
            try:
                question = QuestionModel.objects.filter(id = id_question, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.QUESTION_NOT_FOUND, TypeMessage.ERROR)
                return self.view_question(request, id_discipline, id_lesson, message)
            if not request.method == 'POST':
                return self.view_question(request, id_discipline, id_lesson, message)
            #try:
            items = []
            for i in request.POST.getlist('item'):
                item = ItemModel.objects.get(id = i)
                print item
                if item:
                    items.append(item)
            #except :
                #message = Message(TextMessage.ITEM_NOT_FOUND, TypeMessage.ERROR)
                #return self.view_question(request, id_discipline, id_lesson, message)
            #try:
            return self.__question.answer_question(request, discipline, lesson, question, items)
            #except:
                #message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_question(request, id_discipline, id_lesson, message)
    
    def jump_question(self, request, id_discipline, id_lesson, id_question, message=None):
        if request.user.has_perm("askmath.read_question"):
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.view_question(request, id_discipline, id_lesson, message)
            try:
                lesson = LessonModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_question(request, id_discipline, id_lesson, message)
            try:
                question = QuestionModel.objects.get(id = id_question)
            except:
                message = Message(TextMessage.QUESTION_NOT_FOUND, TypeMessage.ERROR)
                return self.view_question(request, id_discipline, id_lesson, message)
            #try:
            return self.__question.jump_question(request, discipline, lesson, question)
            #except:
                #message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_question(request, id_discipline, id_lesson, message)

    def choose_skipped_question(self, request, id_discipline, id_lesson, id_question, message=None):
        if request.user.has_perm("askmath.read_question"):
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.view_question(request, id_discipline, id_lesson, message)
            try:
                lesson = LessonModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.view_question(request, id_discipline, id_lesson, message)
            try:
                question = QuestionModel.objects.filter(id = id_question, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.QUESTION_NOT_FOUND, TypeMessage.ERROR)
                return self.view_question(request, id_discipline, id_lesson, message)
            #try:
            return self.__question.choose_skipped_question(request, discipline, lesson, question)
            #except:
                #message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_question(request, id_discipline, id_lesson, message)
    
    def reset_lesson(self,request, id_discipline, id_lesson, message=None):
        if request.user.has_perm("askmath.read_question"):
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.__home.index(request, message)
            try:
                lesson = LessonModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.__home.index(request, message)
            #try:
            return self.__question.reset_lesson(request, discipline, lesson)
            #except:
                #message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_initial_details(request, id_discipline, id_lesson)
    
    def help_question(self,request, id_discipline, id_lesson,id_question, message=None):
        if request.user.has_perm("askmath.read_question"):
            try:
                discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.__home.index(request, message)
            try:
                lesson = LessonModel.objects.filter(id = id_lesson, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.LESSON_NOT_FOUND, TypeMessage.ERROR)
                return self.__home.index(request, message)
            try:
                question = QuestionModel.objects.filter(id = id_question, exists=True,visible=True)[0]
            except:
                message = Message(TextMessage.QUESTION_NOT_FOUND, TypeMessage.ERROR)
                return self.view_question(request, id_discipline, id_lesson, message)
            
            #try:
            return self.__question.help_quetion(request, discipline, lesson, question)
            #except:
                #message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_initial_details(request, id_discipline, id_lesson)
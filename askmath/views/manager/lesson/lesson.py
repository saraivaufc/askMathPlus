#-*- encoding=UTF-8 -*- 

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Lesson as ContactModel
from askmath.models import Discipline as DisciplineModel
from askmath.entities import Message, TextMessage, TypeMessage
from .ilesson import ILesson
from askMathPlus.settings import COLORS_ALL
from askmath.forms import LessonForm
from django.utils.translation import ugettext_lazy as _

class Lesson(ILesson):
    
    def view_lessons(self, request, message = None):
        disciplines = []
        for d in DisciplineModel.objects.filter(exists=True):
            if not d.get_lessons():
                continue
            dict = {}
            dict['title'] = d.get_title
            dict['lessons'] = d.get_lessons()
            disciplines.append(dict)
            
        return render(request, "askmath/manager/lesson/manager_view_lessons.html",
            {'request':request,'disciplines': disciplines,'colors': COLORS_ALL, 'message': message})
    
    def view_lessons_removed(self, request, message = None):
        disciplines = []
        for d in DisciplineModel.objects.filter(exists=True):
            if not d.get_lessons_removed():
                continue
            dict = {}
            dict['title'] = d.get_title
            dict['lessons'] = d.get_lessons_removed()
            disciplines.append(dict)
            
        return render(request, "askmath/manager/lesson/manager_view_lessons.html",
            {'request':request,'disciplines': disciplines,'is_removed': True,'colors': COLORS_ALL, 'message': message})
        
    def view_lesson(self, request,lesson,message = None):
        return render(request, "askmath/manager/lesson/manager_view_lesson.html", 
            {'request':request,'lesson': lesson ,'message': message, 'colors': COLORS_ALL })
    
    
    
    def add_lesson(self, request, message = None):
        if request.method == "POST":
            form = LessonForm(request.POST)
            if form.is_valid():
                lesson = form.save()
                message = Message(TextMessage.LESSON_SUCCESS_ADD, TypeMessage.SUCCESS)
                return self.view_lesson(request, lesson, message)
        else:
            form = LessonForm()
        return render(request, "askmath/manager/lesson/manager_form_lesson.html", 
            {'request':request,'form': form,'title_form':_('Create Lesson'), 'message': message})
    
    def remove_lesson(self, request,lesson, message = None):
        lesson.delete()
        message = Message(TextMessage.LESSON_SUCCESS_REM, TypeMessage.SUCCESS)
        return self.view_lessons(request, message)
    def edit_lesson(self, request, lesson, message = None):
        if request.method == 'POST':
            form = LessonForm(request.POST, instance = lesson)
            if form.is_valid():
                lesson = form.save()
                message = Message(TextMessage.LESSON_SUCCESS_EDIT, TypeMessage.SUCCESS)
                return self.view_lesson(request , lesson, message)
        else:
            form = LessonForm( instance = lesson)
        return render(request, "askmath/manager/lesson/manager_form_lesson.html", 
            {'request':request,'form': form,'title_form':_('Edit Lesson'), 'message': message})
    
    def restore_lesson(self, request,  lesson):
        lesson.restore()
        message = Message(TextMessage.LESSON_SUCCESS_RESTORE, TypeMessage.SUCCESS)
        return self.view_lessons(request, message)
#-*- encoding=UTF-8 -*- 

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Lesson as ContactModel
from askmath.models import Discipline as DisciplineModel
from askmath.entities import TextMessage
from django.contrib import messages
from .ilesson import ILesson
from askmath.forms import LessonForm
from django.utils.translation import ugettext_lazy as _

class Lesson(ILesson):
    
    def view_lessons(self, request):
        disciplines = DisciplineModel.objects.filter(exists=True)
        return render(request, "askmath/manager/lesson/manager_view_lessons.html",
            {'request':request,'disciplines': disciplines})
    
    def view_lessons_removed(self, request):
        disciplines = []
        for d in DisciplineModel.objects.filter(exists=True):
            if not d.get_lessons_removed():
                continue
            dict = {}
            dict['title'] = d.get_title
            dict['lessons'] = d.get_lessons_removed()
            disciplines.append(dict)
            
        return render(request, "askmath/manager/lesson/manager_view_lessons.html",
            {'request':request,'disciplines': disciplines,'is_removed': True})
        
    def view_lesson(self, request,lesson,message = None):
        return render(request, "askmath/manager/lesson/manager_view_lesson.html", 
            {'request':request,'lesson': lesson })
    
    
    
    def add_lesson(self, request):
        if request.method == "POST":
            form = LessonForm(request.POST)
            if form.is_valid():
                lesson = form.save()
                messages.success(request,TextMessage.LESSON_SUCCESS_ADD)
                return self.view_lesson(request, lesson)
            else:
                messages.error(request,TextMessage.LESSON_ERROR_ADD)
        else:
            form = LessonForm()
        return render(request, "askmath/manager/lesson/manager_form_lesson.html", 
            {'request':request,'form': form,'title_form':_('Create Lesson')})
    
    def remove_lesson(self, request,lesson):
        lesson.delete()
        messages.error(request,TextMessage.LESSON_SUCCESS_REM)
        return self.view_lessons(request)
    def edit_lesson(self, request, lesson):
        if request.method == 'POST':
            form = LessonForm(request.POST, instance = lesson)
            if form.is_valid():
                lesson = form.save()
                messages.error(request,TextMessage.LESSON_SUCCESS_EDIT)
                return self.view_lesson(request , lesson)
            else:
                messages.error(request,TextMessage.LESSON_ERROR_EDIT)
        else:
            form = LessonForm( instance = lesson)
        return render(request, "askmath/manager/lesson/manager_form_lesson.html", 
            {'request':request,'form': form,'lesson':lesson,'title_form':_('Edit Lesson')})
    
    def restore_lesson(self, request,  lesson):
        lesson.restore()
        messages.error(request,TextMessage.LESSON_SUCCESS_RESTORE)
        return self.view_lessons(request)
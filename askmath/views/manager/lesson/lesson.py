#-*- encoding=UTF-8 -*- 

from askmath.entities import TextMessage
from askmath.forms import LessonForm
from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from .ilesson import ILesson


class Lesson(ILesson):
    
    def view_lessons(self, request, discipline):
        lessons = discipline.get_lessons()
        return render(request, "askmath/manager/lesson/manager_view_lessons.html",
            {'request':request,'discipline': discipline,'lessons': lessons})
    
    def view_lessons_removed(self, request, discipline):
        lessons = discipline.get_lessons_removed()
        return render(request, "askmath/manager/lesson/manager_view_lessons.html",
            {'request':request,'discipline': discipline,'lessons': lessons,'is_removed': True})
    
    def add_lesson(self, request, discipline):
        if request.method == "POST":
            request.POST['discipline'] = discipline.id
            form = LessonForm(request.POST)
            if form.is_valid():
                lesson = form.save()
                messages.success(request,TextMessage.LESSON_SUCCESS_ADD)
                return self.view_lessons(request, discipline)
            else:
                messages.error(request,TextMessage.LESSON_ERROR_ADD)
        else:
            form = LessonForm()
        return render(request, "askmath/manager/lesson/manager_form_lesson.html", 
            {'request':request,'discipline': discipline,'form': form,'title_form':_('Create Lesson')})
    
    def remove_lesson(self, request,lesson, discipline):
        lesson.delete()
        messages.success(request,TextMessage.LESSON_SUCCESS_REM)
        return self.view_lessons(request, discipline)
    def edit_lesson(self, request, lesson, discipline):
        if request.method == 'POST':
            request.POST['discipline'] = discipline.id
            form = LessonForm(request.POST, instance = lesson)
            if form.is_valid():
                lesson = form.save()
                messages.success(request,TextMessage.LESSON_SUCCESS_EDIT)
                return self.view_lessons(request , discipline)
            else:
                messages.error(request,TextMessage.LESSON_ERROR_EDIT)
        else:
            form = LessonForm( instance = lesson)
        return render(request, "askmath/manager/lesson/manager_form_lesson.html", 
            {'request':request,'form': form,'discipline': discipline, 'lesson':lesson,'title_form':_('Edit Lesson')})
    
    def restore_lesson(self, request,  lesson, discipline):
        lesson.restore()
        messages.success(request,TextMessage.LESSON_SUCCESS_RESTORE)
        return self.view_lessons(request, discipline)
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Lesson as ContactModel
from askmath.models import Discipline as CategoryModel
from askmath.entities import Message, TextMessage, TypeMessage
from .ilesson import ILesson
from askmath.forms import LessonForm
from django.utils.translation import ugettext_lazy as _

class Lesson(ILesson):
    
    def view_lessons(self, request, discipline, message = None):
        lessons = discipline.get_lessons_visible()
        print discipline,'---', lessons
        return render(request, "askmath/content/lesson/content_view_lessons.html",
            {'request':request,'discipline': discipline, 'lessons': lessons, 'message': message})
    
    def view_lesson(self, request,discipline, lesson,message = None):
        return render(request, "askmath/content/lesson/content_view_lesson.html", 
            {'request':request, 'discipline': discipline,'lesson': lesson,'message': message})
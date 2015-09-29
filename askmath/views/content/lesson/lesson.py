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
    	disciplines = DisciplineModel.objects.filter(exists=True, visible=True)
     	return render(request, "askmath/content/lesson/content_view_lessons.html",
            {'request':request,'disciplines': disciplines})
    
    def view_lesson(self, request, discipline, lesson):
        return render(request, "askmath/content/lesson/content_view_lesson.html", 
            {'request':request, 'discipline': discipline,'lesson': lesson})
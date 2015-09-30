#-*- encoding=UTF-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from askmath.models import Discipline as CategoryModel
from askmath.models import Lesson as ContactModel

from ..istatistic import IStatistic
from .ilesson import ILesson
from .generatestatistics import GeneratorStatistics

class Lesson(IStatistic, ILesson):
        
    def choose_lesson(self, request):
        disciplines = []
        for discipline in CategoryModel.objects.filter(exists=True):
            if discipline.get_lessons():
                disciplines.append(discipline)
        return render(request, "askmath/manager/statistic/lessons/manager_choose_lesson.html",
            {'request': request,'disciplines': disciplines})
    
    def view_statistics(self, request,lesson):
        generator = GeneratorStatistics()
        percentage_answered_questions = generator.get_percentage_answered_questions(lesson)
        return render(request, "askmath/manager/statistic/lessons/manager_view_statistics.html",
            {'request': request,'lesson': lesson ,'percentage_answered_questions': percentage_answered_questions})
#-*- encoding=UTF-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from askMathPlus.settings import COLORS_ALL
from askmath.entities import Message, TextMessage, TypeMessage

from askmath.models import Discipline as DisciplineModel
from askmath.models import Lesson as ContactModel

from ..istatistic import IStatistic
from .ilesson import ILesson
from .generatestatistics import GeneratorStatistics

class Lesson(IStatistic, ILesson):
        
    def choose_lesson(self, request,statistic, message=None):
        disciplines = []
        for discipline in DisciplineModel.objects.filter(exists=True):
            if discipline.get_lessons():
                disciplines.append(discipline)
        return render(request, "askmath/manager/statistic/lessons/manager_choose_lesson.html",
            {'request': request,'disciplines': disciplines,'statistic': statistic, 'colors': COLORS_ALL})
    
    def view_statistics(self, request,lesson, message=None):
        generator = GeneratorStatistics()
        percentage_answered_questions = generator.get_percentage_answered_questions(lesson)
        return render(request, "askmath/manager/statistic/lessons/manager_view_statistics.html",
            {'request': request,'lesson': lesson ,'percentage_answered_questions': percentage_answered_questions,'colors': COLORS_ALL, 'message': message})
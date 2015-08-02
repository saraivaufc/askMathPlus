#-*- encoding=UTF-8 -*-


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from askMathPlus.settings import COLORS_ALL
from askmath.entities import Message, TextMessage, TypeMessage

from .istatistic import IStatistic

class Statistic(IStatistic):
    def choose_type(self, request, message=None):
        return render(request, "askmath/manager/statistic/manager_choose_types.html",
            {'request': request, 'colors': COLORS_ALL, 'message': message})
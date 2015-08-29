#-*- encoding=UTF-8 -*-


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from askmath.entities import Message, TextMessage, TypeMessage

from .istatistic import IStatistic

class Statistic(IStatistic):
    def choose_type(self, request, message=None):
        return render(request, "askmath/manager/statistic/manager_choose_types.html",
            {'request': request, 'message': message})
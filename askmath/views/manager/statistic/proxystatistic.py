#-*- encoding=UTF-8 -*-


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from askmath.entities import Message, TextMessage, TypeMessage

from .istatistic import IStatistic
from .statistic import Statistic
from askmath.views.index import Home

class ProxyStatistic(IStatistic):
    def __init__(self):
        self.__home = Home()
        self.__statistic = Statistic()
    
    def choose_type(self, request, message=None):
        if request.user.has_perm("askmath.read_statistics"):
            try:
                return self.__statistic.choose_type(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__home.index(request, message)
    
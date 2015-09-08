#-*- encoding=UTF-8 -*-


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from askmath.entities import Message, TextMessage, TypeMessage

from .istatistic import IStatistic
from .statistic import Statistic
from askmath.views.index import ProxyHome

class ProxyStatistic(IStatistic):
    def __init__(self):
        self.__proxy_home = ProxyHome()
        self.__statistic = Statistic()
    
    @method_decorator(login_required)
    def choose_type(self, request, message=None):
        if request.user.has_perm("askmath.read_statistics")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__statistic.choose_type(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__proxy_home.index(request, message)
    
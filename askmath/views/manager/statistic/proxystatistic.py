#-*- encoding=UTF-8 -*-


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from askmath.entities import TextMessage
from django.contrib import messages

from .istatistic import IStatistic
from .statistic import Statistic
from askmath.views.index import ProxyHome

class ProxyStatistic(IStatistic):
    def __init__(self):
        self.__proxy_home = ProxyHome()
        self.__statistic = Statistic()
    
    @method_decorator(login_required)
    def choose_type(self, request):
        if request.user.has_perm("askmath.read_statistics")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__statistic.choose_type(request)
            except Exception, e:
                print e
                messages.error(request,TextMessage.ERROR)
        else:
            messages.error(request,TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_home.index(request)
    
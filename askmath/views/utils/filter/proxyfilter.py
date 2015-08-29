from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from .ifilter import IFilter
from .filter import Filter
from askmath.views.index import ProxyHome

class ProxyFilter(IFilter):
    def __init__(self):
        self.__filter = Filter()
        self.__proxy_home = ProxyHome()
    
    def search(self, request, message=None):
        if request.method == "POST":
            try:
                expression = request.POST['search']
                if len(expression) <= 27:
                   return self.__filter.search(request, expression ,message)
                else:
                    message = Message(TextMessage.SEARCH_ERROR_SIZE, TypeMessage.ERROR)
            except:
                message = Message(TextMessage.ERROR_FORM, TypeMessage.WARNING)
        return self.__proxy_home.index(request, message)
            
            
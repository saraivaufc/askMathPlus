from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import TextMessage
from django.contrib import messages
from .ifilter import IFilter
from .filter import Filter
from askmath.views.index import ProxyHome

class ProxyFilter(IFilter):
    def __init__(self):
        self.__filter = Filter()
        self.__proxy_home = ProxyHome()
    
    def search(self, request):
        if request.method == "POST":
            try:
                expression = request.POST['search']
                if len(expression) <= 50:
                   return self.__filter.search(request, expression)
                else:
                    messages.error(request, TextMessage.SEARCH_ERROR_SIZE)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR_FORM)
        return self.__proxy_home.index(request)
            
            
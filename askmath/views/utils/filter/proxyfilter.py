from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage
from .ifilter import IFilter
from .filter import Filter
from askmath.views.index import Home

class ProxyFilter(IFilter):
    def __init__(self):
        self.__filter = Filter()
        self.__home = Home()
    
    def search(self, request, message=None):
        if request.method == "POST":
            #try:
            expression = request.POST['search']    
            return self.__filter.search(request, expression ,message)
            #except:
                #message = Message(TextMessage.ERROR_FORM, TypeMessage.WARNING)
        return self.__home.index(request, message)
            
            
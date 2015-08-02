from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.views.initial import Home

from .idiscipline import IDiscipline
from .discipline import Discipline

class ProxyDiscipline(IDiscipline):
    
    def __init__(self):
        self.__discipline = Discipline()
        self.__home = Home()
        
    def view_disciplines(self, request, message = None):
        if request.user.has_perm("askmath.read_discipline"):
            try:
                return self.__discipline.view_disciplines(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__home.index(request, message)
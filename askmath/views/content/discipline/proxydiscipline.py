from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models.discipline import Discipline as CategoryModel
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.views.index import ProxyHome
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .idiscipline import IDiscipline
from .discipline import Discipline

class ProxyDiscipline(IDiscipline):
    
    def __init__(self):
        self.__discipline = Discipline()
        self.__proxy_home = ProxyHome()
    
    @method_decorator(login_required)
    def view_disciplines(self, request, message = None):
        if request.user.has_perm("askmath.read_discipline") and request.user.has_perm("askmath.access_content"):
            try:
                return self.__discipline.view_disciplines(request, message)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.__proxy_home.index(request, message)
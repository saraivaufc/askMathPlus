from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.entities import Message, TextMessage, TypeMessage
from askmath.views.index import Home

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
            return self.__home.index(request, message)
    
    def view_disciplines_removed(self, request, message=None):
        if request.user.has_perm("askmath.read_discipline"):
            try:
                return self.__discipline.view_disciplines_removed(request)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_disciplines(request, message)
    
    def view_discipline(self, request, id_discipline, message=None):
        if request.user.has_perm("askmath.read_discipline"):
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline)
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.view_disciplines(request,message)
            try:
                return self.__discipline.view_discipline(request, discipline)
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_disciplines(request,message)
    
    
    def add_discipline(self, request, message=None):
        if request.user.has_perm("askmath.write_discipline"):
            try:
                return self.__discipline.add_discipline(request)
            except:
                message = Message(TextMessage.DISCIPLINE_ERROR_ADD, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_disciplines(request,message)
    
    def remove_discipline(self, request, id_discipline, message=None):
        if request.user.has_perm("askmath.write_discipline"):
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline)
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.view_disciplines(request,message)
            try:
                return self.__discipline.remove_discipline(request, discipline)
            except:
                message = Message(TextMessage.DISCIPLINE_ERROR_REM, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_disciplines(request,message)
    
    def edit_discipline(self, request, id_discipline, message=None):
        if request.user.has_perm("askmath.write_discipline"):
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline)
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.view_disciplines(request,message)
            try:
                return self.__discipline.edit_discipline(request, discipline)
            except:
                message = Message(TextMessage.DISCIPLINE_ERROR_EDIT, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_disciplines(request,message)
    
    def restore_discipline(self, request, id_discipline, message=None):
        if request.user.has_perm("askmath.write_discipline"):
            try:
                discipline = DisciplineModel.objects.get(id = id_discipline)
            except:
                message = Message(TextMessage.DISCIPLINE_NOT_FOUND, TypeMessage.ERROR)
                return self.view_disciplines(request,message)
            try:
                return self.__discipline.restore_discipline(request, discipline)
            except:
                message = Message(TextMessage.DISCIPLINE_ERROR_RESTORE, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.USER_NOT_PERMISSION, TypeMessage.ERROR)
        return self.view_disciplines(request,message)
    
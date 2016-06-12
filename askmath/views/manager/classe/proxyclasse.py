from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models.classe import Classe as ClasseModel
from askmath.entities import TextMessage
from django.contrib import messages
from askmath.views.index import ProxyHome
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .iclasse import IClasse
from .classe import Classe

class ProxyClasse(IClasse):
    
    def __init__(self):
        self.__classe = Classe()
        self.__proxy_home = ProxyHome()
        
    @method_decorator(login_required)
    def view_classes(self, request):
        if request.user.has_perm("askmath.read_classe")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__classe.view_classes(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_home.index(request)
    
    @method_decorator(login_required)
    def view_classes_removed(self, request):
        if request.user.has_perm("askmath.read_classe")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__classe.view_classes_removed(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_classes(request)
    
    @method_decorator(login_required)
    def add_classe(self, request):
        if request.user.has_perm("askmath.write_classe")  and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__classe.add_classe(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_classes(request)
    
    @method_decorator(login_required)
    def remove_classe(self, request, id_classe):
        if request.user.has_perm("askmath.write_classe")  and request.user.has_perm("askmath.access_manager"):
            try:
                classe = ClasseModel.objects.get(id = id_classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_classes(request)
            try:
                return self.__classe.remove_classe(request, classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_classes(request)
    
    @method_decorator(login_required)
    def edit_classe(self, request, id_classe):
        if request.user.has_perm("askmath.write_classe")  and request.user.has_perm("askmath.access_manager"):
            try:
                classe = ClasseModel.objects.get(id = id_classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_classes(request)
            try:
                return self.__classe.edit_classe(request, classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_ERROR_EDIT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_classes(request)
    
    @method_decorator(login_required)
    def restore_classe(self, request, id_classe):
        if request.user.has_perm("askmath.write_classe")  and request.user.has_perm("askmath.access_manager"):
            try:
                classe = ClasseModel.objects.get(id = id_classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_classes(request)
            try:
                return self.__classe.restore_classe(request, classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_classes(request)
    
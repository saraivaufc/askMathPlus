from askmath.entities import TextMessage
from askmath.models.classe import Classe as ClasseModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from .classe import Classe
from .iclasse import IClasse


class ProxyClasse(IClasse):
    def __init__(self):
        self.__classe = Classe()

    @method_decorator(login_required)
    def view_classes(self, request):
        if request.user.has_perm("askmath.read_classe") and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__classe.view_classes(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return HttpResponseRedirect(reverse('askmath:home'))

    @method_decorator(login_required)
    def view_classes_removed(self, request):
        if request.user.has_perm("askmath.read_classe") and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__classe.view_classes_removed(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_classe_view'))

    @method_decorator(login_required)
    def add_classe(self, request):
        if request.user.has_perm("askmath.write_classe") and request.user.has_perm("askmath.access_manager"):
            try:
                return self.__classe.add_classe(request)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_classe_view'))

    @method_decorator(login_required)
    def remove_classe(self, request, id_classe):
        if request.user.has_perm("askmath.write_classe") and request.user.has_perm("askmath.access_manager"):
            try:
                classe = ClasseModel.objects.get(id=id_classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_classe_view'))
            try:
                return self.__classe.remove_classe(request, classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_classe_view'))

    @method_decorator(login_required)
    def edit_classe(self, request, id_classe):
        if request.user.has_perm("askmath.write_classe") and request.user.has_perm("askmath.access_manager"):
            try:
                classe = ClasseModel.objects.get(id=id_classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_classe_view'))
            try:
                return self.__classe.edit_classe(request, classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_ERROR_EDIT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_classe_view'))

    @method_decorator(login_required)
    def restore_classe(self, request, id_classe):
        if request.user.has_perm("askmath.write_classe") and request.user.has_perm("askmath.access_manager"):
            try:
                classe = ClasseModel.objects.get(id=id_classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_classe_view'))
            try:
                return self.__classe.restore_classe(request, classe)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_classe_view'))

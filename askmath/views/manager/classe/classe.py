from askmath.entities import TextMessage
from askmath.forms import ClasseForm
from askmath.models import Classe as ClasseModel
from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from iclasse import IClasse


class Classe(IClasse):
    def view_classes(self, request):
        classes = ClasseModel.objects.filter(exists=True)
        return render(request, "askmath/manager/classe/manager_view_classes.html",
                      {'request': request, 'classes': classes})

    def view_classes_removed(self, request):
        classes = ClasseModel.objects.filter(exists=False)
        return render(request, "askmath/manager/classe/manager_view_classes.html",
                      {'request': request, 'classes': classes, 'is_removed': True})

    def add_classe(self, request):
        if request.method == "POST":
            form = ClasseForm(request.POST, request.FILES)
            if form.is_valid():
                classe = form.save()
                messages.success(request, TextMessage.CLASSE_SUCCESS_ADD)
                return self.view_classes(request)
            else:
                messages.error(request, TextMessage.CLASSE_ERROR_ADD)
        else:
            form = ClasseForm()
        return render(request, "askmath/manager/classe/manager_form_classe.html",
                      {'request': request, 'form': form, 'title_form': _('Create Classe')})

    def remove_classe(self, request, classe):
        classe.delete()
        messages.success(request, TextMessage.CLASSE_SUCCESS_REM)
        return self.view_classes(request)

    def edit_classe(self, request, classe):
        if request.method == 'POST':
            form = ClasseForm(request.POST, request.FILES, instance=classe)
            if form.is_valid():
                classe = form.save()
                messages.success(request, TextMessage.CLASSE_SUCCESS_EDIT)
                return self.view_classes(request)
            else:
                messages.error(request, TextMessage.CLASSE_ERROR_EDIT)
        else:
            form = ClasseForm(instance=classe)
        return render(request, "askmath/manager/classe/manager_form_classe.html",
                      {'request': request, 'form': form, 'classe': classe, 'title_form': _('Edit Classe')})

    def restore_classe(self, request, classe):
        classe.restore()
        messages.success(request, TextMessage.CLASSE_SUCCESS_RESTORE)
        return self.view_classes(request)

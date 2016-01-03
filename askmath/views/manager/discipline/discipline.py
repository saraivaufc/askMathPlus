from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Discipline as CategoryModel
from askmath.entities import TextMessage
from django.contrib import messages
from idiscipline import IDiscipline
from askmath.forms import DisciplineForm
from django.utils.translation import ugettext_lazy as _

class Discipline(IDiscipline):
    def view_disciplines(self, request):
        disciplines = CategoryModel.objects.filter(exists=True)
        return render(request, "askmath/manager/discipline/manager_view_disciplines.html",
            {'request':request,'disciplines': disciplines})
    
    def view_disciplines_removed(self, request):
        disciplines = CategoryModel.objects.filter(exists=False)
        return render(request, "askmath/manager/discipline/manager_view_disciplines.html", 
            {'request':request,'disciplines': disciplines,'is_removed': True})
    
    def add_discipline(self, request):
        if request.method == "POST":
            form = DisciplineForm(request.POST)
            if form.is_valid():
                discipline = form.save()
                messages.success(request, TextMessage.DISCIPLINE_SUCCESS_ADD)
                return self.view_disciplines(request)
            else:
                messages.error(request, TextMessage.DISCIPLINE_ERROR_ADD)
        else:
            form = DisciplineForm()
        return render(request, "askmath/manager/discipline/manager_form_discipline.html", 
            {'request':request,'form': form, 'title_form':_('Create Discipline')})
    
    def remove_discipline(self, request, discipline):
        discipline.delete()
        messages.success(request, TextMessage.DISCIPLINE_SUCCESS_REM)
        return self.view_disciplines(request)
    def edit_discipline(self, request, discipline):
        if request.method == 'POST':
            form = DisciplineForm(request.POST, instance = discipline)
            if form.is_valid():
                discipline=form.save()
                messages.success(request, TextMessage.DISCIPLINE_SUCCESS_EDIT)
                return self.view_disciplines(request)
            else:
                messages.error(request, TextMessage.DISCIPLINE_ERROR_EDIT)
        else:
            form = DisciplineForm( instance = discipline)
        return render(request, "askmath/manager/discipline/manager_form_discipline.html", 
            {'request':request,'form': form,'discipline': discipline, 'title_form':_('Edit Discipline')})
    
    def restore_discipline(self, request, discipline):
        discipline.restore()
        messages.success(request, TextMessage.DISCIPLINE_SUCCESS_RESTORE)
        return self.view_disciplines(request)
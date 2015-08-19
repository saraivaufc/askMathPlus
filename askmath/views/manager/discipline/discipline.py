from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Discipline as DisciplineModel
from askmath.entities import Message, TextMessage, TypeMessage
from idiscipline import IDiscipline
from askMathPlus.settings import COLORS_ALL
from askmath.forms import DisciplineForm
from django.utils.translation import ugettext_lazy as _

class Discipline(IDiscipline):
    def view_disciplines(self, request, message = None):
        disciplines = DisciplineModel.objects.filter(exists=True)
        return render(request, "askmath/manager/discipline/manager_view_disciplines.html",
            {'request':request,'disciplines': disciplines, 'colors': COLORS_ALL, 'message': message})
    
    def view_disciplines_removed(self, request, message = None):
        disciplines = DisciplineModel.objects.filter(exists=False)
        return render(request, "askmath/manager/discipline/manager_view_disciplines.html", 
            {'request':request,'disciplines': disciplines,'is_removed': True, 'colors': COLORS_ALL, 'message': message})
    
    def view_discipline(self, request, discipline,message = None):
        return render(request, "askmath/manager/discipline/manager_view_discipline.html", 
            {'request':request,'discipline': discipline, 'message': message, 'colors': COLORS_ALL})
    
    
    
    def add_discipline(self, request, message = None):
        if request.method == "POST":
            form = DisciplineForm(request.POST)
            if form.is_valid():
                discipline = form.save()
                message = Message(TextMessage.DISCIPLINE_SUCCESS_ADD, TypeMessage.SUCCESS)
                return self.view_discipline(request, discipline, message)
        else:
            form = DisciplineForm()
        return render(request, "askmath/manager/discipline/manager_form_discipline.html", 
            {'request':request,'form': form, 'title_form':_('Create Discipline'), 'message': message})
    
    def remove_discipline(self, request, discipline, message = None):
        discipline.delete()
        message = Message(TextMessage.DISCIPLINE_SUCCESS_REM, TypeMessage.SUCCESS)
        return self.view_disciplines(request, message)
    def edit_discipline(self, request, discipline, message = None):
        if request.method == 'POST':
            form = DisciplineForm(request.POST, instance = discipline)
            if form.is_valid():
                discipline=form.save()
                message = Message(TextMessage.DISCIPLINE_SUCCESS_EDIT, TypeMessage.SUCCESS)
                return self.view_discipline(request,discipline , message)
        else:
            form = DisciplineForm( instance = discipline)
        return render(request, "askmath/manager/discipline/manager_form_discipline.html", 
            {'request':request,'form': form,'discipline': discipline, 'title_form':_('Edit Discipline'), 'message': message})
    
    def restore_discipline(self, request, discipline):
        discipline.restore()
        message = Message(TextMessage.DISCIPLINE_SUCCESS_RESTORE, TypeMessage.SUCCESS)
        return self.view_disciplines(request, message)
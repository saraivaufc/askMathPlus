from askmath.entities import TextMessage
from askmath.forms import DisciplineForm
from askmath.models import Discipline as DisciplineModel
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from idiscipline import IDiscipline


class Discipline(IDiscipline):
	def view_disciplines(self, request):
		disciplines = DisciplineModel.objects.filter(exists=True)
		return render(request, "askmath/manager/discipline/manager_view_disciplines.html",
			{'request': request, 'disciplines': disciplines})

	def view_disciplines_removed(self, request):
		disciplines = DisciplineModel.objects.filter(exists=False)
		return render(request, "askmath/manager/discipline/manager_view_disciplines.html",
			{'request': request, 'disciplines': disciplines, 'is_removed': True})

	def view_discipline(self, request, discipline):
		return render(request, "askmath/manager/discipline/manager_view_discipline.html",
			{'request': request, 'discipline': discipline})

	def add_discipline(self, request):
		if request.method == "POST":
			form = DisciplineForm(request.POST)
			if form.is_valid():
				discipline = form.save()
				messages.success(request, TextMessage.DISCIPLINE_SUCCESS_ADD)
				return HttpResponseRedirect(reverse('askmath:manager_discipline_view', kwargs={'id_discipline': discipline.id}))
			else:
				messages.error(request, TextMessage.DISCIPLINE_ERROR_ADD)
		else:
			form = DisciplineForm()
		return render(request, "askmath/manager/discipline/manager_form_discipline.html",
			{'request': request, 'form': form, 'title_form': _('Create Discipline')})

	def remove_discipline(self, request, discipline):
		discipline.delete()
		messages.success(request, TextMessage.DISCIPLINE_SUCCESS_REM)
		return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

	def edit_discipline(self, request, discipline):
		if request.method == 'POST':
			form = DisciplineForm(request.POST, instance=discipline)
			if form.is_valid():
				discipline = form.save()
				messages.success(request, TextMessage.DISCIPLINE_SUCCESS_EDIT)
				return HttpResponseRedirect(reverse('askmath:manager_discipline_view', kwargs={'id_discipline': discipline.id}))
			else:
				messages.error(request, TextMessage.DISCIPLINE_ERROR_EDIT)
		else:
			form = DisciplineForm(instance=discipline)
		return render(request, "askmath/manager/discipline/manager_form_discipline.html",
					  {'request': request, 'form': form, 'discipline': discipline, 'title_form': _('Edit Discipline')})

	def restore_discipline(self, request, discipline):
		discipline.restore()
		messages.success(request, TextMessage.DISCIPLINE_SUCCESS_RESTORE)
		return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

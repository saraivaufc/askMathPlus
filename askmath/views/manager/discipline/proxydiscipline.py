from askmath.entities import TextMessage
from askmath.models.discipline import Discipline as DisciplineModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from .discipline import Discipline
from .idiscipline import IDiscipline


class ProxyDiscipline(IDiscipline):
	def __init__(self):
		self.__discipline = Discipline()

	@method_decorator(login_required)
	def view_disciplines(self, request):
		if request.user.has_perm("askmath.read_discipline") and request.user.has_perm("askmath.access_manager"):
			try:
				return self.__discipline.view_disciplines(request)
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)

		return HttpResponseRedirect(reverse('askmath:home'))

	@method_decorator(login_required)
	def view_disciplines_removed(self, request):
		if request.user.has_perm("askmath.read_discipline") and request.user.has_perm("askmath.access_manager"):
			try:
				return self.__discipline.view_disciplines_removed(request)
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)

		return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

	@method_decorator(login_required)
	def view_discipline(self, request, id_discipline):
		if request.user.has_perm("askmath.write_discipline") and request.user.has_perm("askmath.access_manager"):
			try:
				discipline = DisciplineModel.objects.get(id=id_discipline)
			except Exception, e:
				print e
				messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
				return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

			try:
				return self.__discipline.view_discipline(request, discipline)
			except Exception, e:
				print e
				messages.error(request, TextMessage.DISCIPLINE_ERROR_REM)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)
			
		return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

	@method_decorator(login_required)
	def add_discipline(self, request):
		if request.user.has_perm("askmath.write_discipline") and request.user.has_perm("askmath.access_manager"):
			try:
				return self.__discipline.add_discipline(request)
			except Exception, e:
				print e
				messages.error(request, TextMessage.DISCIPLINE_ERROR_ADD)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)

		return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

	@method_decorator(login_required)
	def remove_discipline(self, request, id_discipline):
		if request.user.has_perm("askmath.write_discipline") and request.user.has_perm("askmath.access_manager"):
			try:
				discipline = DisciplineModel.objects.get(id=id_discipline)
			except Exception, e:
				print e
				messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
				return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

			try:
				return self.__discipline.remove_discipline(request, discipline)
			except Exception, e:
				print e
				messages.error(request, TextMessage.DISCIPLINE_ERROR_REM)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)

		return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
	@method_decorator(login_required)
	def edit_discipline(self, request, id_discipline):
		if request.user.has_perm("askmath.write_discipline") and request.user.has_perm("askmath.access_manager"):
			try:
				discipline = DisciplineModel.objects.get(id=id_discipline)
			except Exception, e:
				print e
				messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
				return self.view_disciplines(request)
			try:
				return self.__discipline.edit_discipline(request, discipline)
			except Exception, e:
				print e
				messages.error(request, TextMessage.DISCIPLINE_ERROR_EDIT)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)

		return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

	@method_decorator(login_required)
	def restore_discipline(self, request, id_discipline):
		if request.user.has_perm("askmath.write_discipline") and request.user.has_perm("askmath.access_manager"):
			try:
				discipline = DisciplineModel.objects.get(id=id_discipline)
			except Exception, e:
				print e
				messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
				return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
			try:
				return self.__discipline.restore_discipline(request, discipline)
			except Exception, e:
				print e
				messages.error(request, TextMessage.DISCIPLINE_ERROR_RESTORE)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)

		return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))

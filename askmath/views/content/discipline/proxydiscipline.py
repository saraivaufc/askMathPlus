from .idiscipline import IDiscipline
from .discipline import Discipline
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from askmath.entities import TextMessage
from django.contrib import messages

from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.users import Student as StudentModel

from askmath.views.index import ProxyHome

class ProxyDiscipline(IDiscipline):
	def __init__(self):
		self.__discipline = Discipline()
		self.__proxy_home = ProxyHome()

	@method_decorator(login_required)
	def view_disciplines(self, request):
		if request.user.has_perm("askmath.read_discipline")  and request.user.has_perm("askmath.access_content"):
			
			try:
				student = request.user.get_person_class(request.user, StudentModel)
				current_classe = student.get_current_classe()
				print  student.get_current_classe()
				if current_classe != None:
					return self.__discipline.view_disciplines(request, current_classe)
			except Exception, e:
				print e

			try:
				return self.__discipline.view_disciplines(request)
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)
		return self.__proxy_home.index(request)

	@method_decorator(login_required)
	def view_discipline(self, request, id_discipline):
		if request.user.has_perm("askmath.read_discipline")  and request.user.has_perm("askmath.access_content"):
			try:
				discipline = DisciplineModel.objects.get(id = id_discipline,exists=True)
			except Exception, e:
				print e
				messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
				return self.view_disciplines(request)
			
			try:
				return self.__discipline.view_discipline(request,discipline)
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)
		return self.view_disciplines(request)
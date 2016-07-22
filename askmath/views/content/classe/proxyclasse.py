from askmath.entities import TextMessage
from askmath.models.classe import Classe as ClasseModel
from askmath.models.users import Student as StudentModel
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
		if request.user.has_perm("askmath.read_classe")  and request.user.has_perm("askmath.access_content"):
			try:
				student = request.user.get_person_class(request.user, StudentModel)
				return self.__classe.view_classes(request, student)
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)
		return HttpResponseRedirect( reverse('askmath:home') )

	@method_decorator(login_required)
	def view_classe(self, request, id_classe):
		if request.user.has_perm("askmath.read_classe")  and request.user.has_perm("askmath.access_content"):
			try:
				classe = ClasseModel.objects.get(id=id_classe, exists=True, visible=True)
				student = request.user.get_person_class(request.user, StudentModel)
				return self.__classe.view_classe(request,student, classe)
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
				return HttpResponseRedirect( reverse('askmath:content_classe_view') )
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)
		return HttpResponseRedirect( reverse('askmath:home') )

	@method_decorator(login_required)
	def set_current(self, request, id_classe):
		if request.user.has_perm("askmath.read_classe")  and request.user.has_perm("askmath.access_content"):	
			try:
				student = request.user.get_person_class(request.user, StudentModel)
				classe = ClasseModel.objects.get(id=id_classe, exists=True, visible=True)
				return self.__classe.set_current(request, student, classe)
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
				return HttpResponseRedirect( reverse('askmath:content_classe_view') )
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)
		return HttpResponseRedirect( reverse('askmath:home') )

	def join_classe(self, request, id_classe):
		if request.user.has_perm("askmath.read_classe")  and request.user.has_perm("askmath.access_content"):
			
			try:
				classe = ClasseModel.objects.get(id=id_classe, exists=True, visible=True)
				student = request.user.get_person_class(request.user, StudentModel)
				if classe != None:
					return self.__classe.join_classe(request, student,  classe)
				else:
					messages.error(request, TextMessage.CLASSE_NOT_FOUND)
					return HttpResponseRedirect( reverse('askmath:content_classe_view') )	
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)
		return HttpResponseRedirect( reverse('askmath:home') )

	def out_classe(self, request,  id_classe):
		if request.user.has_perm("askmath.read_classe")  and request.user.has_perm("askmath.access_content"):
			try:
				classe = ClasseModel.objects.get(id=id_classe, exists=True, visible=True)
				student = request.user.get_person_class(request.user, StudentModel)
				if classe != None:
					return self.__classe.out_classe(request, student,  classe)
				else:
					messages.error(request, TextMessage.CLASSE_NOT_FOUND)
					return HttpResponseRedirect( reverse('askmath:content_classe_view') )	
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)
		return HttpResponseRedirect( reverse('askmath:home') )
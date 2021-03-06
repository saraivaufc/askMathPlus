from askmath.entities import TextMessage
from askmath.models.classe import Classe as ClasseModel
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .iclasse import IClasse


class Classe(IClasse):
	def view_classes(self, request, student):
		my_classes = student.get_classes()
		current_classe = student.get_current_classe()
		classes = ClasseModel.objects.filter(exists=True, visible=True)
		return render(request, "askmath/content/classe/content_view_classes.html",
					  {'request': request, 'classes': classes, 'my_classes': my_classes,
					   'current_classe': current_classe})

	def view_classe(self, request, student, classe):
		my_classes = student.get_classes()
		current_classe = student.get_current_classe()
		return render(request, "askmath/content/classe/content_view_classe.html",
					  {'request': request, 'classe': classe, 'my_classes': my_classes,
					   'current_classe': current_classe})

	def set_current(self, request, student, classe):
		if student.set_current_classe(classe):
			messages.success(request, TextMessage.CLASSE_SUCCESS_SET)
		else:
			messages.error(request, TextMessage.CLASSE_ERROR_SET)
		return HttpResponseRedirect(reverse('askmath:content_classe_view', kwargs={'id_classe': classe.id}))

	def join_classe(self, request, student, classe):
		if student.join_classe(student, classe):
			messages.success(request, TextMessage.CLASSE_SUCCESS_JOIND)
		else:
			messages.error(request, TextMessage.CLASSE_ERROR_JOIND)
		return HttpResponseRedirect(reverse('askmath:content_classe_view', kwargs={'id_classe': classe.id}))

	def out_classe(self, request, student, classe):
		if student.out_classe(student, classe):
			messages.success(request, TextMessage.CLASSE_SUCCESS_OUT)
		else:
			messages.error(request, TextMessage.CLASSE_ERROR_OUT)
		return HttpResponseRedirect(reverse('askmath:content_classe_view', kwargs={'id_classe': classe.id}))

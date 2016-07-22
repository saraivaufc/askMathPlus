from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

#MODELS
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from askmath.entities import TextMessage
from django.contrib import messages

from .ilesson import ILesson
from .lesson import Lesson

class ProxyLesson(ILesson):
	
	def __init__(self):
		self.__lesson = Lesson()

	@method_decorator(login_required)
	def view_lesson(self, request,id_discipline=None, id_lesson=None):
		if request.user.has_perm("askmath.read_lesson")  and request.user.has_perm("askmath.access_content"):
			try:
				lesson = LessonModel.objects.get(id = id_lesson, exists=True)
			except Exception, e:
				print e
				messages.error(request, TextMessage.LESSON_NOT_FOUND)
				return HttpResponseRedirect( reverse('askmath:content_discipline_view', kwargs={'id_discipline':id_discipline}) )
			
			try:
				discipline = DisciplineModel.objects.filter(id = id_discipline, exists=True,visible=True)[0]
			except Exception, e:
				print e
				try:
					discipline = lesson.get_discipline()
				except Exception, e:
					print e
					messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
				return HttpResponseRedirect( reverse('askmath:content_discipline_view') )
			
			try:
				return self.__lesson.view_lesson(request,discipline, lesson)
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)
		return HttpResponseRedirect( reverse('askmath:content_discipline_view', kwargs={'id_discipline':id_discipline}) )
from askmath.entities import TextMessage
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from askmath.models.video import Video as VideoModel
from askmath.views.index import ProxyHome
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .ivideo import IVideo
from .video import Video


class ProxyVideo(IVideo):
	def __init__(self):
		self.__video = Video()

	@method_decorator(login_required)
	def view_videos(self, request, id_discipline, id_lesson):
		if request.user.has_perm("askmath.read_video") and request.user.has_perm("askmath.access_content"):
			try:
				discipline = DisciplineModel.objects.filter(id=id_discipline, exists=True, visible=True)[0]
			except Exception, e:
				print e
				messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
				return HttpResponseRedirect(reverse('askmath:content_discipline_view'))
			try:
				lesson = LessonModel.objects.filter(id=id_lesson, exists=True, visible=True)[0]
			except Exception, e:
				print e
				messages.error(request, TextMessage.LESSON_NOT_FOUND)
				return HttpResponseRedirect( reverse('askmath:content_discipline_view', kwargs={'id_discipline': id_discipline}))
			try:
				return self.__video.view_videos(request, discipline, lesson)
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
				return HttpResponseRedirect(reverse('askmath:content_lesson_view', kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)
		return HttpResponseRedirect( reverse('askmath:content_lesson_view', kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

	@method_decorator(login_required)
	def view_video(self, request, id_video, id_discipline=None, id_lesson=None):
		if request.user.has_perm("askmath.read_video") and request.user.has_perm("askmath.access_content"):
			try:
				discipline = DisciplineModel.objects.filter(id=id_discipline, exists=True, visible=True)[0]
			except Exception, e:
				print e
				try:
					discipline = lesson.disciplines.filter(exists=True, visible=True)[0]
				except Exception, e:
					print e
					messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
					return HttpResponseRedirect(reverse('askmath:content_discipline_view'))
			try:
				lesson = LessonModel.objects.filter(id=id_lesson, exists=True, visible=True)[0]
			except Exception, e:
				print e
				try:
					lesson = video.get_lesson();
				except Exception, e:
					print e
					messages.error(request, TextMessage.LESSON_NOT_FOUND)
					return HttpResponseRedirect( reverse('askmath:content_discipline_view', kwargs={'id_discipline': id_discipline}))

			try:
				video = VideoModel.objects.filter(id=id_video, exists=True, visible=True)[0]
			except Exception, e:
				print e
				messages.error(request, TextMessage.VIDEO_NOT_FOUND)
				return HttpResponseRedirect(reverse('askmath:content_lesson_view', kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

			if not video in lesson.get_videos():
				messages.error(request, TextMessage.VIDEO_NOT_FOUND_IN_LESSON)
				return HttpResponseRedirect(reverse('askmath:content_video_view', kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

			try:
				return self.__video.view_video(request, discipline, lesson, video)
			except Exception, e:
				print e
				messages.error(request, TextMessage.ERROR)
		else:
			messages.error(request, TextMessage.USER_NOT_PERMISSION)
		return HttpResponseRedirect(reverse('askmath:content_video_view', kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))
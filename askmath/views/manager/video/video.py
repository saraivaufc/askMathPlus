from askmath.entities import TextMessage
from askmath.forms import VideoForm
from askmath.models.video import Video as VideoModel
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from .ivideo import IVideo


class Video(IVideo):
	def view_videos(self, request, lesson, discipline):
		videos = lesson.get_videos()
		return render(request, "askmath/manager/video/manager_view_videos.html",
					  {'request': request, 'discipline': discipline, 'lesson': lesson, 'videos': videos})

	def view_videos_removed(self, request, lesson, discipline):
		videos = VideoModel.objects.filter(exists=False, lesson=lesson.id)
		return render(request, "askmath/manager/video/manager_view_videos.html",
					  {'request': request, 'discipline': discipline, 'lesson': lesson, 'videos': videos,
					   'is_removed': True})

	def view_video(self, request, lesson, discipline, video):
		return render(request, "askmath/manager/video/manager_view_video.html", {'request': request, 'discipline': discipline, 'lesson': lesson, 'video': video})

	def add_video(self, request, lesson, discipline):
		if request.method == "POST":
			request.POST = request.POST.copy()
			request.POST['lesson'] = lesson.id
			try:
				positions = map(lambda x: x.position, lesson.get_videos())
			except Exception, e:
				print e
				positions = [0, ]
			if not positions or len(positions):
				positions = [0, ]
			request.POST['position'] = max(positions) + 1
			form = VideoForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				messages.success(request, TextMessage.VIDEO_SUCCESS_ADD)
				return HttpResponseRedirect(reverse('askmath:manager_video_view',
													kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))
			else:
				messages.error(request, TextMessage.ERROR_FORM)
		else:
			form = VideoForm()
		return render(request, "askmath/manager/video/manager_form_video.html",
					  {'request': request, 'form': form, 'discipline': discipline, 'lesson': lesson,
					   'title_form': _('Create Video')})

	def remove_video(self, request, video, lesson, discipline):
		video.delete()
		messages.success(request, TextMessage.VIDEO_SUCCESS_REM)
		return HttpResponseRedirect(reverse('askmath:manager_video_view',
											kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))

	def edit_video(self, request, video, lesson, discipline):
		if request.method == "POST":
			request.POST = request.POST.copy()
			request.POST['lesson'] = lesson.id

			form = VideoForm(request.POST, request.FILES, instance=video)
			if form.is_valid():
				video = form.save()
				messages.success(request, TextMessage.VIDEO_SUCCESS_EDIT)
				return HttpResponseRedirect(reverse('askmath:manager_video_view', kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id, 'id_video': video.id}))
			else:
				messages.error(request, TextMessage.ERROR_FORM)
		else:
			form = VideoForm(instance=video)
		return render(request, "askmath/manager/video/manager_form_video.html",
					  {'request': request, 'form': form, 'discipline': discipline, 'lesson': lesson, 'video': video,
					   'title_form': _('Edit Video')})

	def restore_video(self, request, video, lesson, discipline):
		video.restore()
		messages.success(request, TextMessage.VIDEO_SUCCESS_RESTORE)
		return HttpResponseRedirect(reverse('askmath:manager_video_view',
											kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))

	def sort_videos(self, request, lesson, discipline, new_order=None):
		videos = VideoModel.objects.filter(exists=True, visible=True, lesson=lesson.id)
		if request.method == 'POST':
			try:
				for index, i in enumerate(new_order):
					VideoModel.objects.filter(id=i).update(position=index + 1)
					messages.success(request, TextMessage.VIDEO_SUCCESS_SORT)
			except Exception, e:
				print e
				messages.error(request, TextMessage.VIDEO_ERROR_SORT)
		return render(request, "askmath/manager/video/manager_view_videos_sort.html",
					  {'request': request, 'discipline': discipline, 'lesson': lesson, 'videos': videos})

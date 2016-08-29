# -*- encoding=UTF-8 -*-

from askmath.entities import TextMessage
from askmath.forms import LessonForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from .ilesson import ILesson


class Lesson(ILesson):

	def view_lesson(self, request, lesson):
		return render(request, "askmath/manager/lesson/manager_view_lesson.html",
			{'request': request, 'discipline': lesson.get_discipline() , 'lesson': lesson})

	def add_lesson(self, request, discipline):
		if request.method == "POST":
			request.POST['discipline'] = discipline.id
			form = LessonForm(request.POST)
			if form.is_valid():
				lesson = form.save()
				messages.success(request, TextMessage.LESSON_SUCCESS_ADD)
				return HttpResponseRedirect(reverse('askmath:manager_lesson_view', kwargs={'id_lesson': lesson.id}))
			else:
				messages.error(request, TextMessage.LESSON_ERROR_ADD)
		else:
			form = LessonForm()
		return render(request, "askmath/manager/lesson/manager_form_lesson.html",
					  {'request': request, 'discipline': discipline, 'form': form, 'title_form': _('New Lesson')})

	def remove_lesson(self, request, lesson):
		lesson.delete()
		messages.success(request, TextMessage.LESSON_SUCCESS_REM)
		return HttpResponseRedirect(reverse('askmath:manager_discipline_view', kwargs={'id_discipline': lesson.get_discipline().id}))

	def edit_lesson(self, request, lesson):
		if request.method == 'POST':
			request.POST['discipline'] = lesson.get_discipline().id
			form = LessonForm(request.POST, instance=lesson)
			if form.is_valid():
				lesson = form.save()
				messages.success(request, TextMessage.LESSON_SUCCESS_EDIT)
				return HttpResponseRedirect( reverse('askmath:manager_lesson_view', kwargs={'id_lesson': lesson.id}))
			else:
				messages.error(request, TextMessage.LESSON_ERROR_EDIT)
		else:
			form = LessonForm(instance=lesson)
		return render(request, "askmath/manager/lesson/manager_form_lesson.html", {'request': request, 'form': form, 'discipline': lesson.get_discipline(), 'lesson': lesson, 'title_form': _('Edit Lesson')})

	def restore_lesson(self, request, lesson):
		lesson.restore()
		messages.success(request, TextMessage.LESSON_SUCCESS_RESTORE)
		return HttpResponseRedirect(reverse('askmath:manager_lesson_view', kwargs={'id_lesson': lesson.id}))

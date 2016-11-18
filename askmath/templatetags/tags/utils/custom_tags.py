# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from askmath.models.state import StudentLessonState
from .. import register


@register.simple_tag(name='SETTINGS')
def settings_value(name):
    return getattr(settings, name, "")

@register.simple_tag(name='lesson_is_complete')
def lesson_sorting(lesson, student, ret):
	try:
		studentlessonstate = StudentLessonState.objects.get(student=student, discipline=lesson.get_discipline(), lesson=lesson,
															exists=True)
	except Exception, e:
		print e
		studentlessonstate = StudentLessonState(student=student, discipline=lesson.get_discipline(), lesson=lesson,
												remaining_jump=lesson.get_maximum_hops())
		studentlessonstate.save()

	question = studentlessonstate.get_question()
	if not question and len(lesson.get_questions_visibles()) > 0:
		return ret
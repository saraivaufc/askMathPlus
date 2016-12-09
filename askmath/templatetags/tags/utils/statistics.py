# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import register
from askmath.models.lesson import Lesson
from askmath.models.state import StudentLessonState
from askmath.models.experience import StudentExperience


@register.filter(name='student_lesson_complete')
def student_lesson_complete(student):
	studentLessonStates = StudentLessonState.objects.filter(student = student.id, percentage_completed=100, exists=True)
	return studentLessonStates

@register.filter(name='student_lesson_redone')
def student_lesson_redone(student):
	studentLessonStates = StudentLessonState.objects.filter(student = student.id, percentage_completed=100, exists=False)
	return studentLessonStates

@register.filter(name='student_lesson_in_progress')
def student_lesson_in_progress(student):
	studentLessonStates = StudentLessonState.objects.filter(student = student.id, percentage_completed__in=range(1,100), exists=True)
	return studentLessonStates

@register.filter(name='student_experience')
def student_scores(student):
	studentExperience = StudentExperience.objects.filter(student = student.id, exists=True).first()
	return studentExperience
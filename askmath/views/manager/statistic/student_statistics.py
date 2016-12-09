#-*- encoding=UTF-8 -*-


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from askmath.models.users import Student
from askmath.models.state import StudentLessonState
from django.utils.translation import ugettext as _


class StudentStatistics():
	@method_decorator(login_required)
	def list_students(self, request):
		students = Student.objects.filter(exists=True, is_active=True)
		return render(request, "askmath/manager/statistic/student_statistics/list_students.html", {'request': request, 'students': students})

	@method_decorator(login_required)
	def lessons_completed(self, request, id_student):
		student = Student.objects.filter(id=id_student, exists=True, is_active=True).first()
		studentLessonStates = StudentLessonState.objects.filter(student = student.id, percentage_completed=100, exists=True)
		return render(request, "askmath/manager/statistic/student_statistics/list_lessons.html", {'request': request, 'student': student, 'studentLessonStates': studentLessonStates, 'type':_("completed")})

	@method_decorator(login_required)
	def lessons_redone(self, request, id_student):
		student = Student.objects.filter(id=id_student, exists=True, is_active=True).first()
		studentLessonStates = StudentLessonState.objects.filter(student = student.id, percentage_completed=100, exists=False)
		return render(request, "askmath/manager/statistic/student_statistics/list_lessons.html", {'request': request, 'student': student, 'studentLessonStates': studentLessonStates, 'type':_("redone")})

	@method_decorator(login_required)
	def lessons_in_progress(self, request, id_student):
		student = Student.objects.filter(id=id_student, exists=True, is_active=True).first()
		if student:
			studentLessonStates = StudentLessonState.objects.filter(student = student.id, percentage_completed__in=range(1,100), exists=True)
		else:
			studentLessonStates = []
		return render(request, "askmath/manager/statistic/student_statistics/list_lessons.html", {'request': request, 'student': student, 'studentLessonStates': studentLessonStates, 'type':_("in progress")})
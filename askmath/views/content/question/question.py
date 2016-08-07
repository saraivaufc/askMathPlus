from askmath.entities import ExperienceLevel
from askmath.entities import TextMessage
from askmath.models.experience import StudentExperience
from askmath.models.state import StudentLessonState
from askmath.models.users import Student as StudentModel
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .iquestion import IQuestion

PERCENT_DOWN_SCORES_IN_RESET_LESSON  = 0.75

class Question(IQuestion):
	def view_question(self, request, discipline, lesson, question=None, definitive=False):
		try:
			student = StudentModel.objects.get(id=request.user.id)
		except Exception, e:
			print e
			messages.error(request, TextMessage.USER_NOT_FOUND)
			return HttpResponseRedirect(
				reverse('askmath:content_lesson_view', kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))

		student_experience = student.get_student_experience()

		experience_level = ExperienceLevel(student_experience.level)

		try:
			studentlessonstate = StudentLessonState.objects.get(student=student, discipline=discipline, lesson=lesson,
																exists=True)
		except Exception, e:
			print e
			studentlessonstate = StudentLessonState(student=student, discipline=discipline, lesson=lesson,
													remaining_jump=lesson.get_maximum_hops())
			studentlessonstate.save()

		studentlessonstate.update()
		if not definitive:
			question = studentlessonstate.get_question(question, True)

		if not question and len(lesson.get_questions_visibles()) > 0:
			lesson_complete = True
		else:
			lesson_complete = False

		occur_obstacle = studentlessonstate.occur_obstacle()
		deficiencies = studentlessonstate.get_deficiencies()

		return render(request, "askmath/content/question/view_question.html",
					  {'request': request, 'discipline': discipline, 'lesson': lesson,
					   'studentlessonstate': studentlessonstate, 'lesson_complete': lesson_complete,
					   'experience_level': experience_level, 'question': question,
					   'occur_obstacle': occur_obstacle, 'deficiencies': deficiencies, 'student_experience':student_experience})

	def answer_question(self, request, discipline, lesson, question, item):
		if request.method == 'POST':
			try:
				student = StudentModel.objects.get(id=request.user.id)
			except Exception, e:
				print e
				messages.error(request, TextMessage.USER_NOT_FOUND)
				return HttpResponseRedirect(reverse('askmath:content_question_view',
													kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))
			try:
				studentlessonstate = StudentLessonState.objects.get(student=student, discipline=discipline,
																	lesson=lesson, exists=True)
			except Exception, e:
				print e
				studentlessonstate = StudentLessonState(student=student, discipline=discipline, lesson=lesson,
														remaining_jump=lesson.get_maximum_hops())
				studentlessonstate.save()
			try:
				studentlessonstate.answer_question(request, question, item)
			except Exception, e:
				messages.error(request, TextMessage.ERROR)
		else:
			messages.error(request, TextMessage.METHOD_NOT_POST)

		return HttpResponseRedirect(reverse('askmath:content_question_view',
											kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id,
													'id_question': question.id}))

	def jump_question(self, request, discipline, lesson, question):
		try:
			student = StudentModel.objects.get(id=request.user.id)
		except Exception, e:
			print e
			messages.error(request, TextMessage.USER_NOT_FOUND)
			return HttpResponseRedirect(reverse('askmath:content_question_view',
												kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))

		try:
			studentlessonstate = StudentLessonState.objects.get(student=student, discipline=discipline, lesson=lesson,
																exists=True)
		except Exception, e:
			print e
			studentlessonstate = StudentLessonState(student=student, discipline=discipline, lesson=lesson,
													remaining_jump=lesson.get_maximum_hops())
			studentlessonstate.save()
		if studentlessonstate.get_remaining_jump():
			try:
				studentlessonstate.add_skipped_question(request, question)
			except Exception, e:
				print e
				messages.warning(request, TextMessage.QUESTION_ERROR_JUMP)
		else:
			messages.warning(request, TextMessage.LESSON_NOT_REMAINING_JUMPS)

		return HttpResponseRedirect(reverse('askmath:content_question_view',
											kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id,
													'id_question': question.id}))

	def choose_skipped_question(self, request, discipline, lesson, question):
		try:
			student = StudentModel.objects.get(id=request.user.id)
		except Exception, e:
			print e
			messages.error(request, TextMessage.USER_NOT_FOUND)
			return HttpResponseRedirect(reverse('askmath:content_question_view',
												kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))
		try:
			studentlessonstate = StudentLessonState.objects.get(student=student, discipline=discipline, lesson=lesson,
																exists=True)
		except Exception, e:
			print e
			studentlessonstate = StudentLessonState(student=student, discipline=discipline, lesson=lesson,
													remaining_jump=lesson.get_maximum_hops())
			studentlessonstate.save()
		studentlessonstate.remove_skipped_question(question)

		return self.view_question(request, discipline, lesson, question, True)

	def reset_lesson(self, request, discipline, lesson):
		try:
			student = StudentModel.objects.get(id=request.user.id)
		except Exception, e:
			print e
			messages.error(request, TextMessage.USER_NOT_FOUND)
			return HttpResponseRedirect(
				reverse('askmath:content_lesson_view', kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))

		try:
			studentlessonstate = StudentLessonState.objects.get(student=student, discipline=discipline, lesson=lesson, exists=True)
		except Exception, e:
			print e
			studentlessonstate = StudentLessonState(student=student, discipline=discipline, lesson=lesson, remaining_jump=lesson.get_maximum_hops())
			studentlessonstate.save()

		student_experience = student.get_student_experience()

		student_experience.down_scores(int( studentlessonstate.get_scores()  * PERCENT_DOWN_SCORES_IN_RESET_LESSON )  )
		studentlessonstate.delete()
		
		messages.success(request, TextMessage.LESSON_SUCCESS_RESET)
		return HttpResponseRedirect(
			reverse('askmath:content_question_view', kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))

	def help_quetion(self, request, discipline, lesson, question):
		try:
			student = StudentModel.objects.get(id=request.user.id)
		except Exception, e:
			print e
			messages.error(request, TextMessage.USER_NOT_FOUND)
			return HttpResponseRedirect(reverse('askmath:content_question_view',
												kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))

		try:
			studentlessonstate = StudentLessonState.objects.get(student=student, discipline=discipline, lesson=lesson,
																exists=True)
		except Exception, e:
			print e
			studentlessonstate = StudentLessonState(student=student, discipline=discipline, lesson=lesson,
													remaining_jump=lesson.get_maximum_hops())
			studentlessonstate.save()

		try:
			studentlessonstate.add_help_question(question)
		except Exception, e:
			print e
			return HttpResponse("False")
		return HttpResponse("True")

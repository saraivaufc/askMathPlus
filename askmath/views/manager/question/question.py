from askmath.entities import TextMessage
from askmath.forms import QuestionForm, ItemForm
from askmath.models.question import Item as ItemModel
from askmath.models.question import Question as QuestionModel
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from .iquestion import IQuestion


class Question(IQuestion):
	def view_questions(self, request, lesson, discipline, question=None):
		context = {'request': request, 'discipline': discipline, 'lesson': lesson}
		if question:
			context['question'] = question
			return render(request, "askmath/manager/question/manager_view_question.html",context)
		else:
			questions = lesson.get_questions()
			context['questions'] = questions
			return render(request, "askmath/manager/question/manager_view_questions.html",context)

	def view_questions_removed(self, request, lesson, discipline):
		questions = QuestionModel.objects.filter(exists=False, lesson=lesson.id)
		return render(request, "askmath/manager/question/manager_view_questions.html",
					  {'request': request, 'discipline': discipline, 'lesson': lesson, 'questions': questions,
					   'is_removed': True})

	def add_question(self, request, lesson, discipline, quantity_items=5):
		if request.method == "POST":
			request.POST = request.POST.copy()
			request.POST['question-lesson'] = lesson.id

			forms_items = [ItemForm(request.POST, request.FILES, prefix=i) for i in range(1, quantity_items + 1)]
			list_items = []
			for index, i in enumerate(forms_items):
				if i.is_valid():
					new_item = i.save()
					ItemModel.objects.filter(id=new_item.id).update(position=index + 1)
					list_items.append(new_item.pk)

			try:
				positions = map(lambda x: x.position, lesson.get_questions())
			except Exception, e:
				print e
				positions = [0]
			if not positions:
				positions = [0]
			request.POST['question-items'] = list_items
			request.POST['question-position'] = max(positions) + 1
			form_question = QuestionForm(request.POST, request.FILES, prefix='question')
			if form_question.is_valid():
				question = form_question.save()
				messages.success(request, TextMessage.QUESTION_SUCCESS_ADD)
				return HttpResponseRedirect(reverse('askmath:manager_question_view',
													kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))
			else:
				messages.error(request, TextMessage.ERROR_FORM)
		else:
			form_question = QuestionForm(prefix='question')
			forms_items = [ItemForm(prefix=i) for i in range(1, quantity_items + 1)]
		return render(request, "askmath/manager/question/manager_form_question.html",
					  {'request': request, 'form_question': form_question, 'lesson': lesson, 'discipline': discipline,
					   'forms_items': forms_items, 'lesson': lesson, 'title_form': _('Create Question')})

	def remove_question(self, request, question, lesson, discipline):
		question.delete()
		messages.success(request, TextMessage.QUESTION_SUCCESS_REM)
		return HttpResponseRedirect(reverse('askmath:manager_question_view',
											kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))

	def edit_question(self, request, question, lesson, discipline):
		if request.method == "POST":
			request.POST = request.POST.copy()
			request.POST['question-lesson'] = lesson.id

			forms_items = forms_items = [ItemForm(request.POST, request.FILES, instance=i, prefix=index + 1) for index, i in enumerate(question.get_items())]
			list_items = []
			for i in forms_items:
				if i.is_valid():
					new_item = i.save()
					list_items.append(new_item.pk)
			request.POST['question-items'] = list_items
			request.POST['question-position'] = question.position
			form_question = QuestionForm(request.POST, request.FILES, instance=question, prefix='question')
			if form_question.is_valid():
				question = form_question.save()
				messages.success(request, TextMessage.QUESTION_SUCCESS_EDIT)
				return HttpResponseRedirect(reverse('askmath:manager_question_view',
													kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))
			else:
				messages.error(request, TextMessage.QUESTION_ERROR_EDIT)
		else:
			form_question = QuestionForm(instance=question, prefix='question')
			forms_items = [ItemForm(instance=i, prefix=index + 1) for index, i in enumerate(question.get_items())]
		return render(request, "askmath/manager/question/manager_form_question.html",
					  {'request': request, 'form_question': form_question, 'forms_items': forms_items,
					   'question': question, 'lesson': lesson, 'discipline': discipline,
					   'title_form': _('Edit Question')})

	def restore_question(self, request, question, lesson, discipline):
		question.restore()
		messages.success(request, TextMessage.QUESTION_SUCCESS_RESTORE)
		return HttpResponseRedirect(reverse('askmath:manager_question_view',
											kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))

	def sort_questions(self, request, lesson, discipline, new_order=None):
		questions = QuestionModel.objects.filter(exists=True, visible=True, lesson=lesson.id)
		if request.method == 'POST':
			try:
				for index, i in enumerate(new_order):
					QuestionModel.objects.filter(id=i).update(position=index + 1)
				messages.success(request, TextMessage.QUESTION_SUCCESS_SORT)
			except Exception, e:
				print e
				messages.error(request, TextMessage.QUESTION_ERROR_SORT)
		return render(request, "askmath/manager/question/manager_view_questions_sort.html",
					  {'request': request, 'questions': questions, 'lesson': lesson, 'discipline': discipline})

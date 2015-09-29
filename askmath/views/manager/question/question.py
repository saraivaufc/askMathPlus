from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models.lesson import Lesson as ContactModel
from askmath.models.question import Question as QuestionModel
from askmath.models.question import Item as ItemModel
from askmath.models.discipline import Discipline as CategoryModel
from askmath.entities import TextMessage
from django.contrib import messages
from .iquestion import IQuestion
from askmath.forms import QuestionForm, ItemForm
from django.utils.translation import ugettext_lazy as _

class Question(IQuestion):
	def choose_lesson(self, request):
		disciplines = []
		for discipline in CategoryModel.objects.filter(exists=True):
			if discipline.get_lessons():
				disciplines.append(discipline) 
		return render(request, "askmath/manager/question/manager_choose_lessons.html",
			{'request':request,'disciplines': disciplines})
	
	def view_questions(self, request, lesson):
		questions = lesson.get_questions()
		return render(request, "askmath/manager/question/manager_view_questions.html",
			{'request':request,'questions': questions, 'lesson': lesson})
	
	def view_questions_removed(self, request, lesson):
		questions = QuestionModel.objects.filter(exists=False,lesson = lesson.id)
		return render(request, "askmath/manager/question/manager_view_questions.html",
			{'request':request,'questions': questions, 'lesson': lesson,'is_removed': True})
	
	def view_question(self, request, lesson, question):
		return render(request, "askmath/manager/question/manager_view_question.html", 
			{'request':request,'lesson': lesson,'question': question })
	
	
	
	def add_question(self, request, lesson, quantity_items=5):
		if request.method == "POST":
			request.POST = request.POST.copy()
			request.POST['question-lesson'] = lesson.id
			
			forms_items =  [ ItemForm(request.POST, prefix=i) for i in range(1, quantity_items+1)]
			list_items=[]
			for index, i in enumerate(forms_items):
				if i.is_valid():
					new_item = i.save()
					ItemModel.objects.filter(id= new_item.id).update(position = index +1)
					list_items.append(new_item.pk)
			
			try:
				positions = map(lambda x: x.position, lesson.get_questions())
			except Exception, e:
				print e
				positions = [0]
			if not positions:
				positions = [0]
			request.POST['question-items']= list_items
			request.POST['question-position']= max(positions)+1
			form_question = QuestionForm(request.POST, prefix='question')
			if form_question.is_valid():
				question = form_question.save()
				messages.error(request,TextMessage.QUESTION_SUCCESS_ADD)
				return self.view_question(request, lesson, question)
			else:
				messages.error(request,TextMessage.ERROR_FORM)
		else:
			form_question = QuestionForm(prefix='question')
			forms_items = [ ItemForm(prefix=i) for i in range(1, quantity_items+1)]
		return render(request, "askmath/manager/question/manager_form_question.html", 
			{'request':request,'form_question': form_question,'lesson': lesson,'forms_items': forms_items ,'lesson': lesson, 'title_form':_('Create Question')})
	
	def remove_question(self, request, lesson,question):
		question.delete()
		messages.error(request,TextMessage.QUESTION_SUCCESS_REM)
		return self.view_questions(request, lesson)
	
	def edit_question(self, request, lesson, question):
		if request.method == "POST":
			request.POST = request.POST.copy()
			request.POST['question-lesson'] = lesson.id
			
			forms_items = forms_items = [ ItemForm(request.POST,instance=i , prefix=index+1) for index, i in enumerate(question.get_items())]
			list_items = []
			for i in forms_items:
				if i.is_valid():
					new_item = i.save()
					list_items.append(new_item.pk)
			request.POST['question-items']= list_items
			form_question = QuestionForm(request.POST, instance=question, prefix='question')
			if form_question.is_valid():
				question = form_question.save()
				messages.error(request,TextMessage.QUESTION_SUCCESS_EDIT)
				return self.view_question(request, lesson, question)
			else:
				messages.error(request,TextMessage.QUESTION_ERROR_EDIT)
		else:
			form_question = QuestionForm(instance=question, prefix='question')
			forms_items = [ ItemForm(instance=i, prefix=index+1) for index, i in enumerate(question.get_items())]
		return render(request, "askmath/manager/question/manager_form_question.html", 
			{'request':request,'form_question': form_question,'forms_items': forms_items ,'lesson': lesson,'question':question, 'title_form':_('Edit Question')})
	
	
	def restore_question(self, request, lesson, question):
		question.restore()
		messages.error(request,TextMessage.QUESTION_SUCCESS_RESTORE)
		return self.view_questions(request, lesson)
	
	def sort_questions(self, request, lesson,new_order=None=None):
		questions = QuestionModel.objects.filter(exists=True, visible=True,lesson = lesson.id)
		if request.method == 'POST':    
			try:
				for index, i in enumerate(new_order):
					QuestionModel.objects.filter(id = i).update(position = index + 1)
				messages.error(request,TextMessage.QUESTION_SUCCESS_SORT)
				request.method = "GET"
				return self.sort_questions(request, lesson, None)
			except Exception, e:
				print e
				messages.error(request,TextMessage.QUESTION_ERROR_SORT)
		return render(request, "askmath/manager/question/manager_view_questions_sort.html",
			{'request':request,'questions': questions, 'lesson': lesson})
	
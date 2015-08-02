from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models.lesson import Lesson as LessonModel
from askmath.models.question import Question as QuestionModel
from askmath.models.question import Item as ItemModel
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.entities import Message, TextMessage, TypeMessage
from .iquestion import IQuestion
from askMathPlus.settings import COLORS_ALL
from askmath.forms import QuestionForm, ItemForm
from django.utils.translation import ugettext_lazy as _

class Question(IQuestion):
    def choose_lesson(self, request, message = None):
        disciplines = []
        for discipline in DisciplineModel.objects.filter(exists=True):
            if discipline.get_lessons():
                disciplines.append(discipline) 
        return render(request, "askmath/manager/question/manager_choose_lessons.html",
            {'request':request,'disciplines': disciplines, 'colors': COLORS_ALL, 'message': message})
    
    def view_questions(self, request, lesson, message = None):
        questions = lesson.get_questions()
        return render(request, "askmath/manager/question/manager_view_questions.html",
            {'request':request,'questions': questions, 'lesson': lesson, 'colors': COLORS_ALL, 'message': message})
    
    def view_questions_removed(self, request, lesson, message = None):
        questions = QuestionModel.objects.filter(exists=False,lesson = lesson.id)
        return render(request, "askmath/manager/question/manager_view_questions.html",
            {'request':request,'questions': questions, 'lesson': lesson,'is_removed': True, 'colors': COLORS_ALL, 'message': message})
    
    def view_question(self, request, lesson, question, message = None):
        return render(request, "askmath/manager/question/manager_view_question.html", 
            {'request':request,'lesson': lesson,'question': question , 'message': message, 'colors': COLORS_ALL })
    
    
    
    def add_question(self, request, lesson, quantity_items=5, message = None):
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
            except:
                positions = [0]
            if not positions:
                positions = [0]
            request.POST['question-items']= list_items
            request.POST['question-position']= max(positions)+1
            form_question = QuestionForm(request.POST, prefix='question')
            if form_question.is_valid():
                question = form_question.save()
                message = Message(TextMessage.QUESTION_SUCCESS_ADD, TypeMessage.SUCCESS)
                return self.view_question(request, lesson, question, message)
        else:
            form_question = QuestionForm(prefix='question')
            forms_items = [ ItemForm(prefix=i) for i in range(1, quantity_items+1)]
        return render(request, "askmath/manager/question/manager_form_question.html", 
            {'request':request,'form_question': form_question,'forms_items': forms_items ,'lesson': lesson, 'title_form':_('Create Question'), 'message': message})
    
    def remove_question(self, request, lesson,question,  message = None):
        question.delete()
        message = Message(TextMessage.QUESTION_SUCCESS_REM, TypeMessage.SUCCESS)
        return self.view_questions(request, lesson, message)
    
    def edit_question(self, request, lesson, question,  message = None):
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
                message = Message(TextMessage.QUESTION_SUCCESS_EDIT, TypeMessage.SUCCESS)
                return self.view_question(request, lesson, question, message)
        else:
            form_question = QuestionForm(instance=question, prefix='question')
            forms_items = [ ItemForm(instance=i, prefix=index+1) for index, i in enumerate(question.get_items())]
        return render(request, "askmath/manager/question/manager_form_question.html", 
            {'request':request,'form_question': form_question,'forms_items': forms_items ,'lesson': lesson, 'title_form':_('Edit Question'), 'message': message})
    
    
    def restore_question(self, request, lesson, question):
        question.restore()
        message = Message(TextMessage.QUESTION_SUCCESS_RESTORE, TypeMessage.SUCCESS)
        return self.view_questions(request, lesson, message)
    
    def sort_questions(self, request, lesson,new_order=None, message=None):
        questions = QuestionModel.objects.filter(exists=True, visible=True,lesson = lesson.id)
        if request.method == 'POST':    
            try:
                for index, i in enumerate(new_order):
                    QuestionModel.objects.filter(id = i).update(position = index + 1)
                message = Message(TextMessage.QUESTION_SUCCESS_SORT, TypeMessage.SUCCESS)
                request.method = "GET"
                return self.sort_questions(request, lesson, None, message)
            except:
                message = Message(TextMessage.QUESTION_ERROR_SORT, TypeMessage.ERROR)
        return render(request, "askmath/manager/question/manager_view_questions_sort.html",
            {'request':request,'questions': questions, 'lesson': lesson, 'colors': COLORS_ALL, 'message': message})
    
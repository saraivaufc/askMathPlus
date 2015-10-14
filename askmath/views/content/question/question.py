from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import TextMessage
from django.contrib import messages

#MODELS
from askmath.models.discipline import Discipline as CategoryModel
from askmath.models.lesson import Lesson as ContactModel
from askmath.models.question import Question as QuestionModel
from askmath.models.question import Item as ItemModel
from askmath.models.users import Student as StudentModel

from askmath.models.experience import StudentExperience
from askmath.models.state import StudentLessonState

from .iquestion import IQuestion
from django.utils.translation import ugettext_lazy as _
from askmath.entities import ExperienceLevel
from askmath.views.index import ProxyHome


class Question(IQuestion):
    def __init__(self):
        self.__proxy_home = ProxyHome()
    
    def view_initial_details(self, request, discipline, lesson):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except Exception, e:
            print e
            messages.error(request, TextMessage.USER_NOT_FOUND)
            return self.__proxy_home.index(request)
        
        try:
            studentexperience = StudentExperience.objects.get(student = student, exists=True)
        except Exception, e:
            print e
            try:
                studentexperience = StudentExperience(student = student)
                studentexperience.save()
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
                return self.__proxy_home.index(request)  
        
        experience_level = ExperienceLevel(studentexperience.level)
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except Exception, e:
            print e
            studentlessonstate = StudentLessonState(student = student,discipline = discipline,lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
            
        
        studentlessonstate.update()
            
        return render(request, "askmath/content/question/view_initial_details.html",
            {'request': request, 'discipline': discipline, 'lesson': lesson,
             'experience_level': experience_level, 'studentlessonstate': studentlessonstate,'studentexperience': studentexperience})
    
    
    def view_question(self, request, discipline, lesson, question=None):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except Exception, e:
            print e
            messages.error(request, TextMessage.USER_NOT_FOUND)
            return self.view_initial_details(request, discipline, lesson)
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except Exception, e:
            print e
            studentlessonstate = StudentLessonState(student = student,discipline = discipline,lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
        
        studentlessonstate.update()
        
        if not question:
            question = studentlessonstate.get_question()
        
        if not question:
            # Licao Concluida
            messages.success(request, TextMessage.LESSON_SUCCESS_COMPLETED)
            return self.view_initial_details(request, discipline, lesson)
        
        return render(request, "askmath/content/question/view_question.html",
            {'request': request, 'discipline': discipline, 'lesson': lesson,
             'studentlessonstate': studentlessonstate,'question': question})
    
    def answer_question(self,request, discipline, lesson, question, items):
        if request.method == 'POST':
            try:
                student = StudentModel.objects.get(id = request.user.id)
            except Exception, e:
                print e
                messages.error(request, TextMessage.USER_NOT_FOUND)
                return self.view_initial_details(request, discipline, lesson)
            try:
                studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
            except Exception, e:
                print e
                studentlessonstate = StudentLessonState(student = student,discipline = discipline,lesson = lesson, remaining_jump=lesson.get_maximum_hops())
                studentlessonstate.save()
            try:
                studentlessonstate.answer_question(request, question, items)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.METHOD_NOT_POST)
        return self.view_question(request, discipline, lesson, None)
    
    def jump_question(self,request, discipline, lesson, question):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except Exception, e:
            print e
            messages.error(request, TextMessage.USER_NOT_FOUND)
            return self.view_question(request, discipline, lesson,None)
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except Exception, e:
            print e
            studentlessonstate = StudentLessonState(student = student,discipline = discipline, lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
        if studentlessonstate.get_remaining_jump():
            try:
                studentlessonstate.add_skipped_question(request, question)
            except Exception, e:
                print e
                messages.warning(request, TextMessage.QUESTION_ERROR_JUMP)
        else:
            messages.warning(request, TextMessage.LESSON_NOT_REMAINING_JUMPS)
        return self.view_question(request, discipline, lesson,None)
    
    def choose_skipped_question(self,request, discipline, lesson, question):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except Exception, e:
            print e
            messages.error(request, TextMessage.USER_NOT_FOUND)
            return self.view_question(request, discipline, lesson,None)
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except Exception, e:
            print e
            studentlessonstate = StudentLessonState(student = student,discipline = discipline, lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
        
        studentlessonstate.remove_skipped_question(question)
        
        return self.view_question(request, discipline, lesson,question)
    
    def reset_lesson(self,request, discipline, lesson):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except Exception, e:
            print e
            messages.error(request, TextMessage.USER_NOT_FOUND)
            return self.view_initial_details(request, discipline, lesson)    
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except Exception, e:
            print e
            studentlessonstate = StudentLessonState(student = student,discipline = discipline, lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
        
        studentexperience = StudentExperience.objects.get_or_create(student = student, exists=True)[0]
        
        studentlessonstate.delete()
        messages.success(request, TextMessage.LESSON_SUCCESS_RESET)
        studentexperience.down_scores(studentexperience.get_scores()/2)
        return self.view_initial_details(request, discipline, lesson)
    
    def help_quetion(self,request, discipline, lesson, question):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except Exception, e:
            print e
            messages.error(request, TextMessage.USER_NOT_FOUND)
            return self.view_question(request, discipline, lesson,None)
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except Exception, e:
            print e
            studentlessonstate = StudentLessonState(student = student,discipline = discipline, lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
        
        try:
            studentlessonstate.add_help_question(question)
        except Exception, e:
            print e
            return HttpResponse("False")
        return HttpResponse("True")
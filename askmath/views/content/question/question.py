from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.entities import Message, TextMessage, TypeMessage

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
    
    def view_initial_details(self, request, discipline, lesson, message=None):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except:
            message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
            return self.__proxy_home.index(request, message)
        
        try:
            studentexperience = StudentExperience.objects.get(student = student, exists=True)
        except:
            try:
                studentexperience = StudentExperience(student = student)
                studentexperience.save()
            except:
                message = Message(TextMessage.ERROR, TypeMessage.ERROR)
                return self.__proxy_home.index(request, message)  
        
        experience_level = ExperienceLevel(studentexperience.level)
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except:
            studentlessonstate = StudentLessonState(student = student,discipline = discipline,lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
            
        
        studentlessonstate.update()
            
        return render(request, "askmath/content/question/view_initial_details.html",
            {'request': request, 'discipline': discipline, 'lesson': lesson,
             'experience_level': experience_level, 'studentlessonstate': studentlessonstate,'studentexperience': studentexperience,  'message': message})
    
    
    def view_question(self, request, discipline, lesson, question=None, message=None):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except:
            message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
            return self.__proxy_home.index(request, message)
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except:
            studentlessonstate = StudentLessonState(student = student,discipline = discipline,lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
        
        studentlessonstate.update()
        
        if not question:
            question = studentlessonstate.get_question()
        
        if not question:
            # Licao Concluida
            message = Message(TextMessage.LESSON_SUCCESS_COMPLETED, TypeMessage.SUCCESS)
            return self.view_initial_details(request, discipline, lesson, message)
        
            
        return render(request, "askmath/content/question/view_question.html",
            {'request': request, 'discipline': discipline, 'lesson': lesson,
             'studentlessonstate': studentlessonstate,'question': question, 'message': message})
    
    def answer_question(self,request, discipline, lesson, question, items, message=None):
        if request.method == 'POST':
            try:
                student = StudentModel.objects.get(id = request.user.id)
            except:
                message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
                return self.view_initial_details(request, discipline, lesson, message)
            
            try:
                studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
            except:
                studentlessonstate = StudentLessonState(student = student,discipline = discipline,lesson = lesson, remaining_jump=lesson.get_maximum_hops())
                studentlessonstate.save()
            try:
                message = studentlessonstate.answer_question(question, items)
            except:
                message =  Message(TextMessage.ERROR, TypeMessage.ERROR)
        else:
            message = Message(TextMessage.METHOD_NOT_POST, TypeMessage.ERROR)
        return self.view_question(request, discipline, lesson, None, message)
    
    def jump_question(self,request, discipline, lesson, question,message=None):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except:
            message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
            return self.view_question(request, discipline, lesson,None, message)
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except:
            studentlessonstate = StudentLessonState(student = student,discipline = discipline, lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
        if studentlessonstate.get_remaining_jump():
            try:
                message = studentlessonstate.add_skipped_question(question)
            except:
                message = Message(TextMessage.QUESTION_ERROR_JUMP, TypeMessage.WARNING)
        else:
            message = Message(TextMessage.LESSON_NOT_REMAINING_JUMPS, TypeMessage.WARNING)
        return self.view_question(request, discipline, lesson,None, message)
    
    def choose_skipped_question(self,request, discipline, lesson, question,message=None):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except:
            message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
            return self.view_question(request, discipline, lesson,None, message)
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except:
            studentlessonstate = StudentLessonState(student = student,discipline = discipline, lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
            
        studentlessonstate.remove_skipped_question(question)
        return self.view_question(request, discipline, lesson,question, message)
    
    def reset_lesson(self,request, discipline, lesson,message=None):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except:
            message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
            return self.view_initial_details(request, discipline, lesson, message)    
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except:
            studentlessonstate = StudentLessonState(student = student,discipline = discipline, lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
        
        studentexperience = StudentExperience.objects.get_or_create(student = student, exists=True)[0]
        
        studentlessonstate.delete()
        message = Message(TextMessage.LESSON_SUCCESS_RESET, TypeMessage.SUCCESS)
        studentexperience.down_scores(studentexperience.get_scores()/2)
        return self.view_initial_details(request, discipline, lesson, message)
    
    def help_quetion(self,request, discipline, lesson, question,message=None):
        try:
            student = StudentModel.objects.get(id = request.user.id)
        except:
            message = Message(TextMessage.USER_NOT_FOUND, TypeMessage.ERROR)
            return self.view_question(request, discipline, lesson,None, message)
        
        try:
            studentlessonstate = StudentLessonState.objects.get(student = student,discipline = discipline, lesson = lesson, exists=True)
        except:
            studentlessonstate = StudentLessonState(student = student,discipline = discipline, lesson = lesson, remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()
        
        try:
            studentlessonstate.add_help_question(question)
        except:
            return HttpResponse("False")
        return HttpResponse("True")
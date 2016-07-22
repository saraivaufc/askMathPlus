import json
from askmath.entities import TextMessage
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from askmath.models.question import Question as QuestionModel
from askmath.views.index import ProxyHome
from askmath.views.manager.lesson import ProxyLesson
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .iquestion import IQuestion
from .question import Question


class ProxyQuestion(IQuestion):
    def __init__(self):
        self.__question = Question()
        self.__proxy_home = ProxyHome()
        self.__proxy_lesson = ProxyLesson()

    @method_decorator(login_required)
    def view_questions(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.__proxy_lesson.view_lessons(request, id_discipline)
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.__proxy_lesson.view_lessons(request, id_discipline)

            try:
                return self.__question.view_questions(request, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.__proxy_lesson.view_lessons(request, id_discipline)

    @method_decorator(login_required)
    def view_questions_removed(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                return self.__question.view_questions_removed(request, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_questions(request, id_lesson, id_discipline)

    @method_decorator(login_required)
    def add_question(self, request, id_lesson, id_discipline, quantity_items=5):
        if request.user.has_perm("askmath.write_question") and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                return self.__question.add_question(request, lesson, discipline, int(quantity_items))
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_questions(request, id_lesson, id_discipline)

    @method_decorator(login_required)
    def remove_question(self, request, id_question, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_question") and request.user.has_perm("askmath.access_manager"):

            try:
                question = QuestionModel.objects.get(id=id_question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                return self.__question.remove_question(request, question, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_questions(request, id_lesson, id_discipline)

    @method_decorator(login_required)
    def edit_question(self, request, id_question, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_question") and request.user.has_perm("askmath.access_manager"):
            try:
                question = QuestionModel.objects.get(id=id_question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                return self.__question.edit_question(request, question, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_ERROR_EDIT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_questions(request, id_lesson, id_discipline)

    @method_decorator(login_required)
    def restore_question(self, request, id_question, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_question") and request.user.has_perm("askmath.access_manager"):
            try:
                question = QuestionModel.objects.get(id=id_question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                return self.__question.restore_question(request, question, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return self.view_questions(request, id_lesson, id_discipline)

    @method_decorator(login_required)
    def sort_questions(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_manager"):
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return self.view_questions(request, id_lesson, id_discipline)

            try:
                if request.method == "POST":
                    new_order = json.loads(request.POST['new_order'])
                    return self.__question.sort_questions(request, lesson, discipline, new_order)
                else:
                    return self.__question.sort_questions(request, lesson, discipline, None)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_ERROR_SORT)
        return self.view_questions(request, id_lesson, id_discipline)

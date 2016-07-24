import json
from askmath.entities import TextMessage
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from askmath.models.question import Question as QuestionModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from .iquestion import IQuestion
from .question import Question


class ProxyQuestion(IQuestion):
    def __init__(self):
        self.__question = Question()

    @method_decorator(login_required)
    def view_questions(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))
            try:
                return self.__question.view_questions(request, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))

    @method_decorator(login_required)
    def view_questions_removed(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))
            try:
                return self.__question.view_questions_removed(request, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(
            reverse('askmath:manager_question_view', kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

    @method_decorator(login_required)
    def add_question(self, request, id_lesson, id_discipline, quantity_items=5):
        if request.user.has_perm("askmath.write_question") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))
            try:
                return self.__question.add_question(request, lesson, discipline, int(quantity_items))
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_ERROR_ADD)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(
            reverse('askmath:manager_question_view', kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

    @method_decorator(login_required)
    def remove_question(self, request, id_question, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_question") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))
            try:
                question = QuestionModel.objects.get(id=id_question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_question_view',
                            kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))
            try:
                return self.__question.remove_question(request, question, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_ERROR_REM)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect( reverse('askmath:manager_question_view', kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

    @method_decorator(login_required)
    def edit_question(self, request, id_question, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_question") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))
            try:
                question = QuestionModel.objects.get(id=id_question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_question_view',
                            kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

            try:
                return self.__question.edit_question(request, question, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_ERROR_EDIT)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_question_view',
                                                kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

    @method_decorator(login_required)
    def restore_question(self, request, id_question, id_lesson, id_discipline):
        if request.user.has_perm("askmath.write_question") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))
            try:
                question = QuestionModel.objects.get(id=id_question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_question_view',
                            kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))
            try:
                return self.__question.restore_question(request, question, lesson, discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_ERROR_RESTORE)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:manager_question_view',
                                            kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

    @method_decorator(login_required)
    def sort_questions(self, request, id_lesson, id_discipline):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_manager"):
            try:
                discipline = DisciplineModel.objects.get(id=id_discipline)
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:manager_discipline_view'))
            try:
                lesson = LessonModel.objects.get(id=id_lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:manager_lesson_view', kwargs={'id_discipline': id_discipline}))
            try:
                if request.method == "POST":
                    new_order = json.loads(request.POST['new_order'])
                    return self.__question.sort_questions(request, lesson, discipline, new_order)
                else:
                    return self.__question.sort_questions(request, lesson, discipline, None)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_ERROR_SORT)

        return HttpResponseRedirect(reverse('askmath:manager_question_view',
                                            kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))
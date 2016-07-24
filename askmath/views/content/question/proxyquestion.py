from askmath.entities import TextMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

# MODELS
from askmath.models.discipline import Discipline as DisciplineModel
from askmath.models.lesson import Lesson as LessonModel
from askmath.models.question import Question as QuestionModel
from askmath.models.question import Item as ItemModel

from .iquestion import IQuestion
from .question import Question


class ProxyQuestion(IQuestion):
    def __init__(self):
        self.__question = Question()

    @method_decorator(login_required)
    def view_question(self, request, id_discipline, id_lesson, id_question=None):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_content"):
            try:
                discipline = DisciplineModel.objects.filter(id=id_discipline, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:content_discipline_view'))
            try:
                lesson = LessonModel.objects.filter(id=id_lesson, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:content_discipline_view', kwargs={'id_discipline': id_discipline}))
            if id_question:
                try:
                    question = QuestionModel.objects.filter(id=id_question, exists=True, visible=True)[0]
                except Exception, e:
                    print e
                    messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                    return HttpResponseRedirect(reverse('askmath:content_lesson_view',
                                                        kwargs={'id_discipline': id_discipline,
                                                                'id_lesson': id_lesson}))
            else:
                question = None
            try:
                return self.__question.view_question(request, discipline, lesson, question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return HttpResponseRedirect(
            reverse('askmath:content_lesson_view', kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

    @method_decorator(login_required)
    def answer_question(self, request, id_discipline, id_lesson, id_question):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_content"):
            try:
                discipline = DisciplineModel.objects.filter(id=id_discipline, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:content_discipline_view'))
            try:
                lesson = LessonModel.objects.filter(id=id_lesson, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:content_discipline_view', kwargs={'id_discipline': id_discipline}))
            try:
                question = QuestionModel.objects.filter(id=id_question, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:content_lesson_view',
                            kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))
            try:
                item = ItemModel.objects.get(id=int(request.POST['item']))
            except Exception, e:
                print e
                messages.error(request, TextMessage.ITEM_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:content_lesson_view',
                                                    kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))
            try:
                return self.__question.answer_question(request, discipline, lesson, question, item)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)
        return HttpResponseRedirect(reverse('askmath:content_question_view',
                                            kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

    @method_decorator(login_required)
    def jump_question(self, request, id_discipline, id_lesson, id_question):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_content"):
            try:
                discipline = DisciplineModel.objects.filter(id=id_discipline, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:content_discipline_view'))
            try:
                lesson = LessonModel.objects.filter(id=id_lesson, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:content_discipline_view', kwargs={'id_discipline': id_discipline}))
            try:
                question = QuestionModel.objects.get(id=id_question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:content_lesson_view',
                                                    kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))
            try:
                return self.__question.jump_question(request, discipline, lesson, question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:content_question_view',
                                            kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

    @method_decorator(login_required)
    def choose_skipped_question(self, request, id_discipline, id_lesson, id_question):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_content"):
            try:
                discipline = DisciplineModel.objects.filter(id=id_discipline, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:content_discipline_view'))
            try:
                lesson = LessonModel.objects.filter(id=id_lesson, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:content_discipline_view', kwargs={'id_discipline': id_discipline}))
            try:
                question = QuestionModel.objects.filter(id=id_question, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:content_lesson_view',
                                                    kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))
            try:
                return self.__question.choose_skipped_question(request, discipline, lesson, question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:content_question_view',
                                            kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

    @method_decorator(login_required)
    def reset_lesson(self, request, id_discipline, id_lesson):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_content"):
            try:
                discipline = DisciplineModel.objects.filter(id=id_discipline, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:content_discipline_view'))
            try:
                lesson = LessonModel.objects.filter(id=id_lesson, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:content_discipline_view', kwargs={'id_discipline': id_discipline}))
            try:
                return self.__question.reset_lesson(request, discipline, lesson)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:content_question_view',
                                            kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

    @method_decorator(login_required)
    def help_question(self, request, id_discipline, id_lesson, id_question):
        if request.user.has_perm("askmath.read_question") and request.user.has_perm("askmath.access_content"):
            try:
                discipline = DisciplineModel.objects.filter(id=id_discipline, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.DISCIPLINE_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:content_discipline_view'))
            try:
                lesson = LessonModel.objects.filter(id=id_lesson, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.LESSON_NOT_FOUND)
                return HttpResponseRedirect(
                    reverse('askmath:content_discipline_view', kwargs={'id_discipline': id_discipline}))
            try:
                question = QuestionModel.objects.filter(id=id_question, exists=True, visible=True)[0]
            except Exception, e:
                print e
                messages.error(request, TextMessage.QUESTION_NOT_FOUND)
                return HttpResponseRedirect(reverse('askmath:content_lesson_view',
                                                    kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))
            try:
                return self.__question.help_quetion(request, discipline, lesson, question)
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
        else:
            messages.error(request, TextMessage.USER_NOT_PERMISSION)

        return HttpResponseRedirect(reverse('askmath:content_question_view',
                                            kwargs={'id_discipline': id_discipline, 'id_lesson': id_lesson}))

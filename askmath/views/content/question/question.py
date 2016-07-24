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


class Question(IQuestion):
    def view_question(self, request, discipline, lesson, question=None, definitive=False):
        try:
            student = StudentModel.objects.get(id=request.user.id)
        except Exception, e:
            print e
            messages.error(request, TextMessage.USER_NOT_FOUND)
            return HttpResponseRedirect(
                reverse('askmath:content_lesson_view', kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))

        try:
            studentexperience = StudentExperience.objects.get(student=student, exists=True)
        except Exception, e:
            print e
            try:
                studentexperience = StudentExperience(student=student)
                studentexperience.save()
            except Exception, e:
                print e
                messages.error(request, TextMessage.ERROR)
                return HttpResponseRedirect(reverse('askmath:content_question_view',
                                                    kwargs={'id_discipline': discipline.id, 'id_lesson': lesson.id}))

        experience_level = ExperienceLevel(studentexperience.level)

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

        return render(request, "askmath/content/question/view_question.html",
                      {'request': request, 'discipline': discipline, 'lesson': lesson,
                       'studentlessonstate': studentlessonstate, 'lesson_complete': lesson_complete,
                       'experience_level': experience_level, 'question': question})

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
            studentlessonstate = StudentLessonState.objects.get(student=student, discipline=discipline, lesson=lesson,
                                                                exists=True)
        except Exception, e:
            print e
            studentlessonstate = StudentLessonState(student=student, discipline=discipline, lesson=lesson,
                                                    remaining_jump=lesson.get_maximum_hops())
            studentlessonstate.save()

        studentexperience = StudentExperience.objects.get_or_create(student=student, exists=True)[0]

        studentlessonstate.delete()
        messages.success(request, TextMessage.LESSON_SUCCESS_RESET)
        studentexperience.down_scores(studentexperience.get_scores() / 2)
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

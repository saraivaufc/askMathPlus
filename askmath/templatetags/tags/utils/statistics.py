# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from askmath.views.manager.statistic.lesson.generatestatistics import GeneratorStatistics as GeneratorStatisticsLesson
from .. import register

@register.filter(name='acerts_question')
def acerts_question(question):
    generate_statistics_lesson = GeneratorStatisticsLesson()
    return generate_statistics_lesson.get_acerts_question(question)

@register.filter(name='errors_question') 
def errors_question(question):
    generate_statistics_lesson = GeneratorStatisticsLesson()
    return generate_statistics_lesson.get_errors_question(question)

@register.filter(name='skippeds_question') 
def skippeds_question(question):
    generate_statistics_lesson = GeneratorStatisticsLesson()
    return generate_statistics_lesson.get_skippeds_question(question)

@register.filter(name='helps_question') 
def helps_question(question):
    generate_statistics_lesson = GeneratorStatisticsLesson()
    return generate_statistics_lesson.get_helps_question(question)


@register.filter(name='percentage_answered_questions') 
def percentage_answered_questions(lesson):
    generate_statistics_lesson = GeneratorStatisticsLesson()
    return generate_statistics_lesson.get_percentage_answered_questions(lesson)

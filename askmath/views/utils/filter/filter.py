# -*- encoding=UTF-8 -*-

from multiprocessing.pool import ThreadPool

import nltk
import os
from askMathPlus.settings import BASE_DIR
from askMathPlus.settings import COLORS_ALL
from askmath.models import Discipline, Lesson, Video
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from nltk.corpus import stopwords
from .ifilter import IFilter

nltk.data.path.append(os.path.join(BASE_DIR, 'askmath/static/askmath/filter/nltk_data/'))

LANGUAGE = "portuguese"
IGNORED_WORDS = stopwords.words(LANGUAGE)


class Filter(IFilter):
    def search(self, request, expression):
        disciplines = Discipline.objects.filter(exists=True, visible=True)
        lessons = Lesson.objects.filter(exists=True, visible=True)
        videos = Video.objects.filter(exists=True, visible=True)

        pool = ThreadPool(processes=3)

        p_disciplines = pool.apply_async(self.search_disciplines, (request, expression, disciplines))
        p_lessons = pool.apply_async(self.search_lessons, (request, expression, lessons))
        p_videos = pool.apply_async(self.search_videos, (request, expression, videos))

        disciplines_occurrences = p_disciplines.get()
        lessons_occurrences = p_lessons.get()
        videos_occurrences = p_videos.get()

        if type(disciplines_occurrences) == HttpResponseRedirect:
            return disciplines_occurrences
        if type(lessons_occurrences) == HttpResponseRedirect:
            return lessons_occurrences
        if type(videos_occurrences) == HttpResponseRedirect:
            return videos_occurrences
        return render(request, "askmath/utils/filter/search.html",
                      {'request': request, 'expression': expression,
                       'disciplines_occurrences': disciplines_occurrences[:5],
                       'lessons_occurrences': lessons_occurrences[:5], 'videos_occurrences': videos_occurrences[:5],
                       'colors': COLORS_ALL})

    def search_disciplines(self, request, expression, disciplines):
        disciplines_occurrences = {}
        for discipline in disciplines:
            discipline_title = (discipline.get_title()).upper()
            expression = expression.upper()

            if discipline_title == expression:
                if request.user.is_authenticated():
                    return HttpResponseRedirect(
                        reverse('askmath:content_discipline_view', kwargs={'id_discipline': discipline.id}))
            else:
                occurrences = self.occurrences(discipline_title, expression)
                if occurrences > 0:
                    disciplines_occurrences[discipline] = occurrences
            del discipline
            del occurrences

        disciplines_occurrences = sorted(disciplines_occurrences.items(), key=lambda x: x[1], reverse=True)
        return disciplines_occurrences

    def search_lessons(self, request, expression, lessons):
        lessons_occurrences = {}
        for lesson in lessons:
            lesson_title = (lesson.get_title()).upper()
            expression = expression.upper()
            if lesson_title == expression:
                if request.user.is_authenticated():
                    return HttpResponseRedirect(reverse('askmath:content_lesson_view',
                                                        kwargs={'id_discipline': lesson.get_discipline().id,
                                                                'id_lesson': lesson.id}))
            else:
                occurrences = 0
                for title in lesson_title.split(" "):
                    if len(title) > 2:
                        occurrences += self.occurrences(title, expression)
                if occurrences > 0:
                    lessons_occurrences[lesson] = occurrences

        lessons_occurrences = sorted(lessons_occurrences.items(), key=lambda x: x[1], reverse=True)
        return lessons_occurrences

    def search_videos(self, request, expression, videos):
        videos_occurrences = {}
        for video in videos:
            video_title = (video.get_title()).upper()
            expression = expression.upper()
            if video_title == expression:
                if request.user.is_authenticated():
                    return HttpResponseRedirect(reverse('askmath:content_video_view',
                                                        kwargs={'id_discipline': lesson.get_discipline().id,
                                                                'id_lesson': lesson.id, 'id_video': video.id}))
            else:
                occurrences = self.occurrences(video_title, expression)
                if occurrences > 0:
                    videos_occurrences[video] = occurrences
        videos_occurrences = sorted(videos_occurrences.items(), key=lambda x: x[1], reverse=True)
        return videos_occurrences

    def occurrences(self, text="", expression=""):
        text = self.expression_clean(text).encode('utf-8')
        expression = self.expression_clean(expression).split(" ")
        occurrences_count = 0
        for i in expression:
            try:
                if len(i) > 2 and len(text) > 2:
                    occurrences_count += len(self.string_matching(unicode(text), unicode(i)))
            except Exception, e:
                print e
        return occurrences_count

    def expression_clean(self, expression=""):
        expression = [i for i in expression.split(" ") if i not in IGNORED_WORDS]
        return ' '.join(unicode(e) for e in expression)

    def string_matching(self, text='', pattern=''):
        m = len(pattern)
        n = len(text)
        offsets = []
        if m > n:
            return offsets
        skip = []
        for k in range(256):
            skip.append(m)
        for k in range(m - 1):
            skip[ord(pattern[k])] = m - k - 1
        skip = tuple(skip)
        k = m - 1
        while k < n:
            j = m - 1;
            i = k
            while j >= 0 and text[i] == pattern[j]:
                j -= 1
                i -= 1
            if j == -1:
                offsets.append(i + 1)
            k += skip[ord(text[k])]
        return offsets

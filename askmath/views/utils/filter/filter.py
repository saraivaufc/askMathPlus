#-*- encoding=UTF-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Discipline, Lesson, Video
from askMathPlus.settings import BASE_DIR
from askMathPlus.settings import COLORS_ALL
from multiprocessing.pool import ThreadPool

from .ifilter import IFilter
import nltk, os
nltk.data.path.append(os.path.join(BASE_DIR, 'askmath/static/askmath/filter/nltk_data/'))
from nltk.corpus import stopwords
import operator

from askmath.views.content.discipline import ProxyDiscipline
from askmath.views.content.lesson import ProxyLesson
from askmath.views.content.video import ProxyVideo

LANGUAGE = "portuguese"
IGNORED_WORDS = stopwords.words(LANGUAGE)

class Filter(IFilter):
    def __init__(self):
        self.__proxy_discipline = ProxyDiscipline()
        self.__proxy_lesson = ProxyLesson()
        self.__proxy_video = ProxyVideo()
    
    def search(self, request, expression , message=None):
        disciplines = Discipline.objects.filter(exists=True, visible=True)
        lessons = Lesson.objects.filter(exists=True, visible=True)
        videos = Video.objects.filter(exists=True, visible=True)
        
        pool = ThreadPool(processes=3)
        
        p_disciplines = pool.apply_async(self.search_disciplines, (request, expression, disciplines, message))
        p_lessons = pool.apply_async(self.search_lessons, (request, expression, lessons, message))
        p_videos = pool.apply_async(self.search_videos, (request, expression, videos, message))
        
        
        disciplines_occurrences = p_disciplines.get()
        lessons_occurrences = p_lessons.get()
        videos_occurrences = p_videos.get()
        
        return render(request, "askmath/utils/filter/search.html", 
            {'disciplines_occurrences': disciplines_occurrences[:5],'lessons_occurrences': lessons_occurrences[:5],'videos_occurrences': videos_occurrences[:5],'colors': COLORS_ALL, 'message': message})
    
    
    
    def search_disciplines(self, request,expression, disciplines, message=None):
        disciplines_occurrences = {}
        for discipline in disciplines:
            discipline_title = (discipline.get_title()).upper()
            expression = expression.upper()
            
            if  discipline_title == expression:
                if request.user.is_authenticated():
                    return self.__proxy_lesson.view_lessons(request, discipline.id, message)
            else:
                occurrences = self.occurrences(discipline_title, expression)
                if occurrences > 0:
                    disciplines_occurrences[discipline] = occurrences
            del discipline
            del occurrences
            
        disciplines_occurrences = sorted(disciplines_occurrences.items(), key=lambda x: x[1], reverse=True)
        print "disciplines"
        return disciplines_occurrences
    
    def search_lessons(self, request, expression, lessons, message=None):        
        lessons_occurrences = {}
        for lesson in lessons:
            lesson_title = (lesson.get_title()).upper() 
            expression = expression.upper()
            if lesson_title == expression:
                if request.user.is_authenticated():
                    return self.__proxy_lesson.view_lesson(request, None, lesson.id , message)
            else:
                occurrences = self.occurrences(lesson_title, expression)
                if occurrences > 0:
                    lessons_occurrences[lesson] = occurrences
                    
            del lesson
            del occurrences
        
        
        lessons_occurrences = sorted(lessons_occurrences.items(), key=lambda x: x[1], reverse=True)
        print 'lessons'
        return lessons_occurrences
    
    def search_videos(self, request, expression, videos, message=None):
        #SEARCH IN VIDEOS
        videos_occurrences = {}
        for video in videos:
            video_title = (video.get_title()).upper()
            expression = expression.upper()
            if video_title == expression:
                if request.user.is_authenticated():
                    return self.__proxy_video.view_video(request, video.id, None, None, message)
            else:
                occurrences = self.occurrences(video_title, expression)
                if occurrences > 0:
                    videos_occurrences[video] = occurrences
            del video
            del occurrences
        
        videos_occurrences = sorted(videos_occurrences.items(), key=lambda x: x[1], reverse=True)
        print 'videos'
        return videos_occurrences
    
                    
    def occurrences(self, text="", expression=""):
        text = self.expression_clean(text)
        expression = self.expression_clean(expression).split(" ")
        print "Text=",text," and Expression=",expression
        occurrences = 0
        for i in expression:
            try:
                if len(i) > 2 and len(text)>2:
                    occurrences += len(self.string_matching(text, i))
            except:
                pass
        return occurrences
        
    
    def expression_clean(self, expression=""):
        expression = [i for i in expression.split(" ") if i  not in IGNORED_WORDS]
        return  ' '.join(unicode(e) for e in expression)
    
    def string_matching(self, text='', pattern=''):
        m = len(pattern)
        n = len(text)
        offsets = []
        if m > n:
            return offsets
        skip = []
        for k in range(256):
            skip.append(m)
        for k in range(m-1):
            skip[ord(pattern[k])] = m - k - 1
        skip = tuple(skip)
        k = m - 1
        while k < n:
            j = m - 1; i = k
            while j >= 0 and text[i] == pattern[j]:
                j -= 1
                i -= 1
            if j == -1:
                offsets.append(i + 1)
            k += skip[ord(text[k])]
        return offsets

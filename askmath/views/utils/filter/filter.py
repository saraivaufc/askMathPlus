#-*- encoding=UTF-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Discipline, Lesson, Video
from askMathPlus.settings import BASE_DIR

from .ifilter import IFilter
import nltk, os
nltk.data.path.append(os.path.join(BASE_DIR, 'askmath/static/askmath/filter/nltk_data/'))
from nltk.corpus import stopwords

LANGUAGE = "portuguese"
IGNORED_WORDS = stopwords.words(LANGUAGE)

class Filter(IFilter):
    def search(self, request, expression , message=None):
        disciplines = Discipline.objects.filter(exists=True, visible=True)
        lessons = Lesson.objects.filter(exists=True, visible=True)
        videos = Video.objects.filter(exists=True, visible=True)
        return self.expression_clean(expression)
    
    def expression_clean(self, expression=""):
        expression = [i for i in expression.split(" ") if i  not in IGNORED_WORDS]
        return  HttpResponse(' '.join(unicode(e) for e in expression))
    
    def string_matching(self, text='', pattern=''):
        text = self.expression_clean(text)
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

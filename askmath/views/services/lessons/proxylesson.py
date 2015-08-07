from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from .ilesson import ILesson
from .lesson import Lesson

class ProxyLesson(ILesson):
    def __init__(self):
        self.__lesson = Lesson()
    def get(self, request):
        return self.__lesson.get(request)
        
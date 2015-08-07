from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from askmath.models import Lesson as LessonModel

from askmath.views.services.lessons.ilesson import ILesson

type_output = 'json'

class Lesson(ILesson):
    def get(self, request):
        lessons = serializers.serialize(type_output, LessonModel.objects.filter(exists=True, visible=True), fields=('id','title'))
        return HttpResponse(lessons)
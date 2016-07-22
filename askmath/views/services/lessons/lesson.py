from askmath.models import Lesson as ContactModel
from askmath.views.services.lessons.ilesson import ILesson
from django.core import serializers
from django.http import HttpResponse

type_output = 'json'

class Lesson(ILesson):
    def get(self, request):
        lessons = serializers.serialize(type_output, ContactModel.objects.filter(exists=True, visible=True), fields=('id','title'))
        return HttpResponse(lessons)
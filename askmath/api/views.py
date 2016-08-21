from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from askmath.models import Discipline, Lesson
from .serializers import DisciplineSerializer, LessonSerializer

class DisciplineList(APIView):
	"""
	List all topics, or create a new topic.
	"""
	def get(self, request, format=None):
		disciplines = Discipline.objects.filter(exists=True)
		serializer = DisciplineSerializer(disciplines, context={'request': request}, many=True)
		return Response(serializer.data)

class LessonList(APIView):
	"""
	List all topics, or create a new topic.
	"""
	def get(self, request, format=None):
		lessons = Lesson.objects.filter(exists=True)
		serializer = LessonSerializer(lessons, context={'request': request}, many=True)
		return Response(serializer.data)
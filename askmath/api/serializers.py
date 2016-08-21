from rest_framework import serializers
from askmath.models import Discipline, Lesson


class DisciplineSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Discipline
		fields = ('title', )

class LessonSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lesson
		fields = ('title', )

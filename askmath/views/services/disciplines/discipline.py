from askmath.models import Discipline as CategoryModel
from django.core import serializers
from django.http import HttpResponse
from .idiscipline import IDiscipline

type_output = 'json'


class Discipline(IDiscipline):
    def get(self, request):
        disciplines = serializers.serialize(type_output, CategoryModel.objects.filter(exists=True, visible=True),
                                            fields=('id', 'title'))
        return HttpResponse(disciplines)

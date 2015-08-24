from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from askmath.models import Discipline as DisciplineModel

from .idiscipline import IDiscipline

type_output = 'json'

class Discipline(IDiscipline):
    def get(self, request):
        disciplines = serializers.serialize(type_output, DisciplineModel.objects.filter(exists=True, visible=True), fields=('id','title'))
        return HttpResponse(disciplines)
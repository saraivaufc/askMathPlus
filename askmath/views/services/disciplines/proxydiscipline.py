from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from .idiscipline import IDiscipline
from .discipline import Discipline

class ProxyDiscipline(IDiscipline):
    def __init__(self):
        self.__discipline = Discipline()
    def get(self, request):
        return self.__discipline.get(request)
        
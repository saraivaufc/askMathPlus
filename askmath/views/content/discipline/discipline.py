from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Discipline as DisciplineModel
from askmath.entities import Message, TextMessage, TypeMessage
from idiscipline import IDiscipline
from askMathPlus.settings import COLORS_ALL
from django.utils.translation import ugettext_lazy as _

class Discipline(IDiscipline):
    def view_disciplines(self, request, message = None):
        disciplines = DisciplineModel.objects.filter(exists=True, visible=True)
        return render(request, "askmath/content/discipline/content_view_disciplines.html",
            {'request':request,'disciplines': disciplines, 'colors': COLORS_ALL, 'message': message})
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from askmath.models import Discipline as CategoryModel
from askmath.entities import Message, TextMessage, TypeMessage
from idiscipline import IDiscipline
from django.utils.translation import ugettext_lazy as _

class Discipline(IDiscipline):
    def view_disciplines(self, request, message = None):
        disciplines = CategoryModel.objects.filter(exists=True, visible=True)
        return render(request, "askmath/content/discipline/content_view_disciplines.html",
            {'request':request,'disciplines': disciplines, 'message': message})
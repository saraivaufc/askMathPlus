from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from .idiscipline import IDiscipline

class Discipline(IDiscipline):
    
    def view_discipline(self, request, discipline):
    	return render(request, "askmath/content/discipline/content_view_discipline.html", 
            {'request':request, 'discipline': discipline})
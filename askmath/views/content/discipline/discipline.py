from django.shortcuts import render, HttpResponse

from askmath.models.discipline import Discipline as DisciplineModel
from .idiscipline import IDiscipline


class Discipline(IDiscipline):
    def view_disciplines(self, request, classe=None):
        if classe:
            disciplines = classe.get_disciplines()
        else:
            disciplines = DisciplineModel.objects.filter(exists=True, visible=True)
        return render(request, "askmath/content/content_home.html",
                      {'request': request, 'disciplines': disciplines, 'current_classe': classe})

    def view_discipline(self, request, discipline):
        return render(request, "askmath/content/discipline/content_view_discipline.html",
                      {'request': request, 'discipline': discipline})

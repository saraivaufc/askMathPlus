from askmath.models import Discipline as DisciplineModel
from django.shortcuts import render


def index_view(request):
    disciplines = DisciplineModel.objects.filter(exists=True, visible=True)
    return render(request, 'askmath/content/content_home.html', {'request': request, 'disciplines': disciplines})

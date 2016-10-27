from django.shortcuts import render, HttpResponse

from askmath.models.discipline import Discipline as DisciplineModel
from askmath.utils.lesson_sorting import LessonSorting
from .idiscipline import IDiscipline



class Discipline(IDiscipline):
	def view_disciplines(self, request):
		disciplines = DisciplineModel.objects.filter(exists=True, visible=True)
		return render(request, "askmath/content/content_home.html",
					  {'request': request, 'disciplines': disciplines})

	def view_discipline(self, request, discipline):
		lesson_no_edges = []
		for l in discipline.get_lessons():
			if not l.get_requirements():
				lesson_no_edges.append(l)
		lesson_sorting = LessonSorting(lesson_no_edges, discipline)
		lessons = lesson_sorting.get_result()
		return render(request, "askmath/content/discipline/content_view_discipline.html",
					  {'request': request, 'discipline': discipline, 'lessons': lessons})

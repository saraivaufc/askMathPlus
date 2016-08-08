from askmath.entities import TextMessage
from askmath.entities import ExperienceLevel
from askmath.models.classe import Classe as ClasseModel
from askmath.models.experience import StudentExperience
from askmath.models.users import Student as StudentModel
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .iranking import IRanking


class Ranking(IRanking):
	def view_ranking(self, request, student, classe):

		student_experience = student.get_student_experience()
		if student_experience.is_new_round():
			new_round = True
			student_experience.new_round = False
			student_experience.save()
		else:
			new_round = False

		experience_level = ExperienceLevel(student_experience.get_level())

		student_experiences = StudentExperience.objects.filter(exists=True).order_by('-new_scores')
		students_list = []
		last_winner = None
		for index, i in enumerate(student_experiences): 
			if i.is_last_winner():
				last_winner = i
			students_list.append({
									"position": index+1, 
									"student":i.get_student(), 
									"student_experience": i, 
									"experience_level": ExperienceLevel(i.get_level())
								 })

		return render(request, "askmath/content/ranking/content_view_ranking.html",
						{'request': request, 
						'classe': classe, 
						'me': student, 
						'student_experience': student_experience,
						'experience_level': experience_level, 
						'students': students_list,
						"new_round": new_round,
						"last_winner": last_winner,
						})
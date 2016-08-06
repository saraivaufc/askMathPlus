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
		if(student_experience.is_new_round()){
			student_experience.new_round = False
			student_experience.save()
		}

		experience_level = ExperienceLevel(student_experience.level)

		students = StudentModel.objects.filter(exists=True)
		students_list = []
		for i in students:
			try:
				try:
					temp_student_experience = StudentExperience.objects.get(student=i, exists=True)
				except Exception, e:
					print e
					temp_student_experience = StudentExperience(student=i)
					temp_student_experience.save()
				temp_experience_level = ExperienceLevel(temp_student_experience.get_level())
			except Exception, e:
				print e
				continue
			students_list.append({"student":i, "student_experience": temp_student_experience, "experience_level": temp_experience_level})

		return render(request, "askmath/content/ranking/content_view_ranking.html",
						{'request': request, 
						'classe': classe, 
						'me': student, 
						'student_experience': student_experience,
						'experience_level': experience_level, 
						'students': students_list})
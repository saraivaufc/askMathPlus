from celery.task.schedules import crontab
from celery.decorators import periodic_task

from askmath.models.experience import StudentExperience

#crontab(hour=0, minute=0, day_of_week=1)

@periodic_task(run_every=(crontab(hour=0, minute=0, day_of_week=1)), name="reset_round", ignore_result=True)
def reset_round():
	winner = None
	swap = False
	temp_student_experience = None
	for student_experience in  StudentExperience.objects.filter(exists=True):
		temp_student_experience = student_experience
		student_experience.new_round = True
		
		student_experience.last_scores = student_experience.get_scores()
		student_experience.last_new_scores = student_experience.get_new_scores()
		
		student_experience.new_scores = 0

		if not winner:
			winner = student_experience

		if student_experience.get_new_scores() > winner.get_new_scores():
			swap = True
			winner = student_experience
		else:
			student_experience.last_winner = False

		student_experience.save()

	if swap:
		update = True
	elif winner.get_new_scores() != temp_student_experience.get_new_scores():
		update = True
	else:
		update = False

	if update:
		StudentExperience.objects.filter(id=winner.id, exists=True).update(last_winner=True)

	

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from datetime import datetime
from django.utils import timezone


from askmath.models.experience import StudentExperience

#crontab(hour=0, minute=0, day_of_week=1)

c = crontab(hour=0, minute=0, day_of_week=0)

@periodic_task(run_every=(c), name="reset_round", ignore_result=True)
def reset_round():
	winner = None
	winner_new_scores = 0
	swap = False
	temp_student_experience = None
	students_experiences = StudentExperience.objects.filter(exists=True)
	for student_experience in  students_experiences:
		temp_student_experience = student_experience
		student_experience.new_round = True
		student_experience.date_start_new_round = timezone.now()
		student_experience.date_end_new_round =timezone.now() +  c.remaining_estimate(timezone.now())
		
		student_experience.last_scores = student_experience.get_full_scores()
		student_experience.last_new_scores = student_experience.get_new_scores()

		if not winner:
			winner = student_experience
			winner_new_scores = student_experience.get_new_scores()

		if student_experience.get_new_scores() > winner_new_scores:
			swap = True
			winner = student_experience
			winner_new_scores = student_experience.get_new_scores()
		else:
			student_experience.last_winner = False

		student_experience.new_scores = 0
		student_experience.save()

	if swap or len(students_experiences) == 1:
		update = True
	elif winner_new_scores != temp_student_experience.get_new_scores():
		update = True
	else:
		update = False

	if update:
		winner.last_winner = True
		winner.save()

	

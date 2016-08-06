from celery.task.schedules import crontab
from celery.decorators import periodic_task

print "Task Some_Task"

@periodic_task(run_every=(crontab(minute='*/1')), name="some_task", ignore_result=True)
def some_task():
	f = file("ciano.txt", 'w')
	f.write("casa")

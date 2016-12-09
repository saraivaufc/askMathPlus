from django.conf.urls import patterns, include, url

from askmath.views.manager.statistic import StudentStatistics


student_statistics = StudentStatistics()

urlpatterns = patterns('',
    url(r'^list_students/$', student_statistics.list_students, name="manager_statistics_student_list_students"),
    url(r'^lessons_completed/student=(?P<id_student>\d+)/$', student_statistics.lessons_completed, name="manager_statistics_student_lessons_completed"),
    url(r'^lessons_redone/student=(?P<id_student>\d+)/$', student_statistics.lessons_redone, name="manager_statistics_student_lessons_redone"),
    url(r'^lessons_in_progress/student=(?P<id_student>\d+)/$', student_statistics.lessons_in_progress, name="manager_statistics_student_lessons_in_progress"),
)
from askmath.views.manager import ProxyQuestion
from django.conf.urls import patterns, url


proxy_question = ProxyQuestion()  

urlpatterns = patterns('',
    url(r'^view/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.view_questions, name="manager_question_view"),
    url(r'^view_removed/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.view_questions_removed, name="manager_question_view_removed"),
    url(r'^add/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/quantity_items=(?P<quantity_items>\d+)/$', proxy_question.add_question, name="manager_question_add"),
    url(r'^remove/question=(?P<id_question>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.remove_question, name="manager_question_remove"),
    url(r'^edit/question=(?P<id_question>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.edit_question, name="manager_question_edit"),
    url(r'^restore/question=(?P<id_question>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.restore_question, name="manager_question_restore"),
    url(r'^sort/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.sort_questions, name="manager_question_sort"),
)
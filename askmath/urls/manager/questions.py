from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyQuestion


proxy_question = ProxyQuestion()  

urlpatterns = patterns('',
    url(r'^view/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.view_questions),
    url(r'^view_removed/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.view_questions_removed),
    url(r'^add/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/quantity_items=(?P<quantity_items>\d+)/$', proxy_question.add_question),
    url(r'^remove/question=(?P<id_question>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.remove_question),
    url(r'^edit/question=(?P<id_question>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.edit_question),
    url(r'^restore/question=(?P<id_question>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.restore_question),
    url(r'^sort/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_question.sort_questions),
)
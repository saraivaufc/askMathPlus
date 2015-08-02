from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyQuestion


proxy_question = ProxyQuestion()  

urlpatterns = patterns('',
    url(r'^choose_lesson/$', proxy_question.choose_lesson),
    url(r'^view/lesson=(?P<id_lesson>\d+)/$', proxy_question.view_questions),
    url(r'^view_removed/lesson=(?P<id_lesson>\d+)/$', proxy_question.view_questions_removed),
    url(r'^view/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_question.view_question),
    url(r'^add/lesson=(?P<id_lesson>\d+)/quantity_items=(?P<quantity_items>\d+)/$', proxy_question.add_question),
    url(r'^remove/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_question.remove_question),
    url(r'^edit/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_question.edit_question),
    url(r'^restore/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_question.restore_question),
    url(r'^sort/lesson=(?P<id_lesson>\d+)/$', proxy_question.sort_questions),
)
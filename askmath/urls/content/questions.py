from django.conf.urls import patterns, include, url

from askmath.views.content import ProxyQuestion


proxy_category = ProxyQuestion()  

urlpatterns = patterns('',
    url(r'^view_inicial_details/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/$', proxy_category.view_initial_details),
    url(r'^reset_lesson/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/$', proxy_category.reset_lesson),
    url(r'^view_question/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/$', proxy_category.view_question),
    url(r'^answer_question/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_category.answer_question),
    url(r'^jump_question/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_category.jump_question),
    url(r'^choose_skipped_question/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_category.choose_skipped_question),
    url(r'^help/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_category.help_question),
   
)
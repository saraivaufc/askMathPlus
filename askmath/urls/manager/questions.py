from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyQuestion


proxy_category = ProxyQuestion()  

urlpatterns = patterns('',
    url(r'^choose_lesson/$', proxy_category.choose_lesson),
    url(r'^view/lesson=(?P<id_lesson>\d+)/$', proxy_category.view_questions),
    url(r'^view_removed/lesson=(?P<id_lesson>\d+)/$', proxy_category.view_questions_removed),
    url(r'^view/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_category.view_question),
    url(r'^add/lesson=(?P<id_lesson>\d+)/quantity_items=(?P<quantity_items>\d+)/$', proxy_category.add_question),
    url(r'^remove/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_category.remove_question),
    url(r'^edit/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_category.edit_question),
    url(r'^restore/lesson=(?P<id_lesson>\d+)/question=(?P<id_question>\d+)/$', proxy_category.restore_question),
    url(r'^sort/lesson=(?P<id_lesson>\d+)/$', proxy_category.sort_questions),
)
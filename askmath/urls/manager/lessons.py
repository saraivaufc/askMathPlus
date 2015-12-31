from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyLesson


proxy_category = ProxyLesson()  

urlpatterns = patterns('',
    url(r'^view/discipline=(?P<id_discipline>\d+)/$', proxy_category.view_lessons),
    url(r'^view_removed/discipline=(?P<id_discipline>\d+)/$', proxy_category.view_lessons_removed),
    url(r'^add/discipline=(?P<id_discipline>\d+)/$', proxy_category.add_lesson),
    url(r'^remove/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_category.remove_lesson),
    url(r'^edit/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_category.edit_lesson),
    url(r'^restore/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_category.restore_lesson),
)
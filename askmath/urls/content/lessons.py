from django.conf.urls import patterns, include, url

from askmath.views.content import ProxyLesson


proxy_lesson = ProxyLesson()  

urlpatterns = patterns('',
    url(r'^view/discipline=(?P<id_discipline>\d+)/$', proxy_lesson.view_lessons),
    url(r'^view/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/$', proxy_lesson.view_lesson),
)
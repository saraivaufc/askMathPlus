from django.conf.urls import patterns, include, url

from askmath.views.manager.statistic import ProxyLesson


proxy_lesson = ProxyLesson()  
urlpatterns = patterns('',
    url(r'^choose_lesson/$', proxy_lesson.choose_lesson),
    url(r'^view_statistics/lesson=(?P<id_lesson>\d+)/$', proxy_lesson.view_statistics),
)
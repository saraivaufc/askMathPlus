from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyLesson


proxy_lesson = ProxyLesson()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_lesson.view_lessons),
    url(r'^view_removed/$', proxy_lesson.view_lessons_removed),
    url(r'^view/lesson=(?P<id_lesson>\d+)/$', proxy_lesson.view_lesson),
    url(r'^add/$', proxy_lesson.add_lesson),
    url(r'^remove/lesson=(?P<id_lesson>\d+)/$', proxy_lesson.remove_lesson),
    url(r'^edit/lesson=(?P<id_lesson>\d+)/$', proxy_lesson.edit_lesson),
    url(r'^restore/lesson=(?P<id_lesson>\d+)/$', proxy_lesson.restore_lesson),
)
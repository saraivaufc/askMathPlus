from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyLesson


proxy_category = ProxyLesson()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_category.view_lessons),
    url(r'^view_removed/$', proxy_category.view_lessons_removed),
    url(r'^view/lesson=(?P<id_lesson>\d+)/$', proxy_category.view_lesson),
    url(r'^add/$', proxy_category.add_lesson),
    url(r'^remove/lesson=(?P<id_lesson>\d+)/$', proxy_category.remove_lesson),
    url(r'^edit/lesson=(?P<id_lesson>\d+)/$', proxy_category.edit_lesson),
    url(r'^restore/lesson=(?P<id_lesson>\d+)/$', proxy_category.restore_lesson),
)
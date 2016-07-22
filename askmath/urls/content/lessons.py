from askmath.views.content import ProxyLesson
from django.conf.urls import patterns, url


proxy_category = ProxyLesson()  

urlpatterns = patterns('',
    url(r'^view/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/$', proxy_category.view_lesson, name="content_lesson_view"),
)
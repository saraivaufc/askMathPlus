from django.conf.urls import patterns, include, url

from askmath.views.services import ProxyLesson


proxy_lesson = ProxyLesson()  

urlpatterns = patterns('',
    url(r'^get/$', proxy_lesson.get),
)
from django.conf.urls import patterns, include, url

from askmath.views.content import ProxyVideo


proxy_video = ProxyVideo()  

urlpatterns = patterns('',
    url(r'^view/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/$', proxy_video.view_videos),
    url(r'^view/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/video=(?P<id_video>\d+)/', proxy_video.view_video),
)
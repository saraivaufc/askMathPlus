from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyVideo


proxy_video = ProxyVideo()  

urlpatterns = patterns('',
    url(r'^view/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.view_videos),
    url(r'^view_removed/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.view_videos_removed),
    url(r'^add/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.add_video),
    url(r'^remove/video=(?P<id_video>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.remove_video),
    url(r'^edit/video=(?P<id_video>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.edit_video),
    url(r'^restore/video=(?P<id_video>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.restore_video),
    url(r'^sort/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.sort_videos),
)
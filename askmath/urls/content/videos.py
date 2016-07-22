from askmath.views.content import ProxyVideo
from django.conf.urls import patterns, url

proxy_video = ProxyVideo()

urlpatterns = patterns('',
                       url(r'^view/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/$',
                           proxy_video.view_videos, name="content_video_view"),
                       url(
                           r'^view/discipline=(?P<id_discipline>\d+)/lesson=(?P<id_lesson>\d+)/video=(?P<id_video>\d+)/',
                           proxy_video.view_video, name="content_video_view"),
                       )

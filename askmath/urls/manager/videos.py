from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyVideo


proxy_video = ProxyVideo()  

urlpatterns = patterns('',
    url(r'^view/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.view_videos, name="manager_video_view"),
    url(r'^view_removed/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.view_videos_removed, name="manager_video_view_removed"),
    url(r'^add/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.add_video, name="manager_video_add"),
    url(r'^remove/video=(?P<id_video>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.remove_video, name="manager_video_remove"),
    url(r'^edit/video=(?P<id_video>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.edit_video, name="manager_video_edit"),
    url(r'^restore/video=(?P<id_video>\d+)/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.restore_video, name="manager_video_restore"),
    url(r'^sort/lesson=(?P<id_lesson>\d+)/discipline=(?P<id_discipline>\d+)/$', proxy_video.sort_videos, name="manager_video_sort"),
)
from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyVideo


proxy_video = ProxyVideo()  

urlpatterns = patterns('',
    url(r'^choose_lesson/$', proxy_video.choose_lesson),
    url(r'^view/lesson=(?P<id_lesson>\d+)/$', proxy_video.view_videos),
    url(r'^view_removed/lesson=(?P<id_lesson>\d+)/$', proxy_video.view_videos_removed),
    url(r'^view/lesson=(?P<id_lesson>\d+)/video=(?P<id_video>\d+)/$', proxy_video.view_video),
    url(r'^add/lesson=(?P<id_lesson>\d+)/$', proxy_video.add_video),
    url(r'^remove/lesson=(?P<id_lesson>\d+)/video=(?P<id_video>\d+)/$', proxy_video.remove_video),
    url(r'^edit/lesson=(?P<id_lesson>\d+)/video=(?P<id_video>\d+)/$', proxy_video.edit_video),
    url(r'^restore/lesson=(?P<id_lesson>\d+)/video=(?P<id_video>\d+)/$', proxy_video.restore_video),
    url(r'^sort/lesson=(?P<id_lesson>\d+)/$', proxy_video.sort_videos),
)
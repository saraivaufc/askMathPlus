from django.conf.urls import patterns, include, url

from askmath.views.forum import ProxyTopic


proxy_topic = ProxyTopic()

urlpatterns = patterns('',
    url(r'^view/category=(?P<id_category>\d+)/$', proxy_topic.view_topics),
    url(r'^view_removed/category=(?P<id_category>\d+)/$', proxy_topic.view_topics_removed),
    url(r'^view/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/$', proxy_topic.view_topic),
    url(r'^add/category=(?P<id_category>\d+)/$', proxy_topic.add_topic),
    url(r'^edit/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/$', proxy_topic.edit_topic),
    url(r'^remove/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/$', proxy_topic.remove_topic),
    url(r'^restore/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/$', proxy_topic.restore_topic),
    url(r'^like/topic=(?P<id_topic>\d+)/$', proxy_topic.like_topic),
    url(r'^unlike/topic=(?P<id_topic>\d+)/$', proxy_topic.unlike_topic),
)
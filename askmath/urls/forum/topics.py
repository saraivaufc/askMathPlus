from askmath.views.forum import ProxyTopic
from django.conf.urls import patterns, url

proxy_topic = ProxyTopic()

urlpatterns = patterns('',
                       url(r'^view/category=(?P<id_category>\d+)/$', proxy_topic.view_topics, name="forum_topic_view"),
                       url(r'^view_removed/category=(?P<id_category>\d+)/$', proxy_topic.view_topics_removed,
                           name="forum_topic_view_removed"),
                       url(r'^view/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/$', proxy_topic.view_topic,
                           name="forum_topic_view"),
                       url(r'^add/category=(?P<id_category>\d+)/$', proxy_topic.add_topic, name="forum_topic_add"),
                       url(r'^edit/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/$', proxy_topic.edit_topic,
                           name="forum_topic_edit"),
                       url(r'^remove/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/$', proxy_topic.remove_topic,
                           name="forum_topic_remove"),
                       url(r'^restore/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/$',
                           proxy_topic.restore_topic, name="forum_topic_restore"),
                       url(r'^like/topic=(?P<id_topic>\d+)/$', proxy_topic.like_topic, name="forum_topic_like"),
                       url(r'^unlike/topic=(?P<id_topic>\d+)/$', proxy_topic.unlike_topic, name="forum_topic_unlike"),
                       )

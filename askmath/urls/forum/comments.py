from django.conf.urls import patterns, include, url

from askmath.views.forum import ProxyComment


proxy_comment = ProxyComment()  

urlpatterns = patterns('',
    url(r'^add/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/$', proxy_comment.add_comment),
    url(r'^remove/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/comment=(?P<id_comment>\d+)/$', proxy_comment.remove_comment),
    url(r'^edit/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/comment=(?P<id_comment>\d+)/$', proxy_comment.edit_comment),
    url(r'^like/comment=(?P<id_comment>\d+)/$', proxy_comment.like_comment),
    url(r'^unlike/comment=(?P<id_comment>\d+)/$', proxy_comment.unlike_comment),
)
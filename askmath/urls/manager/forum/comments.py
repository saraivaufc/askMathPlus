from django.conf.urls import patterns, include, url

from askmath.views.manager.forum import ProxyComment


proxy_comment = ProxyComment()  

urlpatterns = patterns('',
    url(r'^remove/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/comment=(?P<id_comment>\d+)/$', proxy_comment.remove_comment),
    url(r'^edit/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/comment=(?P<id_comment>\d+)/$', proxy_comment.edit_comment),
)
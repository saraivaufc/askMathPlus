from askmath.views.forum import ProxyComment
from django.conf.urls import patterns, url


proxy_comment = ProxyComment()  

urlpatterns = patterns('',
    url(r'^add/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/$', proxy_comment.add_comment, name="forum_comment_add"),
    url(r'^remove/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/comment=(?P<id_comment>\d+)/$', proxy_comment.remove_comment, name="forum_comment_remove"),
    url(r'^edit/category=(?P<id_category>\d+)/topic=(?P<id_topic>\d+)/comment=(?P<id_comment>\d+)/$', proxy_comment.edit_comment, name="forum_comment_edit"),
    url(r'^like/comment=(?P<id_comment>\d+)/$', proxy_comment.like_comment, name="forum_comment_like"),
    url(r'^unlike/comment=(?P<id_comment>\d+)/$', proxy_comment.unlike_comment, name="forum_comment_unlike"),
)
from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyMessage


proxy_message = ProxyMessage()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_message.view_messages),
    url(r'^view_removed/$', proxy_message.view_messages_removed),
    url(r'^view/message=(?P<id_message>\d+)/$', proxy_message.view_message),
    url(r'^remove/message=(?P<id_message>\d+)/$', proxy_message.remove_message),
    url(r'^restore/message=(?P<id_message>\d+)/$', proxy_message.restore_message),
)
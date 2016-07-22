from askmath.views.manager import ProxyMessage
from django.conf.urls import patterns, url

proxy_message = ProxyMessage()

urlpatterns = patterns('',
                       url(r'^view/$', proxy_message.view_messages, name="manager_message_view"),
                       url(r'^view_removed/$', proxy_message.view_messages_removed,
                           name="manager_message_view_removed"),
                       url(r'^remove/message=(?P<id_message>\d+)/$', proxy_message.remove_message,
                           name="manager_message_remove"),
                       url(r'^restore/message=(?P<id_message>\d+)/$', proxy_message.restore_message,
                           name="manager_message_restore"),
                       )

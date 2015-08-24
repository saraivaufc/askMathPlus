from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyContact


proxy_contact = ProxyContact()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_contact.view_contacts),
    url(r'^view_removed/$', proxy_contact.view_contacts_removed),
    url(r'^view/contact=(?P<id_contact>\d+)/$', proxy_contact.view_contact),
    url(r'^remove/contact=(?P<id_contact>\d+)/$', proxy_contact.remove_contact),
    url(r'^restore/contact=(?P<id_contact>\d+)/$', proxy_contact.restore_contact),
)
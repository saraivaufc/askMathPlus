from django.conf.urls import patterns, include, url
from askmath.views.initial import ProxyPerson

proxy_person = ProxyPerson()

urlpatterns = patterns('',
    url(r'^profile/view/$', proxy_person.view_profile),
    url(r'^profile/edit/$', proxy_person.edit_profile),
    url(r'^profile/alter_password/$', proxy_person.alter_password),
    url(r'^profile/remove_account/$', proxy_person.remove_account),
)
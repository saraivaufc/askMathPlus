from django.conf.urls import patterns, include, url
from askmath.views.initial import ProxyPerson

proxyperson = ProxyPerson()

urlpatterns = patterns('',
    url(r'^profile/view/$', proxyperson.view_profile),
    url(r'^profile/edit/$', proxyperson.edit_profile),
)
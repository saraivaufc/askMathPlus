from django.conf.urls import patterns, include, url
from askmath.views.authentication import ProxyPerson

proxy_person = ProxyPerson()

urlpatterns = patterns('',
    url(r'^$', proxy_person.login),
    url(r'^login/$', proxy_person.login),
    url(r'^logout/$', proxy_person.logout),
    url(r'^signup/$', proxy_person.signup),
    url(r'^recover_password/$', proxy_person.recover_password)
)
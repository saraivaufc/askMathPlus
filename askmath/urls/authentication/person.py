from django.conf.urls import patterns, include, url
from askmath.views.authentication import ProxyPerson

proxy_account = ProxyPerson()

urlpatterns = patterns('',
    url(r'^$', proxy_account.login),
    url(r'^login/$', proxy_account.login),
    url(r'^logout/$', proxy_account.logout),
    url(r'^signup/$', proxy_account.signup),
    url(r'^recover_password/$', proxy_account.recover_password),
)
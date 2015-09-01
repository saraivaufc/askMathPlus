from django.conf.urls import patterns, include, url
from askmath.views.authentication import ProxyAccount

proxy_account = ProxyAccount()

urlpatterns = patterns('',
    url(r'^options/$', proxy_account.options),
    url(r'^signin/$', proxy_account.signin),
    url(r'^signup/$', proxy_account.signup),
    url(r'^logout/$', proxy_account.logout),
    url(r'^recover_password/$', proxy_account.recover_password),
)
from django.conf.urls import patterns, include, url
from askmath.views.person import ProxyAccount

proxy_account = ProxyAccount()

urlpatterns = patterns('',
    url(r'^view/$', proxy_account.view_profile),
    url(r'^edit/$', proxy_account.edit_profile),
    url(r'^alter_password/$', proxy_account.alter_password),
    url(r'^remove_account/$', proxy_account.remove_account),
)
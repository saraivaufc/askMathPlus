from askmath.views.person import ProxyAccount
from django.conf.urls import patterns, url

proxy_account = ProxyAccount()

urlpatterns = patterns('',
                       url(r'^view/$', proxy_account.view_profile, name="person_account_view"),
                       url(r'^edit/$', proxy_account.edit_profile, name="person_account_edit"),
                       url(r'^alter_password/$', proxy_account.alter_password, name="person_account_alter_password"),
                       url(r'^remove_account/$', proxy_account.remove_account, name="person_account_remove_account"),
                       )

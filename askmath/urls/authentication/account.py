from askmath.views.authentication import ProxyAccount
from django.conf.urls import patterns, url

proxy_account = ProxyAccount()

urlpatterns = patterns('',
                       url(r'^$', proxy_account.options),

                       url(r'^options/$', proxy_account.options, name="authentication_options"),
                       url(r'^signin/$', proxy_account.signin, name="authentication_signin"),
                       url(r'^signup/$', proxy_account.signup, name="authentication_signup"),
                       url(r'^logout/$', proxy_account.logout, name="authentication_logout"),
                       url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset',
                           name='reset_password_reset1'),
                       url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done',
                           name='password_reset_done'),
                       url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                           'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
                       url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
                           name='password_reset_complete'),
                       )

from django.conf.urls import patterns, include, url
from askmath.views.index import ProxyHome

proxy_home = ProxyHome()

urlpatterns = patterns('',
    url(r'^$', proxy_home.index),
    url(r'^home/$', proxy_home.index),
    url(r'^about/$', proxy_home.about),
    url(r'^contact/$', proxy_home.contact),
    url(r'^terms/$', proxy_home.terms),
    url(r'^policies/$', proxy_home.policies),
    url(r'^credits/$', proxy_home.credits),
    url(r'^contents/$', proxy_home.contents),
    url(r'^contents/lesson=(?P<id_lesson>\d+)/$', proxy_home.contents),
)
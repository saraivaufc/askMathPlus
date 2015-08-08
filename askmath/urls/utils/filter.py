from django.conf.urls import patterns, include, url

from askmath.views.utils import ProxyFilter


proxy_filter = ProxyFilter()  

urlpatterns = patterns('',
    url(r'^search/$', proxy_filter.search),
)
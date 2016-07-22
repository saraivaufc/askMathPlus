from askmath.views.utils import ProxyFilter
from django.conf.urls import patterns, url


proxy_filter = ProxyFilter()  

urlpatterns = patterns('',
    url(r'^search/$', proxy_filter.search, name="utils_filter_search"),
)
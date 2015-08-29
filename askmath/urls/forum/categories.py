from django.conf.urls import patterns, include, url

from askmath.views.forum import ProxyCategory


proxy_category = ProxyCategory()  

urlpatterns = patterns('',
    url(r'^', proxy_category.view_categories),
    url(r'^view/$', proxy_category.view_categories),
)
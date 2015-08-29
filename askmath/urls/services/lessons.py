from django.conf.urls import patterns, include, url

from askmath.views.services import ProxyLesson


proxy_category = ProxyLesson()  

urlpatterns = patterns('',
    url(r'^get/$', proxy_category.get),
)
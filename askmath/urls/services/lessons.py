from askmath.views.services import ProxyLesson
from django.conf.urls import patterns, url


proxy_category = ProxyLesson()  

urlpatterns = patterns('',
    url(r'^get/$', proxy_category.get),
)
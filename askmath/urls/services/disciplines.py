from askmath.views.services import ProxyDiscipline
from django.conf.urls import patterns, url

proxy_category = ProxyDiscipline()

urlpatterns = patterns('',
                       url(r'^get/$', proxy_category.get),
                       )

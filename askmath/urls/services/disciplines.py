from django.conf.urls import patterns, include, url

from askmath.views.services import ProxyDiscipline


proxy_discipline = ProxyDiscipline()  

urlpatterns = patterns('',
    url(r'^get/$', proxy_discipline.get),
)
from django.conf.urls import patterns, include, url

from askmath.views.content import ProxyDiscipline


proxy_discipline = ProxyDiscipline()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_discipline.view_disciplines),
    url(r'^view/discipline=(?P<id_discipline>\d+)/$', proxy_discipline.view_discipline),
)
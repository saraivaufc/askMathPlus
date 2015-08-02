from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyDiscipline


proxy_discipline = ProxyDiscipline()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_discipline.view_disciplines),
    url(r'^view_removed/$', proxy_discipline.view_disciplines_removed),
    url(r'^view/discipline=(?P<id_discipline>\d+)/$', proxy_discipline.view_discipline),
    url(r'^add/$', proxy_discipline.add_discipline),
    url(r'^remove/discipline=(?P<id_discipline>\d+)/$', proxy_discipline.remove_discipline),
    url(r'^edit/discipline=(?P<id_discipline>\d+)/$', proxy_discipline.edit_discipline),
    url(r'^restore/discipline=(?P<id_discipline>\d+)/$', proxy_discipline.restore_discipline),
)
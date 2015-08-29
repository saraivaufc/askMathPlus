from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyDiscipline


proxy_category = ProxyDiscipline()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_category.view_disciplines),
    url(r'^view_removed/$', proxy_category.view_disciplines_removed),
    url(r'^view/discipline=(?P<id_discipline>\d+)/$', proxy_category.view_discipline),
    url(r'^add/$', proxy_category.add_discipline),
    url(r'^remove/discipline=(?P<id_discipline>\d+)/$', proxy_category.remove_discipline),
    url(r'^edit/discipline=(?P<id_discipline>\d+)/$', proxy_category.edit_discipline),
    url(r'^restore/discipline=(?P<id_discipline>\d+)/$', proxy_category.restore_discipline),
)
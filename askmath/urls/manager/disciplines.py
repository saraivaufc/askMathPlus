from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyDiscipline


proxy_category = ProxyDiscipline()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_category.view_disciplines, name="manager_discipline_view"),
    url(r'^view_removed/$', proxy_category.view_disciplines_removed, name="manager_discipline_view_removed"),
    url(r'^add/$', proxy_category.add_discipline, name="manager_discipline_add"),
    url(r'^remove/discipline=(?P<id_discipline>\d+)/$', proxy_category.remove_discipline, name="manager_discipline_remove"),
    url(r'^edit/discipline=(?P<id_discipline>\d+)/$', proxy_category.edit_discipline, name="manager_discipline_edit"),
    url(r'^restore/discipline=(?P<id_discipline>\d+)/$', proxy_category.restore_discipline, name="manager_discipline_restore"),
)
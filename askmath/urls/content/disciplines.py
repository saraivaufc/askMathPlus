from askmath.views.content import ProxyDiscipline
from django.conf.urls import patterns, url


proxy_discipline = ProxyDiscipline()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_discipline.view_disciplines, name="content_discipline_view"),
    url(r'^view/discipline=(?P<id_discipline>\d+)/$', proxy_discipline.view_discipline, name="content_discipline_view"),
)
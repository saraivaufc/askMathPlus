from django.conf.urls import patterns, include, url

from askmath.views.content import ProxyDiscipline


proxy_category = ProxyDiscipline()  

urlpatterns = patterns('',
    url(r'^view/$', proxy_category.view_disciplines),
)
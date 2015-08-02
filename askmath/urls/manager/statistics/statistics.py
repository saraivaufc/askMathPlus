from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyStatistic


proxy_statistic = ProxyStatistic()  
urlpatterns = patterns('',
    url(r'^choose_type/$', proxy_statistic.choose_type),
    url(r'^discipline/', include('askmath.urls.manager.statistics.disciplinestatistics')),
    url(r'^lesson/', include('askmath.urls.manager.statistics.lessonstatistics')),
)
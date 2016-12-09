from django.conf.urls import patterns, include, url

from askmath.views.manager import ProxyStatistic


proxy_statistic = ProxyStatistic()
urlpatterns = patterns('',
    url(r'^choose_type/$', proxy_statistic.choose_type),
    url(r'^student_statistics/', include('askmath.urls.manager.statistics.student_statistics')),
)
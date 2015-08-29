from django.conf.urls import patterns, include, url

from askmath.views.manager.statistic import ProxyLesson


proxy_category = ProxyLesson()  
urlpatterns = patterns('',
    url(r'^choose_lesson/$', proxy_category.choose_lesson),
    url(r'^view_statistics/lesson=(?P<id_lesson>\d+)/$', proxy_category.view_statistics),
)
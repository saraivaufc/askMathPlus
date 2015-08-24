from django.conf.urls import patterns, include, url
from askmath.views.index import Home

home = Home()

urlpatterns = patterns('',
    url(r'^$', home.index),
    url(r'^home/$', home.index),
    url(r'^about/$', home.about),
    url(r'^contact/$', home.contact),
    url(r'^terms/$', home.terms),
    url(r'^policies/$', home.policies),
    url(r'^credits/$', home.credits),
    url(r'^contents/$', home.contents),
    url(r'^contents/lesson=(?P<id_lesson>\d+)/$', home.contents),
)
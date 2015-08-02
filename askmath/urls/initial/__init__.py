from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^', include('askmath.urls.initial.home')),
    url(r'^person/', include('askmath.urls.initial.person')),
)
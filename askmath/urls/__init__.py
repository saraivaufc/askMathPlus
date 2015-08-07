from django.conf.urls import patterns, include, url


urlpatterns = patterns('',          
    url(r'^',  include('askmath.urls.initial')),
    url(r'^authentication/', include('askmath.urls.authentication')),
    
    url(r'^home/content/',  include('askmath.urls.content')),
    url(r'^home/manager/', include('askmath.urls.manager')),
    url(r'^services/', include('askmath.urls.services')),
)
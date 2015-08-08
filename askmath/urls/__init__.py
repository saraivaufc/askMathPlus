from django.conf.urls import patterns, include, url


urlpatterns = patterns('',          
    url(r'^',  include('askmath.urls.index')),
    url(r'^authentication/', include('askmath.urls.authentication')),
    
    url(r'^home/person/',  include('askmath.urls.person')),
    url(r'^home/content/',  include('askmath.urls.content')),
    url(r'^home/manager/', include('askmath.urls.manager')),
    
    url(r'^services/', include('askmath.urls.services')),
    url(r'^utils/', include('askmath.urls.utils')),
)
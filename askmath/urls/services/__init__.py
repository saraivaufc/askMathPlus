from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^disciplines/', include('askmath.urls.services.disciplines')),
                       url(r'^lessons/', include('askmath.urls.services.lessons')),
                       )

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^filter/', include('askmath.urls.utils.filter')),
                       )

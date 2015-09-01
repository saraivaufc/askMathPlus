from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('askmath.urls.forum.categories')),
    url(r'^categories/', include('askmath.urls.forum.categories')),
    url(r'^topics/', include('askmath.urls.forum.topics')),
    url(r'^comments/', include('askmath.urls.forum.comments')),
)
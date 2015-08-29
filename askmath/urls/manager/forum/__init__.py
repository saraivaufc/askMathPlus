from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('askmath.urls.manager.forum.categories')),
    url(r'^categories/', include('askmath.urls.manager.forum.categories')),
    url(r'^topics/', include('askmath.urls.manager.forum.topics')),
    url(r'^comments/', include('askmath.urls.manager.forum.comments')),
)
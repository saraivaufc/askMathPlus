from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^disciplines/', include('askmath.urls.manager.disciplines')),
    url(r'^lessons/', include('askmath.urls.manager.lessons')),
    url(r'^questions/', include('askmath.urls.manager.questions')),
    url(r'^videos/', include('askmath.urls.manager.videos')),
    url(r'^statistics/', include('askmath.urls.manager.statistics.statistics')),
    url(r'^persons/', include('askmath.urls.manager.persons')),
    url(r'^messages/', include('askmath.urls.manager.messages')),
)
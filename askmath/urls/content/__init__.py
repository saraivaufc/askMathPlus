from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^classes/', include('askmath.urls.content.classes')),
    url(r'^disciplines/', include('askmath.urls.content.disciplines')),
    url(r'^lessons/', include('askmath.urls.content.lessons')),
    url(r'^questions/', include('askmath.urls.content.questions')),
    url(r'^videos/', include('askmath.urls.content.videos')),
    url(r'^statistics/', include('askmath.urls.content.statistics')),
)
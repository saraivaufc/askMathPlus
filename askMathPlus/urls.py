from django.conf.urls import patterns, include, url
from django.contrib import admin

from askmath import urls as askmath_urls
from askmath.feeds import LessonsLatests
import settings


urlpatterns = patterns('',
    url(r'^', include(askmath_urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feed/$', LessonsLatests()),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

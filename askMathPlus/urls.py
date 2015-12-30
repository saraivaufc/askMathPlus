from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext

from askmath import urls as askmath_urls
from askmath.feeds import LessonsLatests
import settings


urlpatterns = patterns('',
    url(r'^', include(askmath_urls)),
    url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset1'),
    url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^feed/$', LessonsLatests()),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

if 'social.apps.django_app.default':
    urlpatterns += patterns('',
        url('', include('social.apps.django_app.urls', namespace='social')),
    )



#ERRORS

def handler404(request):
    response = render_to_response('askmath/index/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('askmath/index/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

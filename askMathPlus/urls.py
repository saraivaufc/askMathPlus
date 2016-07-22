import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.i18n import javascript_catalog

js_info_dict = {
    'packages': ('manager',),
}

urlpatterns = patterns('',
                       url(r'^', include('askmath.urls', namespace="askmath", app_name="askmath")),
                       url(r'^admin/', include(admin.site.urls), name='admin'),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       url(r'^jsi18n/$', javascript_catalog, js_info_dict),
                       )

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
                            url(r'^rosetta/', include('rosetta.urls')),
                            )

if 'social.apps.django_app.default':
    urlpatterns += patterns('',
                            url('', include('social.apps.django_app.urls', namespace='social')),
                            )


# ERRORS

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

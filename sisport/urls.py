from django.conf.urls import patterns, include, url
from django.contrib import admin
from ask.views import *
from ask.views_admin import *

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^' , include('ask.urls', namespace="ask", app_name="ask")),
    url(r'^' , include('ask.urls_admin', namespace="ask", app_name="ask")),

    url(r'^forum/', include('spirit.urls', namespace="spirit", app_name="spirit")),
    
    url(r'^admin/', include(admin.site.urls)),
)	

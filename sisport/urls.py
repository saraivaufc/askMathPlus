from django.conf.urls import patterns, include, url
from django.contrib import admin
from Ask.views import *


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^' , include('Ask.urls', namespace="Ask", app_name="Ask")),

    url(r'^forum/', include('spirit.urls', namespace="spirit", app_name="spirit")),
    
    url(r'^admin/', include(admin.site.urls)),
)	

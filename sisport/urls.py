# -*- coding: utf-8 -*-

#IMPORTS PYTHON

#IMPORTS DJANGO
from django.conf.urls import patterns, include, url
from django.contrib import admin

#IMPORTS SPIRIT

#IMPORTS USER_PROFILE_SPIRIT

#IMPORTS ASK



admin.autodiscover()


#ERROS

handler400 = 'ask.views.my_custom_bad_request_view'
handler403 = 'ask.views.my_custom_permission_denied_view'
handler404 = 'ask.views.my_custom_page_not_found_view'
handler500 = 'ask.views.my_custom_error_view'


urlpatterns = patterns('',
	url(r'^' , include('ask.urls', namespace="ask", app_name="ask")),

    url(r'^forum/', include('spirit.urls', namespace="spirit", app_name="spirit")),
    
    url(r'^admin/', include(admin.site.urls)),
)	

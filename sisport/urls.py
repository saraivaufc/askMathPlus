from django.conf.urls import patterns, include, url
from django.contrib import admin
from ask.views import *
from ask.views_admin import *

admin.autodiscover()


#ERROS

handler400 = 'ask.views.my_custom_bad_request_view'
handler403 = 'ask.views.my_custom_permission_denied_view'
handler404 = 'ask.views.my_custom_page_not_found_view'
handler500 = 'ask.views.my_custom_error_view'


urlpatterns = patterns('',
	url(r'^' , include('ask.urls', namespace="ask", app_name="ask")),
    url(r'^' , include('ask.urls_admin', namespace="ask", app_name="ask")),

    url(r'^forum/', include('spirit.urls', namespace="spirit", app_name="spirit")),
    
    url(r'^admin/', include(admin.site.urls)),
)	

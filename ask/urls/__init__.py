from django.conf.urls import patterns, include, url
from django.contrib import admin
from ask.views import *

urlpatterns = patterns('',
	url(r'^' , include('ask.urls.admin', namespace="ask", app_name="ask")),
	url(r'^' , include('ask.urls.user', namespace="ask", app_name="ask")),
)

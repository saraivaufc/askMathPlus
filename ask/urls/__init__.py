# -*- coding: utf-8 -*-

#IMPORTS PYTHON

#IMPORTS DJANGO
from django.conf.urls import patterns, include, url
from django.contrib import admin

#IMPORTS SPIRIT

#IMPORTS USER_PROFILE_SPIRIT

#IMPORTS ASK
from ask.views import *

urlpatterns = patterns('',
	url(r'^' , include('ask.urls.admin', namespace="ask", app_name="ask")),
	url(r'^' , include('ask.urls.user', namespace="ask", app_name="ask")),
	url(r'^' , include('ask.urls.saida', namespace="ask", app_name="ask")),
)

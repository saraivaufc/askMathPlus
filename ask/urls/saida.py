# -*- coding: utf-8 -*-

#IMPORTS PYTHON

#IMPORTS DJANGO
from django.conf.urls import patterns, include, url

#IMPORTS SPIRIT

#IMPORTS USER_PROFILE_SPIRIT

#IMPORTS ASK
from ask.views import *

urlpatterns = patterns('',

    url(r'^saida/getDisciplinas/$' , getDisciplinas),
)

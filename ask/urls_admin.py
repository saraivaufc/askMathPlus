from django.conf.urls import patterns, include, url
from django.contrib import admin
from views_admin import *

urlpatterns = patterns('',
    url(r'^principal_admin/$' , principal_admin),
 	url(r'^principal_admin/(?P<tema_conteudo>\w+)$' , secundario_admin),    
)

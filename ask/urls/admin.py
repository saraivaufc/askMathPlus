from django.conf.urls import patterns, include, url
from ask.views import *

urlpatterns = patterns('',
    url(r'^principal_admin/$' , principal_admin),
 	url(r'^principal_admin/(?P<tema_conteudo>\w+)/$' , secundario_admin),
 	url(r'^principal_admin/(?P<tema_conteudo>\w+)/(?P<id_pergunta>\d+)/$' , terciario_admin),    
)

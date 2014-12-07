from django.conf.urls import patterns, include, url
from django.contrib import admin
from matbasica.views import *


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$' , index),
    url(r'^login/$' , login ),
    url(r'^logout/$' , logout),
    url(r'^login/falha/$' , login_falha),
    
    url(r'^criarConta/$' , criarConta),
    
    url(r'^principal/$' , principal),
    url(r'^principal/(?P<tema_conteudo>\w+)$' , secundario),
    url(r'^principal/forum/$' , forum),
   
    url(r'^principal/estatisticas/$' , estatisticas),

    url(r'^contato/$', contato),
    
    
    url(r'^(?P<id_conteudo>\d+)/(?P<id_pergunta>\d+)/(?P<id_item>\d+)', verifica_respostas),

    url(r'^is_logado$', is_logado),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^forum/', include('forum.urls')),
)	

from django.conf.urls import patterns, include, url
from django.contrib import admin
from Ask.views import *


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$' , index),
    url(r'^login/$' , login, {'template_name': 'login/login.php'}, name='user-login' ),
    url(r'^logout/$' , logout),
    url(r'^login/falha/$' , login_falha),
    
    url(r'^criarConta/$' , criarConta),
    
    url(r'^principal/$' , principal),
    url(r'^principal/(?P<tema_conteudo>\w+)/$' , secundario),

    url(r'^contato/$', contato),

    url(r'^ajuda/(?P<item_id>\d+)/$', getAjuda),
    
    url(r'^atualiza_estado/(?P<conteudo_id>\d+)/(?P<pergunta_id>\d+)/$', atualiza_estado_usuario),
    
    url(r'^busca_ajuda/(?P<id_pergunta>\d+)/(?P<id_item>\d+)/$', busca_ajuda),

    url(r'^(?P<id_conteudo>\d+)/(?P<id_pergunta>\d+)/(?P<id_item>\d+)/$', verifica_respostas),

    url(r'^pulo/(?P<id_conteudo>\d+)/(?P<id_pergunta>\d+)/$', pulo),

    url(r'^is_logado/$', is_logado),
    
    url(r'^forum/', include('spirit.urls', namespace="spirit", app_name="spirit")),
    
    url(r'^admin/', include(admin.site.urls)),
)	

# -*- coding: utf-8 -*-

#IMPORTS PYTHON

#IMPORTS DJANGO
from django.conf.urls import patterns, include, url

#IMPORTS SPIRIT

#IMPORTS USER_PROFILE_SPIRIT

#IMPORTS ASK
from ask.views import *


urlpatterns = patterns('',
	url(r'^principal_admin/$' , principal_admin),
	url(r'^principal_admin/(?P<tema_conteudo>\w+)/$' , secundario_admin),
	url(r'^principal_admin/(?P<tema_conteudo>\w+)/(?P<id_pergunta>\d+)/$' , terciario_admin), 
	url(r'^gerenciador/$' , gerenciador ), 
	url(r'^gerenciador/add/(?P<opcao>\d+)/$' , addOpcao ),
	url(r'^gerenciador/rem/(?P<opcao>\d+)/$' , remOpcao ), 
	url(r'^gerenciador/edit/(?P<opcao>\d+)/$' , editOpcao ),
	url(r'^ordena_perguntas/$', ordenaPerguntas),
	url(r'^zerar_perguntas/$', zerarPerguntas),
)

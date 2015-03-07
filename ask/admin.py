# -*- coding: utf-8 -*-

#IMPORTS PYTHON

#IMPORTS DJANGO
from django.contrib import admin

#IMPORTS SPIRIT

#IMPORTS USER_PROFILE_SPIRIT

#IMPORTS ASK
from ask.models import *



from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('nome',)
        	  }
        ),
	)
	list_display = ('id','nome',)
	list_display_links = ('id',)
	list_editable = ('nome',)
	save_as = True
	search_fields = ['nome']

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':( 'disciplina',
        				 'tema',
        	             'descricao',
        	             'pergunta_inicial',  
        				  'requisitos',
        				  'sugestao_estudo',
        				  'max_pulos',
        				  'linha_metro',
        				  'tamanho_metro',
        				 )
        	  }
        ),
	)

	list_display = ('id','tema','max_pulos','linha_metro','tamanho_metro',)
	list_display_links = ('id',)
	list_editable = ('tema','max_pulos','linha_metro','tamanho_metro',)
	list_filter = ('disciplina','linha_metro','tamanho_metro',)
	raw_id_fields = ('disciplina', 'requisitos', 'sugestao_estudo')
	save_as = True
	search_fields = ['tema'] 


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('conteudo_pertence',
        			'descricao',
        			'item_a','deficiencia_a',
        			'item_b','deficiencia_b',
        			'item_c','deficiencia_c',
        			'item_d','deficiencia_d',
        			'item_e','deficiencia_e',
        			 'item_correto',
        			 'visivel',
        			 'ajuda',
        			 'pontos',
        				)
        	  }
        ),
	)
	list_display = ('id','conteudo_pertence','descricao', 'item_a','item_b','item_c','item_d','item_e','item_correto','visivel', 'ajuda','pontos', )
	list_display_links = ('id','descricao',)
	list_filter = ('conteudo_pertence',)
	raw_id_fields = ('conteudo_pertence',)
	save_as = True
	search_fields = ['descricao',]


@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('usuario',
        			      'disciplina',
        			      'conteudo',
        				  'pergunta',
        				  'item',
        				  'acertou',
        				)
        	  }
        ),
	)
	list_display = ('id','usuario',
			      	'disciplina',
			      	'conteudo',
				  	'pergunta',
				  	'item',
				  	'acertou',
				  	'criacao',)
	list_display_links = ('id',)
	
	list_filter = ('disciplina','usuario','disciplina','conteudo','pergunta','item','acertou','criacao')
	raw_id_fields = ('usuario',
    			     'disciplina',
    			     'conteudo',
    				 'pergunta',)
	save_as = True
	search_fields = ['usuario']

@admin.register(Estado_Usuario)
class Estado_UsuarioAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('disciplina',
        				  'usuario',
        			      'conteudo',
        				  'pergunta',
        				)
        	  }
        ),
	)
	list_display = ('id','disciplina',
		   			'usuario',
			      	'conteudo',
				  	'pergunta',
				  	'criacao',)
	list_display_links = ('id','disciplina',)
	list_filter = ('disciplina','usuario','conteudo','pergunta','criacao')
	raw_id_fields = ('usuario',
    			     'disciplina',
    			     'conteudo',
    				 'pergunta',)
	save_as = True
	search_fields = ['usuario']

@admin.register(Busca_Ajuda)
class Busca_AjudaAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('usuario',
        				  'conteudo',
        				  'pergunta',
        				)
        	  }
        ),
	)
	list_display = ('id',
                    'usuario',
				  	'conteudo',
				  	'pergunta',
				  	'criacao',)
	list_display_links = ('id','usuario',)
	list_filter = ('usuario','conteudo','pergunta','criacao', )
	raw_id_fields = ('usuario',
				  	'conteudo',
				  	'pergunta',)
	save_as = True
	search_fields = ['conteudo']

@admin.register(Pulo)
class PuloAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('disciplina',
        				  'usuario',
        			      'conteudo',
        				  'pergunta',
        				)
        	  }
        ),
	)
	list_display = ('id','disciplina',
		   			'usuario',
			      	'conteudo',
				  	'pergunta',
				  	'criacao',)
	list_display_links = ('id',)
	list_filter = ('disciplina','usuario','conteudo','pergunta','criacao',)
	raw_id_fields = ('usuario',
    			     'disciplina',
    			     'conteudo',
    				 'pergunta',)
	save_as = True
	search_fields = ['usuario']


@admin.register(Pontuacao)
class PontuacaoAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('usuario',
        			      'conteudo',
        				)
        	  }
        ),
	)
	list_display = ('id',
					'usuario',
					'conteudo',
					'pontos',
					'pulosMaximo',
					'pulosRestantes',
					'acertos_seguidos',
					'erros_seguidos')
	list_display_links = ('id',)
	list_filter = ('usuario','conteudo','pontos','pulosRestantes',)
	raw_id_fields = ('usuario',
    			     'conteudo',)
	save_as = True
	search_fields = ['usuario']

@admin.register(Secao)
class SecaoAdmin(admin.ModelAdmin):
	fieldsets = (
        (None,{'fields':('usuario',
        			     'conteudo',
        			     'inicio',
        			     'fim',
        				)
        	  }
        ),
	)
	list_display = ('id',
					'usuario',
			      	'conteudo',
				  	'inicio',
				  	'fim',)
	list_display_links = ('id','usuario',)
	list_filter = ('usuario','conteudo','inicio','fim',)

	raw_id_fields = ('usuario',
    			     'conteudo',)
	save_as = True
	search_fields = ['usuario']

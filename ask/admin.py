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


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('disciplina',
        	             'semestre',
        	             'professor',
        				)
        	  }
        ),
	)
	list_display = ('id','disciplina','semestre','professor',)
	list_display_links = ('id',)
	list_editable = ('disciplina','semestre','professor',)
	list_filter = ('semestre',)
	save_as = True
	search_fields = ['nome'] 

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':(		'turma',
        				 'tema',
        	             		'descricao',  
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
	list_filter = ('turma','linha_metro','tamanho_metro',)
	raw_id_fields = ('turma', 'requisitos', 'sugestao_estudo')
	save_as = True
	search_fields = ['tema'] 


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('conteudo_pertence',
        			'descricao',
        			'item_a','item_b','item_c','item_d','item_e',
        			 'item_correto',
        			 'ajuda',
        			 'pontos',
        				)
        	  }
        ),
	)
	list_display = ('id','conteudo_pertence','getDescricaoMin', 'item_a','item_b','item_c','item_d','item_e','item_correto', 'ajuda','pontos', )
	list_display_links = ('id','getDescricaoMin',)
	list_editable = ('conteudo_pertence','item_correto','ajuda','pontos', )
	list_filter = ('conteudo_pertence',)
	raw_id_fields = ( 'item_a','item_b','item_c','item_d','item_e','item_correto','conteudo_pertence','ajuda',)
	save_as = True
	search_fields = ['descricao',]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('descricao',
        		         'deficiencia',
        			)
        	  }
        ),
	)
	list_display = ('id','getDescricaoMin','deficiencia', )
	list_display_links = ('id','getDescricaoMin',)
	list_editable = ('deficiencia',)
	list_filter = ('deficiencia',)
	raw_id_fields = ('deficiencia',)
	save_as = True
	search_fields = ['descricao',]

@admin.register(Deficiencia)
class DeficienciaAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('conteudo',
        			      'descricao',
        				)
        	  }
        ),
	)
	list_display = ('id','conteudo','getDescricaoMin',  )
	list_display_links = ('id','getDescricaoMin',)
	list_editable = ('conteudo', )
	list_filter = ('conteudo',)
	raw_id_fields = ('conteudo',)
	save_as = True
	search_fields = ['descricao']

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('usuario',
        			      'turma',
        			      'conteudo',
        				  'pergunta',
        				  'item',
        				  'acertou',
        				)
        	  }
        ),
	)
	list_display = ('id','usuario',
			      	'turma',
			      	'conteudo',
				  	'pergunta',
				  	'item',
				  	'acertou',
				  	'criacao',)
	list_display_links = ('id',)
	
	list_filter = ('turma','usuario','turma','conteudo','pergunta','item','acertou','criacao')
	raw_id_fields = ('usuario',
    			     'turma',
    			     'conteudo',
    				 'pergunta',
    				 'item',)
	save_as = True
	search_fields = ['usuario']

@admin.register(Estado_Usuario)
class Estado_UsuarioAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('turma',
        				  'usuario',
        			      'conteudo',
        				  'pergunta',
        				)
        	  }
        ),
	)
	list_display = ('id','turma',
		   			'usuario',
			      	'conteudo',
				  	'pergunta',
				  	'criacao',)
	list_display_links = ('id','turma',)
	list_filter = ('turma','usuario','conteudo','pergunta','criacao')
	raw_id_fields = ('usuario',
    			     'turma',
    			     'conteudo',
    				 'pergunta',)
	save_as = True
	search_fields = ['usuario']

@admin.register(Ajuda)
class AjudaAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('conteudo',
        				 'descricao',
        				)
        	  }
        ),
	)
	list_display = ('id','getDescricaoMin','conteudo',)
	list_display_links = ('id','getDescricaoMin',)
	list_editable =('conteudo',)
	list_filter = ('conteudo',)
	
	raw_id_fields = ('conteudo',)
	save_as = True
	search_fields = ['descricao']

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
        (None,{'fields':('turma',
        				  'usuario',
        			      'conteudo',
        				  'pergunta',
        				)
        	  }
        ),
	)
	list_display = ('id','turma',
		   			'usuario',
			      	'conteudo',
				  	'pergunta',
				  	'criacao',)
	list_display_links = ('id',)
	list_filter = ('turma','usuario','conteudo','pergunta','criacao',)
	raw_id_fields = ('usuario',
    			     'turma',
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

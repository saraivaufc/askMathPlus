from django.contrib import admin
from models import *


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	fieldsets = (
        (None,{'fields':('username',
        				 'first_name',
        				 'last_name',
        	             'email',
        	             'password',
        	             'turma',
        				)
        	  }
        ),
	)
	raw_id_fields = ('turma',)
	list_display = ('id','username','first_name','last_name' ,'email',)
	save_as = True
	search_fields = ['nome']


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('nome',
        	             'semestre',
        				)
        	  }
        ),
	)
	list_display = ('id','nome','semestre','criacao')
	save_as = True
	search_fields = ['nome'] 

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('turma',
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
	list_display = ('id','tema','pergunta_inicial','max_pulos',)
	raw_id_fields = ('turma','pergunta_inicial', 'requisitos', 'sugestao_estudo')
	save_as = True
	search_fields = ['tema'] 


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('conteudo_pertence',
        			      'descricao',
        				  'item_correto',
        				  'pergunta_proximo_acertou',
        				  'pergunta_proximo_errou',
        				  'ajuda',
        				  'pontos',
        				)
        	  }
        ),
	)
	list_display = ('id','conteudo_pertence','descricao', 'item_correto', 'pergunta_proximo_acertou','pergunta_proximo_errou', 'ajuda','pontos' )
	raw_id_fields = ('item_correto','conteudo_pertence','pergunta_proximo_acertou','pergunta_proximo_errou','ajuda')
	save_as = True
	search_fields = ['descricao']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('pergunta_pertence',
        			      'descricao',
        				)
        	  }
        ),
	)
	list_display = ('id','pergunta_pertence','descricao','criacao',  )
	raw_id_fields = ('pergunta_pertence',)
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
        (None,{'fields':('descricao',
        				)
        	  }
        ),
	)
	list_display = ('id','descricao', 'criacao',
					)
	save_as = True
	search_fields = ['descricao']

@admin.register(Busca_Ajuda)
class Busca_AjudaAdmin(admin.ModelAdmin):
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
				  	'criacao',)
	raw_id_fields = ('usuario',
				  	'conteudo',)
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
	raw_id_fields = ('usuario',
    			     'turma',
    			     'conteudo',
    				 'pergunta',)
	save_as = True
	search_fields = ['usuario']


@admin.register(UsuarioPontuacao)
class UsuarioPontuacaoAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('usuario',
        			      'conteudo',
        				)
        	  }
        ),
	)
	list_display = ('id','usuario',
			      	'conteudo',
				  	'pontos',
				  	'pulosMaximo',
				  	'pulosRestantes')

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
	list_display = ('id','usuario',
			      	'conteudo',
				  	'inicio',
				  	'fim',)

	raw_id_fields = ('usuario',
    			     'conteudo',)
	save_as = True
	search_fields = ['usuario']
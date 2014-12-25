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
	list_display = ('username','first_name','last_name' ,'email',)
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
	list_display = ('nome','semestre','criacao')
	save_as = True
	search_fields = ['nome'] 

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('tema',
        	             'descricao', 
        				  'pergunta_inicial', 
        				  'turma' ,
        				  ('linha_metro','tamanho_metro',),
        				)
        	  }
        ),
	)
	list_display = ('tema','pergunta_inicial','criacao')
	raw_id_fields = ('turma','pergunta_inicial')
	save_as = True
	search_fields = ['tema'] 


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('conteudo_pertence',
        			      'descricao',
        				  'item_correto',
        				)
        	  }
        ),
	)
	list_display = ('conteudo_pertence','descricao', 'item_correto','criacao', )
	raw_id_fields = ('item_correto','conteudo_pertence',)
	save_as = True
	search_fields = ['descricao']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('pergunta_pertence',
        			      'descricao',
        			      'possui_proxima_pergunta',
        				  'pergunta_proximo',
        				  'ajuda',
        				)
        	  }
        ),
	)
	list_display = ('pergunta_pertence','descricao','possui_proxima_pergunta','pergunta_proximo', 'ajuda','criacao',  )
	raw_id_fields = ('pergunta_pertence','pergunta_proximo','ajuda')
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
	list_display = ('usuario',
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
	list_display = ('turma',
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
	list_display = ('descricao', 'criacao',
					)
	save_as = True
	search_fields = ['descricao']

@admin.register(Busca_Ajuda)
class Busca_AjudaAdmin(admin.ModelAdmin):
	date_hierarchy = 'criacao'
	fieldsets = (
        (None,{'fields':('usuario',
        				  'pergunta',
        			      'item',
        				)
        	  }
        ),
	)
	list_display = ('usuario',
				  	'pergunta',
				  	'item',
				  	'criacao',)
	raw_id_fields = ('usuario',
				  	'pergunta',
				  	'item',)
	save_as = True
	search_fields = ['pergunta']

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
	list_display = ('turma',
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





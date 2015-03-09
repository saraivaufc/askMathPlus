{% extends 'admin/cabecalhoAdmin.php' %}

{% block titulo %}{{conteudo.tema}}{% endblock %}

{% block conteudo-left-all %}
{% block conteudo-left-visible %}
<div class="col-sm-5 col-md-4 col-lg-5">
{% endblock %}
	<div class="row">
		<div id="conteudo-left">
			<div class="font-dconteudo">
		    	<div class="descricao-conteudo">
		        		<div class="panel-heading">
		        			<div class="panel panel-info">
							 	<div class="panel-title" id="tema-conteudo">
									<center>
						            	<h3 class="texto-azul">{{ conteudo.tema|title }}</h3>
						          	</center>
							  	</div>
							 	<div class="panel-footer">
							 		<div id="descricao-conteudo">
							  		<t><p>{{ conteudo.descricao|safe }}</p><t>
							  		</div>
							  	</div>
						  	</div>
						</div>
		      		<br>
		    	</div>
		  	</div>
		</div>
	</div>
</div>

{% endblock %}


{% block conteudo-right %}
<div class="font-dconteudo">
		<div class="descricao-pergunta">
			<div class="panel-heading">
				<div class="panel panel-info">
				 	{% block panel %}
				 	<div class="panel-footer">
					 	

					 	<input id="conteudo_atual" name="conteudo_atual" value="{{conteudo.id}}" type="hidden">
					 	<input type='hidden' name='csrfmiddlewaretoken' value='{{ csrf_token }}' />
				 		
				 		<ul class="lista_perguntas list-group  perguntas_ordenadas">
							<li  data-toggle="modal" data-target="#perguntas_visiveis"  class="list-group-item active link">
								PERGUNTAS VISÍVEIS <span class="glyphicon glyphicon-info-sign"></span>
							</li>
						  	{% for i in conteudo.getPerguntasOrdenadas %}
						  		<li  value="{{ i.id }}"  name="pergunta" href="/principal_admin/{{ tema_conteudo }}/{{i.id}}/" class="list-group-item move">
						  			<t>{{ i.getDescricao|safe|truncatechars_html:80 }}</t>
						  		</li>
						  	{% empty %}
						  		<li class="list-group-item list-group-item-warning">
						  			Licao nao possui Perguntas Visiveis aos Alunos...
						  		</li>
						  	{% endfor %}
						</ul>
						<ul class="lista_perguntas list-group  perguntas_desordenadas">
							<li  data-toggle="modal" data-target="#perguntas_invisiveis"  class="list-group-item active link">
								PERGUNTAS INVISÍVEIS <span class="glyphicon glyphicon-info-sign"></span>
							</li>
						  	{% for i in conteudo.getPerguntasNaoOrdenadas %}
						  		<li  value="{{ i.id }}"  name="pergunta" href="/principal_admin/{{ tema_conteudo }}/{{i.id}}/" class="list-group-item move">
						  			<t>{{ i.getDescricao|safe|truncatechars_html:80 }}</t>
						  		</li>
						  	{% empty %}
						  		<li class="list-group-item list-group-item-warning">
						  			Licao nao possui Perguntas Invisiveis aos Alunos...
						  		</li>
						  	{% endfor %}
						</ul>

						<button  onclick="atualizarListas()" class="btn btn-success">Submeter Listas</button>

						<hr class="divider">

						<div class="list-group">
						  	<a data-toggle="modal" data-target="#requisitos_modal" class="list-group-item active">
							    REQUISITOS <span class="glyphicon glyphicon-info-sign"></span>
							</a>
							{% for c in conteudo.getRequisitos %}
								<a  onclick="window.open('/principal_admin/{{ c.getTema }}')" class="list-group-item">
									<t>{{ c.tema|title }}</t>
								</a>
							{% empty %}
								<a class="list-group-item list-group-item-warning">
									Nao existe requisitos para essa Licao
								</a>
							{% endfor %}
						</div>
						<div class="list-group">
							<a data-toggle="modal" data-target="#sugestoes_modal" class="list-group-item active">
							    SUGESTÕES DE ESTUDOS <span class="glyphicon glyphicon-info-sign"></span>
							</a>
							{% for c in conteudo.getSugestoes %}
								<a  onclick="window.open('/principal_admin/{{ c.getTema }}')" class="list-group-item">
									<t>{{ c.tema|title }}</t>
								</a>
							{% empty %}
								<a class="list-group-item list-group-item-warning">
									Nao existe sugestoes para essa Licao
								</a>
							{% endfor %}
						</div>
				  	</div>

				 {%  endblock %}
			  	</div>
			</div>
		</div>
		<center>
		{% block barra-inferior %}		
			<div class="barra-responder tela-opcoes-2">
				<div class="btn-group btn-group-justified fixer-bottom" role="toolbar">
					<div class="btn-group">
						<button  type="button"  onclick="window.location='/principal_admin/'" class="btn btn-primary">
							Voltar Início <span class="glyphicon glyphicon-th "></span>
						</button>
					</div>
					<div class="btn-group">
						<button  type="button"  data-toggle="modal" data-target="#detalhes_conteudo_modal" class="btn btn-primary">
							Detalhes <span class="glyphicon glyphicon-exclamation-sign"></span>
						</button>
					</div>
				</div>
			</div>
		{% endblock %}
		</center>

		<div class="font-dconteudo">
			{% block modals %}
				{% include 'usuario/modals/requisitos.php' %}
				{% include 'usuario/modals/sugestoes.php' %}
				{% include 'admin/modals/detalhesConteudo.php' %}
				{% include 'admin/modals/perguntasVisiveis.php' %}
				{% include 'admin/modals/perguntasInvisiveis.php' %}
			{% endblock %}

		</div>
</div>
{% endblock %}

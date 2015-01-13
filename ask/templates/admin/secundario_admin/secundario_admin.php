{% extends 'basico.php' %}
{% load webdesign %}


{% block titulo %}{{conteudo.tema}}{% endblock %}


{% block menu %}
{% include 'admin/cabecalhoAdmin.php' %}
{% endblock %}

{% block conteudo-left %}
	<div class="font-dconteudo">
    	<div class="descricao-conteudo">
        		<div class="panel-heading">
        			<div class="panel panel-info">
					 	<div class="panel-title" id="tema-conteudo">
							<center>
				            	<h3>{{ conteudo.tema|title }}</h3>
				          	</center>
					  	</div>
					 	<div class="panel-footer">
					 		<div id="descricao-conteudo">
					  		<t class="lead">{{ conteudo.descricao|safe }}<t>
					  		</div>
					  	</div>
				  	</div>
				</div>
      		<br>
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
				 	
				 		<div class="list-group">
						  	<a data-toggle="modal" data-target="#pergunta_modal"  class="list-group-item active">
						    PERGUNTAS DESTA LIÇÃO <span class="glyphicon glyphicon-sort-by-attributes"></span>
						  	</a>
						  	{% if existePerguntaInicial == False and conteudo.getQuantPerguntasTotal > 0 %}
						  		<a  class="list-group-item list-group-item-danger">
						  			Lição não possui pergunta Inicial!!!, Corrija isso imediatamente...
						  		</a>
						  	{% else %}
						  		{% if conteudo.getQuantPerguntasTotal == 0 %}
						  			<a class="list-group-item list-group-item-warning">
						  				Licao nao possui Perguntas
						  			</a>
						  		{% else %}
								  	{% for i in perguntas %}
								  		<a  value="{{ i.id }}" name="pergunta" href="/principal_admin/{{ tema_conteudo }}/{{i.id}}/" class="list-group-item">
								  			<t>{{ i.getDescricao|safe }}</t>
								  		</a>
								  	{% empty %}
								  		<a class="list-group-item list-group-item-warning">
								  			Licao nao possui Perguntas
								  		</a>
								  	{% endfor %}
								{% endif %}
							{% endif %}
						</div>
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
				{% include 'admin/modals/perguntasLicao.php' %}
			{% endblock %}

		</div>
</div>
{% endblock %}

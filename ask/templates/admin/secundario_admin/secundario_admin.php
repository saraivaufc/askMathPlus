{% extends 'basico.php' %}
{% load webdesign %}


{% block titulo %}{{conteudo.tema}}{% endblock %}


{% block menu %}
{% include 'admin/cabecalhoAdmin.php' %}
{% endblock %}

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
						            	<h3>{{ conteudo.tema|title }}</h3>
						          	</center>
							  	</div>
							 	<div class="panel-footer">
							 		<div id="descricao-conteudo">
							  		<t><p>{{ conteudo.descricao|safe }}{% lorem 300 w random %}</p><t>
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
				 		<ul id="lista-perguntas" class="list-group ">
							<li  data-toggle="modal" data-target="#pergunta_modal"  class="list-group-item active pointer">
								PERGUNTAS DESTA LIÇÃO <span class="glyphicon glyphicon-sort-by-attributes"></span>
							</li>
							{% if existePerguntaInicial == False and conteudo.getQuantPerguntasTotal > 0 %}
						  		<li  class="list-group-item list-group-item-danger">
						  			Lição não possui pergunta Inicial!!!, Corrija isso imediatamente...
						  		</li>
						  	{% else %}
						  		{% if conteudo.getQuantPerguntasTotal == 0 %}
						  			<li class="list-group-item list-group-item-warning">
						  				Licao nao possui Perguntas
						  			</li>
						  		{% else %}
								  	{% for i in perguntas %}
								  		<li  value="{{ i.id }}" name="pergunta" href="/principal_admin/{{ tema_conteudo }}/{{i.id}}/" class="list-group-item">
								  			<i class="glyphicon glyphicon-move pointer" ></i>
								  			<t>{{ i.getDescricao|safe }}</t>
								  		</li>
								  	{% empty %}
								  		<li class="list-group-item list-group-item-warning">
								  			Licao nao possui Perguntas
								  		</li>
								  	{% endfor %}
								{% endif %}
							{% endif %}
						</ul>

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

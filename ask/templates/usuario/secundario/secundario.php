{% extends 'usuario/cabecalhoUser.php' %}

{% load webdesign %}

{% block titulo %}{{conteudo.tema}}{% endblock %}

{% block estilo %}
	#conteudo{
		background-color: #337AB7;
	}
{% endblock %}

{% block funcoes %}
	$(document).ready(function(){
		$(".panel-heading").css("height", "100%");
		$(".jspPane").css("height", "100%");
		$("#requisitos").css("height", "100%");

		url = "/ganhou_bonus/" + $("#conteudo_atual").val()
		$.ajax({
			"url": url,
			"type": "get",
			"dataType": "html",
			"success": function(data) {
				if(data == "True"){
					$('#ganhou_bonus_modal').modal({
						keyboard: false
					}).css({'color': 'green', 'font-weight':'bold'});
				}			
			},
			"error": function(jqXHR, status, error) {
				alert("status:" + status + "error:" + error);
				alert(url)
			}
		});	

	});
{% endblock %}

{% block voltar_all %}
{% endblock %}

{% block conteudo-left-all %}
{% block conteudo-left-visible %}
<div class="col-sm-5 col-md-4 col-lg-5 hidden-xs">
{% endblock %}
	<div class="row">
		<div id="conteudo-left">
			<div class="font-dconteudo">
		    	<div class="descricao-conteudo">
	        		<div class="panel-heading">
	        			<div class="panel panel-primary">
						 	<div class="panel-title" id="tema-conteudo">
								<center>
					            	<t>
					            		<h3>
					            			{{ conteudo.tema|safe|title }}
					            		</h3>
					            	</t>
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
				<div class="panel panel-primary">
			  	<div class="panel-title">
			  		{%  block titulo-inicial-all %}
				 	<div id="pontuacao-pergunta">
				 		<center>
				 			<h3>
				 			{%  block titulo-inicial %}
					    		Essa Pergunta Vale {{ pergunta.pontos }} Pontos.
					    	{% endblock %}
					    	</h3>
					    </center>
				  	</div>
				  	{% endblock %}
			  	</div>
			  	<div class="panel-footer">
			  		<div class="container-fluid">
				  		<div id="point">
							{%  block pontuacao-all %}
							 	<div class="text-center">
									{%  block pontuacao %}
										<div>
											<div class="col-xs-12 col-sm-5 col-md-3">
												<div class="row">
													PONTOS = {{ pontosAcumulados|default_if_none:"0" }}
												</div>
												<div class="row">
													SALTOS = {{ pulosRealizados|default_if_none:"0" }}
												</div>
											</div>
											<div class="col-xs-12 col-sm-7 col-md-4">
												<div class="row">
													{% if NUMEROPERGUNTA == 0 %}
														Nao Pertence
													{% else %}
														QUESTAO = {{NUMEROPERGUNTA}}/{{ perguntasTotal|default_if_none:"0" }}
													{% endif %}
												</div>
												<div class="row">
													QUESTOES SALTADAS = {{perguntasPuladas|default_if_none:"0"}}/{{ perguntasTotal|default_if_none:"0" }}
												</div>
											</div>
											<div class="col-xs-12 col-sm-12 col-md-5">
												<div class="row">
													QUESTOES CORRETAS = {{perguntasCertas|default_if_none:"0"}}/{{ perguntasTotal|default_if_none:"0" }}
												</div>
												<div class="row">
													SALTOS DISPONÍVEIS = {{ pulosDisponiveis|default_if_none:"0" }}
												</div>
											</div>
										</div>
									{% endblock %}
								</div>
							{% endblock %}
						</div><!-- Point -->
					</div>
						<hr>
						{% block outros-conteudos-all %}
					  		<div class="espacamento">
								  <t><p>{{ pergunta.descricao|safe }}{% lorem 100 w random %}</p></t>
								<hr/>
								<form method="POST" id="perguntas" name="resposta">
								{%csrf_token %} 
									   <input id="pergunta_atual" name="pergunta_atual" value="{{pergunta.id}}" type="hidden"> 
									   <input id="conteudo_atual" name="conteudo_atual" value="{{conteudo.id}}" type="hidden">
									<ol>
									{% for item in pergunta.getItens %}
										<li type="A">
											<div class="font-dconteudo">
												<input name="opcao" value="{{item.id|safe}}" required="" type="radio">
												<t>{{ item.descricao|safe }}{% lorem 50 w random %}</t>
											</div>
										</li>
										<br>
									{% empty %}
										<div class="font-dconteudo">
											<t><p>Essa pergunta nao possui itens.</p></t>
										</div>
									{% endfor %}
									</ol>
								</form>
					  		</div>
				  		{% endblock %}
			  		</div><!-- Panel Foorter -->
				</div><!-- Pnale -->
			</div>
		</div>
		<center>
		{% block barra-inferior %}
			{% if existePular == False %}
				{% if existePulos == False %}
					{% if existeAjuda == False %}		
					<div class="barra-responder navbar-fixed-bottom tela-opcoes-2">
					{% else %}
					<div class="barra-responder navbar-fixed-bottom tela-opcoes-3">
					{% endif %}
				{% else %}
					{% if existeAjuda == False %}		
					<div class="barra-responder navbar-fixed-bottom tela-opcoes-3">
					{% else %}
					<div class="barra-responder navbar-fixed-bottom tela-opcoes-4">
					{% endif %}
				{% endif %}
			{% else %}
				{% if existePulos == False %}
					{% if existeAjuda == False %}		
					<div class="barra-responder navbar-fixed-bottom tela-opcoes-3">
					{% else %}
					<div class="barra-responder navbar-fixed-bottom tela-opcoes-4">
					{% endif %}
				{% else %}
					{% if existeAjuda == False %}		
					<div class="barra-responder navbar-fixed-bottom tela-opcoes-4">
					{% else %}
					<div class="barra-responder navbar-fixed-bottom tela-opcoes-5">
					{% endif %}
				{% endif %}
			{% endif %}
				<div class="btn-group btn-group-justified fixer-bottom" role="toolbar">
					<div class="btn-group">
						<button type="button" id="encerrar"  onclick="window.location = '/principal/encerrar/{{ conteudo.getTema }}' "  class="btn ui-btn btn-danger">
							Terminar <span class="glyphicon glyphicon-off"></span>
						</button>
					</div>
					
					{% if existePular %}
					<div class="btn-group">
						<button  type="button" id="pular" data-toggle="modal" data-target="#pular_pergunta_modal" class="btn ui-btn btn-primary">
							Saltar <span class="glyphicon glyphicon-share-alt"></span>
						</button>
					</div>
					{% endif %}
					{% if existePulos %}
					<div class="btn-group">	
						<button  type="button" id="rever" data-toggle="modal" href="#" data-target="#questoes_saltadas_modal" class="btn ui-btn btn-primary">
							Rever Saltos <span class="glyphicon glyphicon-retweet"></span>
						</button>
					</div>
					{% endif %}
					{% if existeAjuda %}
					<div id="ajuda" class="btn-group">	
						<button  type="button" class="btn ui-btn btn-primary" data-toggle="modal" data-target="#ajuda_modal">
							Pedir Ajuda <span class="glyphicon glyphicon-question-sign"></span>
						</button>
					</div>
					{% endif %}
					<div class="btn-group">
						<button  type="button" id="responder" class="btn ui-btn btn-success">
							Responder <span class="glyphicon glyphicon-check"></span>
						</button>
					</div>
				</div>
			</div>
		{% endblock %}
		</center>

		<div class="font-dconteudo">
			{% block modals %}
				{% include 'usuario/modals/questoesSaltadas.php' %}
				{% include 'usuario/modals/ganhouBonus.php' %}
				{% include 'usuario/modals/ajuda.php' %}
				{% include 'usuario/modals/pularPergunta.php' %}
			{% endblock %}
		</div>

</div>
{% endblock %}

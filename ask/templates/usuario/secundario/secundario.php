{% extends 'usuario/cabecalhoUser.php' %}

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
					            		<h3 class="texto-azul">
					            			{{ conteudo.tema|safe|title }}
					            		</h3>
					            	</t>
					          	</center>
						  	</div>
						 	<div class="panel-footer">
						 		<div id="descricao-conteudo">
						  			<t><p class="lead">{{ conteudo.descricao|safe }}</p><t>
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
				  	<div class="panel-title" id="pontuacao-pergunta">
				  		<div class="text-center">
					 		<div class="row">
							{%  block pontuacao %}
								<div class="col-xs-4 col-sm-4 col-md-4">
									<div class="row">
										<h4>Pontos : {{ pontosAcumulados|default_if_none:"0" }}</h4>
									</div>	
								</div>
								<div class="col-xs-4 col-sm-4 col-md-4">
									<div class="row">
										<h4>Questão : {{ NUMEROPERGUNTA }} / {{ perguntasTotal|default_if_none:"0" }}</h4>
									</div>	
								</div>
								<div class="col-xs-4 col-sm-4 col-md-4">
									<div class="row">
										<h4>Saltos : {{ pulosRealizados|default_if_none:"0" }} / {{ pulosDisponiveis|default_if_none:"0" }}</h4>
									</div>	
								</div>
							{% endblock %}
							</div>
						</div>
				  	</div>
			  	<div class="panel-footer">
						{% block outros-conteudos-all %}
					  		<div class="espacamento">
								  <t><p class="lead">{{ pergunta.descricao|safe }}</p></t>
								<hr/>
								<form method="POST" id="perguntas" name="resposta">
								{%csrf_token %} 
									   <input id="pergunta_atual" name="pergunta_atual" value="{{pergunta.id}}" type="hidden"> 
									   <input id="conteudo_atual" name="conteudo_atual" value="{{conteudo.id}}" type="hidden">
									<ol>
									{% for chave , item in pergunta.getItens.items %}
										<li type="A">
											<div class="font-dconteudo">
												<input name="opcao" value='{{chave}}' required type="radio">
												<t class="lead">{{ item|safe }}</t>
											</div>
										</li>
										<br>
									{% empty %}
										<div class="font-dconteudo">
											<t><p class="lead">Essa pergunta não possui itens.</p></t>
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
			<div class="barra-responder navbar-fixed-bottom tela-opcoes-5">
				<div class="btn-group btn-group-justified fixer-bottom" role="toolbar">
					<div class="btn-group">
						<button type="button" id="encerrar"  onclick="window.location = '/principal/encerrar/{{ conteudo.getTema }}' "  class="btn ui-btn btn-danger">
							Terminar <span class="glyphicon glyphicon-off"></span>
						</button>
					</div>
					
					<div class="btn-group">
						{% if existePular == False %}
							<button  type="button" id="pular" data-toggle="modal" data-target="#pular_pergunta_modal" class="btn ui-btn btn-primary" disabled>
						{% else %}
							<button  type="button" id="pular" data-toggle="modal" data-target="#pular_pergunta_modal" class="btn ui-btn btn-primary">
						{% endif %}
						Saltar <span class="glyphicon glyphicon-share-alt"></span>
						</button>
					</div>


					<div class="btn-group">
					{% if existePulos == False %}
						<button  type="button" id="rever" data-toggle="modal" href="#" data-target="#questoes_saltadas_modal" class="btn ui-btn btn-primary" disabled>
						{% else %}
						<button  type="button" id="rever" data-toggle="modal" href="#" data-target="#questoes_saltadas_modal" class="btn ui-btn btn-primary">
						{% endif %}	
						Rever Saltos <span class="glyphicon glyphicon-retweet"></span>
						</button>
					</div>

					<div id="ajuda" class="btn-group">	
						{% if  existeAjuda == False %}
						<button  type="button" class="btn ui-btn btn-primary" data-toggle="modal" data-target="#ajuda_modal" disabled>
						{% else %}
						<button  type="button" class="btn ui-btn btn-primary" data-toggle="modal" data-target="#ajuda_modal">
						{% endif %}	
							Pedir Ajuda <span class="glyphicon glyphicon-question-sign"></span>
						</button>
					</div>

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

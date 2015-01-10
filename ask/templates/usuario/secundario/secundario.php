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

{% block conteudo-left %}
	<div class="font-dconteudo">
    	<div class="descricao-conteudo">
        		<div class="panel-heading">
        			<div class="panel panel-info">
					 	<div class="panel-title" id="tema-conteudo">
							<center>
				            	<t class="lead"><h3>{{ conteudo.tema|safe|title }}</t></h3>
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
					{%  block titulo-inicial-all %}
				 	<div class="panel-title" id="pontuacao">
				 		<center>
				 			<h3>
				 			{%  block titulo-inicial %}
					    		Essa Pergunta Vale {{ pergunta.pontos }} Pontos.
					    	{% endblock %}
					    	</h3>
					    </center>
				  	</div>
				  	{% endblock %}

				 	<div class="panel-footer">
				 		{%  block table-pontuacao-all %}
				 		<div  class="table-responsive">
							<table class="table table-bordered table-condensed">
								{%  block table-pontuacao %}
								<tr>
									<td class="text-center">PONTOS ACUMULADOS</td>
									<td class="text-center">TOTAL DE QUESTÕES</td>
									<td class="text-center">QUESTÕES CORRETAS</td>
									<td class="text-center">SALTOS DISPONÍVEIS</td>
									<td class="text-center">SALTOS REALIZADOS</td>
								</tr>
								<tr>
									<td class="text-center">{{ pontosAcumulados|default_if_none:"0" }}</td>
									<td class="text-center">{{ perguntasTotal|default_if_none:"0" }}</td>
									<td class="text-center">{{ perguntasCertas|default_if_none:"0" }}</td>
									<td class="text-center">{{ pulosDisponiveis|default_if_none:"0" }}</td>		
									<td class="text-center">{{ pulosRealizados|default_if_none:"0" }}</td>
								</tr>
								{% endblock %}
							</table>
						</div>
						{% endblock %}
						{% block outros-conteudos-all %}
				  		<div class="espacamento">
							  <t class="lead">{{ pergunta.descricao|safe }} </t>
							<hr/>
							<form method="POST" id="perguntas" name="resposta">
							{%csrf_token %} 
								   <input id="pergunta_atual" name="pergunta_atual" value="{{pergunta.id}}" type="hidden"> 
								   <input id="conteudo_atual" name="conteudo_atual" value="{{conteudo.id}}" type="hidden">
								<ol>
								{% for item in itens %}
									<li type="A">
										<div class="font-dconteudo">
											<input name="opcao" value="{{item.id|safe}}" required="" type="radio">
											<t class="lead">{{ item.descricao|safe }}</t>
										</div>
									</li>
									<br>
								{% empty %}
									<div class="font-dconteudo">
										<t class="lead">Essa pergunta nao possui itens.</t>
									</div>
								{% endfor %}
								</ol>
							</form>
				  		</div>
				  		{% endblock %}
				  	</div>
			  	</div>
			</div>
		</div>
		<center>
		{% block barra-inferior %}
			{% if existePular == False %}
				{% if existePulos == False %}
					{% if existeAjuda == False %}		
					<div class="barra-responder tela-opcoes-2">
					{% else %}
					<div class="barra-responder tela-opcoes-3">
					{% endif %}
				{% else %}
					{% if existeAjuda == False %}		
					<div class="barra-responder tela-opcoes-3">
					{% else %}
					<div class="barra-responder tela-opcoes-4">
					{% endif %}
				{% endif %}
			{% else %}
				{% if existePulos == False %}
					{% if existeAjuda == False %}		
					<div class="barra-responder tela-opcoes-3">
					{% else %}
					<div class="barra-responder tela-opcoes-4">
					{% endif %}
				{% else %}
					{% if existeAjuda == False %}		
					<div class="barra-responder tela-opcoes-4">
					{% else %}
					<div class="barra-responder tela-opcoes-5">
					{% endif %}
				{% endif %}
			{% endif %}
				<div class="btn-group btn-group-justified fixer-bottom" role="toolbar">
					<div class="btn-group">
						<button  type="button" id="encerrar"  onclick="window.location = '/principal/encerrar/{{ conteudo.getTema }}' "  class="btn btn-danger">
							Terminar <span class="glyphicon glyphicon-off"></span>
						</button>
					</div>
					
					{% if existePular %}
					<div class="btn-group">
						<button  type="button" id="pular" data-toggle="modal" data-target="#pular_pergunta_modal" class="btn btn-primary">
							Saltar <span class="glyphicon glyphicon-share-alt"></span>
						</button>
					</div>
					{% endif %}
					{% if existePulos %}
					<div class="btn-group">	
						<button  type="button" id="rever" data-toggle="modal" href="#" data-target="#questoes_saltadas_modal"	  class="btn btn-primary">
							Rever Saltos <span class="glyphicon glyphicon-retweet"></span>
						</button>
					</div>
					{% endif %}
					{% if existeAjuda %}
					<div id="ajuda" class="btn-group">	
						<button  type="button" class="btn btn-primary" data-toggle="modal" data-target="#ajuda_modal">
							Pedir Ajuda <span class="glyphicon glyphicon-question-sign"></span>
						</button>
					</div>
					{% endif %}
					<div class="btn-group">
						<button  type="button" id="responder" class="btn btn-success ">
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

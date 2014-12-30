{% extends 'usuario/cabecalhoUser.php' %}

{% block titulo %}{{conteudo.tema}}{% endblock %}

{% block estilo %}
	#conteudo{
		background-color: #428bca;
	}
{% endblock %}

{% block funcoes %}
	$(document).ready(function(){
		$(".panel-heading").css("height", "100%");
		$(".jspPane").css("height", "100%");
		$("#requisitos").css("height", "100%");


	});
{% endblock %}

{% block voltar_all %}{% endblock %}

{% block conteudo-left %}
	<div class="font-dconteudo">
    	<div class="descricao-conteudo">
        		<div class="panel-heading">
        			<div class="panel panel-info">
					 	<div class="panel-title">
							<center>
				            	<h3>{{ conteudo.tema }}</h3>
				          	</center>
					  	</div>
					 	<div class="panel-footer">
					 		<div id="descricao-conteudo">
					  		<t> {{ conteudo.descricao|safe }}<t>
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
				 	<div class="panel-title pontuacao">
				 		<center>
					    		<h3>Pergunta</h3>
					    </center>
				  	</div>

				 	<div class="panel-footer">
				 		<div  class="table-responsive">
							<table class="table table-hover table-bordered">
								<tr>
									<td class="text-center">
										PONTOS ACUMULADOS = {{ pontosAcumulados }}
									</td>
									<td class="text-center">
										SALTOS REALIZADOS = {{ pulosRealizados }}
									</td>
									<td class="text-center">
										SALTOS DISPONIVEIS = {{ pulosDisponiveis }}
									</td>
									<td class="text-center">
										QUESTOES CORRETAS = {{ perguntasCertas }}/{{ perguntasTotal }}
									</td>
								</tr>
							</table>
						</div>
				  		<div class="espacamento">
							  <t> {{ pergunta.descricao|safe }} </t>
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
											<t>{{ item.descricao | safe }}</t>
										</div>
									</li>
									<br>
								{% endfor %}
								</ol>
							</form>
				  		</div>
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

				

			<div class="btn-group btn-group-justified fixer-bottom">
				<div class="btn-group">
					<button  type="button" id="encerrar"  onclick="window.location = '/principal/encerrar/{{ conteudo.getTema }}' "  class="btn btn-danger">Encerrar Licao</button>
				</div>
				
				{% if existePular %}
				<div class="btn-group">
					<button  type="button" id="pular"     class="btn btn-primary">Saltar</button>
				</div>
				{% endif %}
				{% if existePulos %}
				<div class="btn-group">	
					<button  type="button" id="rever" data-toggle="modal" href="#" data-target="#questoes_saltadas_modal"	  class="btn btn-primary">Rever Saltos</button>
				</div>
				{% endif %}
				{% if existeAjuda %}
				<div id="ajuda" class="btn-group">	
					<button  type="button" class="btn btn-primary" data-toggle="modal" data-target="#ajuda_modal">Pedir Ajuda</button>
				</div>
				{% endif %}
				<div class="btn-group">
					<button  type="button" id="responder" class="btn btn-success ">Responder</button>
				</div>
			</div>
		</div>
		{% endblock %}
		</center>
		{% include 'usuario/modals/questoesSaltadas.php' %}

		<!-- Modal Ajuda -->
		<div class="modal fade" id="ajuda_modal" tabindex="-1" role="dialog" aria-labelledby="contatoLabel" aria-hidden="true">
		  	<div class="modal-dialog">
				<div class="modal-content">
				    <div class="modal-header">
				        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
				        <h4 class="modal-title" id="myModalLabel">Ajuda</h4>
				    </div>
				    <div class="modal-body">
				    	<div class="text-justify">
							<t id="ajuda_text">
				      		</t>
			      		</div>
					</div>

					<div class="modal-footer">
						<center>
							<div class="tela-opcoes-1">
								<div class="btn-group btn-group-justified ">
									<div class="btn-group">
										<button type="button" class="btn btn-primary" data-dismiss="modal">Sair</button>
									</div>
								</div>
							</div>
						</center>
					</div>
				</div>
		  	</div>
		</div>
		<!-- end modal  -->

</div>

{% endblock %}

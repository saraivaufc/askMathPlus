{% extends 'usuario/secundario/secundario.php' %}

{% block conteudo-right %}
	<div class="font-dconteudo">
    	<div class="descricao-pergunta">
        		<div class="panel-heading">
	        		<div class="panel panel-info">
					 	<div class="panel-title">
							<center>
								{%  block titulo-inicial %}
				            		<h3>Sobre esta Licao</h3>
								{% endblock %}
				          	</center>
					  	</div>
					 	<div class="panel-footer">
					 		{%  block table-pontuacao-all %}
					 		<div class="table-responsive">
								<table class="table table-hover table-bordered">
									{%  block table-pontuacao %}
									<tr>
										<td class="text-center">
											NUMERO DE QUESTOES
										</td>
										<td class="text-center">
											{{ conteudo.getQuantPerguntasTotal }}
										</td>
									</tr>
									<tr>
										<td class="text-center">
											SALTOS DISPONIVEIS
										</td>
										<td class="text-center">
											{{ conteudo.max_pulos }}
										</td>
									</tr>
									{% endblock %}
								</table>
							</div>
							{% endblock %}
							<br>
							{% block outros-conteudos-all %}
							<div id="requisitos">
								<div class="list-group">
									{% block outros-conteudos %}
										<a data-toggle="modal" href="#" data-target="#requisitos_modal" class="list-group-item active">
										    REQUISITOS(*)
										</a>
										{% for c in conteudo.getRequisitos %}
											<a  onclick="window.open('/principal/opcoes/{{ c.getTema }}')" href="#" class="list-group-item">{{ c.tema }}</a>
										{% endfor %}
									{% endblock %}
								</div>
							</div>
							{% endblock %}
						</div>
					</div>
				</div>
		</div>

    	<center>
    		{%  block barra-inferior %}
    		{% if existePulos == False %}
	    		<div class="barra-responder tela-opcoes-2">
	    	{% else %}
	    		<div class="barra-responder tela-opcoes-3">
	    	{% endif %}
					<div class="btn-group btn-group-justified fixer-bottom">
						<div class="btn-group">
							<button  type="button"  onclick="window.location='/principal/'" class="btn btn-primary">
								Voltar Inicio
							</button>
						</div>
						<div class="btn-group">
							<button  type="button"  onclick="window.location='/principal/{{ conteudo.getTema }}'" class="btn btn-success">
								{% if respondeuPergunta %}
									Refazer Licao
								{% else %}
									Iniciar Licao
								{% endif %}
							</button>
						</div>
						{% if existePulos %}
							<div class="btn-group">
								<button type="button"  data-toggle="modal" href="#" data-target="#questoes_saltadas_modal" class="btn btn-primary">Rever Saltos</button>
							</div>
						{% endif %}
						
					</div>
			</div>
			{% endblock %}
		</center>

		{% include 'usuario/modals/questoesSaltadas.php' %}

		{% block modal-outros-conteudos %}
		<!-- Modal Requisitos -->
		<div class="modal fade" id="requisitos_modal" tabindex="-1" role="dialog" aria-labelledby="requisitosLabel" aria-hidden="true">
		  	<div class="modal-dialog">
				<div class="modal-content">
				    <div class="modal-header">
				        <h4 class="modal-title" id="myModalLabel">Sobre a escolha dos Requisitos</h4>
				    </div>
				    <div class="modal-body">
						<div class="text-justify">
							fazer depois
						</div>
					</div>

					<div class="modal-footer">
						<center>
							<div class="tela-opcoes-1">
								<div class="btn-group btn-group-justified ">
									<div class="btn-group">
										<button type="button" class="btn btn-primary" data-dismiss="modal">Fechar</button>
									</div>
								</div>
							</div>
						</center>
					</div>
				</div>
		  	</div>
		</div>
		<!-- Fim do Modal Rquisitos-->
		{% endblock %}

	</div>
{% endblock %}
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
					 		<div class="table-responsive">
								<table class="table table-hover table-bordered">
									{%  block table-pontuacao %}
									<tr class="success">
										<td class="text-center">
											NUMERO DE QUESTOES = {{ conteudo.getQuantPerguntasTotal }}
										</td>
										<td class="text-center">
											SALTOS DISPONIVEIS = {{ conteudo.max_pulos }}
										</td>
									</tr>
									{% endblock %}
								</table>
							</div>
							<br>
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
						</div>
					</div>
				</div>
		</div>

    	<center>
    		{%  block barra-inferior %}
    		{% if existePulos == False %}
	    		<div class="barra-responder tela-opcoes-1">
	    	{% else %}
	    		<div class="barra-responder tela-opcoes-2">
	    	{% endif %}
					<div class="btn-group btn-group-justified fixer-bottom">
						{% if existePulos %}
							<div class="btn-group">
								<button  type="button" class="btn btn-primary">Rever Questoes Saltadas</button>
							</div>
						{% endif %}
						<div class="btn-group">
							<button  type="button"  onclick="window.location='/principal/{{ conteudo.getTema }}'" class="btn btn-success">
								{% if respondeuPergunta %}
									Refazer Licao
								{% else %}
									Iniciar Licao
								{% endif %}
							</button>
						</div>
						
					</div>
			</div>
			{% endblock %}
		</center>
		{% block modal-outros-conteudos %}
		<!-- Modal Requisitos -->
		<div class="modal fade" id="requisitos_modal" tabindex="-1" role="dialog" aria-labelledby="requisitosLabel" aria-hidden="true">
		  	<div class="modal-dialog">
				<div class="modal-content">
				    <div class="modal-header">
				        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
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
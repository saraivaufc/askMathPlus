{% extends 'usuario/secundario/secundario.php' %}

{% block conteudo-right %}
	<div class="font-dconteudo">
    	<div class="descricao-pergunta">
        		<div class="panel-heading">
	        		<div class="panel panel-info">
					 	<div class="panel-title">
							<center>
				            	<h3>Detalhes</h3>
				          	</center>
					  	</div>
					 	<div class="panel-footer">
					 		<div class="table-responsive">
								<table class="table table-hover table-bordered">
									<tr>
										<td class="text-center">
											NUMERO DE QUESTOES = 20
										</td>
										<td class="text-center">
											SALTOS DISPONIVEIS = 112
										</td>
									</tr>
								</table>
							</div>
							<br>
							<div id="requisitos">
								<div class="list-group">
									<a data-toggle="modal" href="#" data-target="#requisitos_modal" class="list-group-item active">
									    Requisitos(*)
									</a>
									{% for c in conteudo.getRequisitos %}
										<a href="/principal/opcoes/{{ c.tema }}" class="list-group-item">{{ c.tema }}</a>
									{% endfor %}
								</div>
							</div>
						</div>
					</div>
				</div>
		</div>

    	<center>
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
							<button  type="button"  onclick="window.location = '/principal/{{ conteudo.getTema }}'" class="btn btn-success">Iniciar Secao</button>
						</div>
						
					</div>
			</div>
		</center>

		<div class="modal fade" id="requisitos_modal" tabindex="-1" role="dialog" aria-labelledby="contatoLabel" aria-hidden="true">
		  	<div class="modal-dialog">
				<div class="modal-content">
				    <div class="modal-header">
				        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
				        <h4 class="modal-title" id="myModalLabel">Sobre os Requisitos</h4>
				    </div>
				    <div class="modal-body">
						<center>
							A escolha desses requisitos foram baseadas em aleatoriedade
						</center>
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

	</div>
{% endblock %}
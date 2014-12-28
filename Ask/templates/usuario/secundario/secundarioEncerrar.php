{% extends 'usuario/secundario/secundario.php' %}

{% block conteudo-right %}
	<div class="font-dconteudo">
    	<div class="descricao-pergunta">
        		<div class="panel-heading">
	        		<div class="panel panel-info">
					 	<div class="panel-title">
							<center>
				            	<h3>Seu Andamento na Liçao</h3>
				          	</center>
					  	</div>
					 	<div class="panel-footer">
					 		<div class="table-responsive">
								<table class="table table-hover table-bordered">
									<tr class="success">
										<td class="text-center">
											QUESTOES SALTADAS = {{ questoesPuladas }}
										</td>
										<td class="text-center">
											QUESTOES CORRETAS = {{ questoesCorretas }}
										</td>
										<td class="text-center">
											QUESTOES ERRADAS = {{ questoesErradas }}
										</td>
										<td class="text-center">
											VEZES QUE PEDIU AJUDA = {{ vezesPediuAjuda }}
										</td>
									</tr>
								</table>
							</div>
							<br>
							<div id="requisitos">
								<div class="list-group">
									<a data-toggle="modal" href="#" data-target="#sugestoes_modal" class="list-group-item active">
									    SUGESTOES DE ESTUDOS(*)
									</a>
									{% for c in conteudo.getSugestoes %}
										<a  onclick="window.open('/principal/opcoes/{{ c.getTema }}')" href="/principal/opcoes/{{ c.getTema }}" class="list-group-item">{{ c.tema }}</a>
									{% endfor %}
								</div>
							</div>
						</div>
					</div>
				</div>
		</div>

    	<center>
	    	<div class="barra-responder tela-opcoes-1">
				<div class="btn-group btn-group-justified fixer-bottom">
					<div class="btn-group">
						<button  type="button"  onclick="window.location='/principal/'" class="btn btn-danger">
							Sair
						</button>
					</div>
					
				</div>
			</div>
		</center>

		<!-- Modal Requisitos -->
		<div class="modal fade" id="sugestoes_modal" tabindex="-1" role="dialog" aria-labelledby="requisitosLabel" aria-hidden="true">
		  	<div class="modal-dialog">
				<div class="modal-content">
				    <div class="modal-header">
				        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
				        <h4 class="modal-title" id="myModalLabel">Sobre a escolha das Sugestoes</h4>
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

	</div>
{% endblock %}
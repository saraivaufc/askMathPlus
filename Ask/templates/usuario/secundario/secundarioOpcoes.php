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
									<td>
										NUMERO DE QUESTOES = 20
									</td>
									<td>
										SALTOS DISPONIVEIS = 112
									</td>
								</tr>
							</table>
							<div id="requisitos">
							<div class="list-group">
								<a href="#" class="list-group-item active">
								    Requisitos(*)
								</a>
								{% for c in conteudo.getRequisitos %}
									<a href="#" class="list-group-item">{{ c.tema }}</a>
								{% endfor %}
							</div>
							</div>

						</div>
				  	</div>
				  	</div>
				</div>
    	</div>
    	<center>
    	<div class="barra-responder tela-opcoes">
				<div class="btn-group btn-group-justified fixer-bottom">
					<div class="btn-group">
						<button  type="button" onclick="window.location = '/principal/' " class="btn btn-primary">Voltar</button>
					</div>
					<div class="btn-group">
						<button  type="button" id="pular" class="btn btn-primary">Rever Questoes Saltadas</button>
					</div>
					<div class="btn-group">
						<button  type="button" id="pular" class="btn btn-success">Iniciar Secao</button>
					</div>
					
				</div>
		</div>
		</center>
  	</div>
{% endblock %}
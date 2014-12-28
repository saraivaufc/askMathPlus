{% extends 'usuario/secundario/secundarioOpcoes.php' %}

{% block titulo-inicial  %}
	<h3>Seu Andamento na Liçao</h3>
{% endblock %}

{% block table-pontuacao %}
	<tr class="success">
		<td class="text-center">
			QUESTOES TOTAL = {{ conteudo.getQuantPerguntasTotal }}
		</td>
		<td class="text-center">
			QUESTOES CORRETAS = {{ questoesCorretas }}
		</td>
		<td class="text-center">
			QUESTOES ERRADAS = {{ questoesErradas }}
		</td>
		<td class="text-center">
			QUESTOES SALTADAS = {{ questoesPuladas }}
		</td>
		<td class="text-center">
			VEZES QUE PEDIU AJUDA = {{ vezesPediuAjuda }}
		</td>
	</tr>
{% endblock %}

{% block outros-conteudos %}
	<a data-toggle="modal" href="#" data-target="#sugestoes_modal" class="list-group-item active">
	    SUGESTOES DE ESTUDOS(*)
	</a>
	{% for c in conteudo.getSugestoes %}
		<a  onclick="window.open('/principal/opcoes/{{ c.getTema }}')" href="#" class="list-group-item">{{ c.tema }}</a>
	{% endfor %}
{% endblock %}

{%  block barra-inferior %}
	<div class="barra-responder tela-opcoes-2">
				<div class="btn-group btn-group-justified fixer-bottom">
					<div class="btn-group">
						<button  type="button"  onclick="window.location='/principal/'" class="btn btn-danger">
							Encerrar Inicio
						</button>
					</div>
					<div class="btn-group">
						<button  type="button"  onclick="window.location='/principal/{{ conteudo.getTema }}'" class="btn btn-success">
							Continuar com Licao
						</button>
					</div>
				</div>
	</div>
{% endblock %}


{% block modal-outros-conteudos %}
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
{% endblock %}
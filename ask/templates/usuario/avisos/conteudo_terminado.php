{% extends 'usuario/secundario/secundarioOpcoes.php' %}

{% block titulo-inicial  %}
	<h3>Licao Concluida Com Exito</h3>
{% endblock %}

{% block table-pontuacao %}
	<tr>
		<td class="text-center">
			QUESTOES TOTAL = {{ conteudo.getQuantPerguntasTotal }}
		</td>
	</tr>
	<tr>
		<td class="text-center">
			PULOS REALIZADOS = {{ pulosRealizados }}
		</td>
	</tr>
	<tr>
		<td class="text-center">
			VEZES QUE PEDIU AJUDA = {{ vezesPediuAjuda }}
		</td>
	</tr>
	<tr>
		<td class="text-center">
			PONTOS ACUMULADOS = {{ pontosAcumulados }}
		</td>
	</tr>
{% endblock %}

{% block outros-conteudos-all %}

{% endblock %}

{%  block barra-inferior %}
	<div class="barra-responder tela-opcoes-1">
				<div class="btn-group btn-group-justified fixer-bottom">
					<div class="btn-group">
						<button  type="button"  onclick="window.location='/principal/'" class="btn btn-primary">
							Voltar Inicio
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
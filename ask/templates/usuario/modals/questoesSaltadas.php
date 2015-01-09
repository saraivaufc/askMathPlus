<!-- Modal Requisitos -->
<div class="modal fade" id="questoes_saltadas_modal" tabindex="-1" role="dialog" aria-labelledby="requisitosLabel" aria-hidden="true">
  	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header text-center">
		        <h3 class="modal-title text-center" id="myModalLabel">{{ conteudo.tema|title }}</h3>
		    </div>

		    <div class="modal-body">
				<div class="text-justify">
					<div class="list-group">
						<a class="list-group-item active text-center ">
							    Questões Saltadas
						</a>
							{% for p in perguntasSaltadas %}
								<a href="/irPergunta/{{ p.id }}/" class="list-group-item">
									<t>
										{{ p.getDescricao|safe }}
									</t>
								</a>
							{% empty %}
							<a class="list-group-item list-group-item-warning">Nao existe Perguntas Saltadas.</a>
							{% endfor %}
					</div>
				</div>
			</div>

			<div class="modal-footer">
				<center>
					<div class="tela-opcoes-1">
						<div class="btn-group btn-group-justified ">
							<div class="btn-group">
								<button type="button" class="btn btn-primary" data-dismiss="modal">
									Fechar <span class="glyphicon glyphicon-remove"></span>
								</button>
							</div>
						</div>
					</div>
				</center>
			</div>
		</div>
  	</div>
</div>
<!-- Fim do Modal Rquisitos-->

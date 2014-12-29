<!-- Modal Requisitos -->
<div class="modal fade" id="questoes_saltadas_modal" tabindex="-1" role="dialog" aria-labelledby="requisitosLabel" aria-hidden="true">
  	<div class="modal-dialog">
		<div class="modal-content">
		    <div class="modal-header">
		        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
		        <h4 class="modal-title" id="myModalLabel">Questoes que Voce Saltou</h4>
		    </div>
		    <div class="modal-body">
				<div class="text-justify">
					<div class="list-group">
						<a data-toggle="modal" href="#" data-target="#requisitos_modal" class="list-group-item active">
							    Questoes Saltadas
						</a>
							{% for p in perguntasSaltadas %}
								<a href="/irPergunta/{{ p.id }}/" class="list-group-item">{{ p.getDescricao }}</a>
							{% endfor %}
					</div>
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
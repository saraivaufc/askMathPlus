<!-- Modal Detalhes Pergunta -->
<div class="modal fade" id="detalhes_pergunta_modal" tabindex="-1" role="dialog" aria-labelledby="contatoLabel" aria-hidden="true">
  	<div class="modal-dialog">
		<div class="modal-content">
		    <div class="modal-header">
		        <h2 class="modal-title text-center" id="myModalLabel">{{conteudo.tema}}</h2>
		    </div>
		    <div class="modal-body">
		    	<table class="table table-bordered">
		    		<caption>Sobre a Pontuacao</caption>
					<tr class="active">
						</td><td>Pontos</td>
					</tr>
						<td>
							{{pergunta.pontos}}
						</td>
					</tr>
				</table>

				<hr/>

				<table class="table table-bordered table-hover">
					<caption>Item Correto</caption>
					<tr class="info">
						</td><td>Descriçao</td>
					</tr>
						{% if pergunta.item_correto_id == None %}
						<tr class="danger link">
				  			<td>
				  				Nao Existe Item Correto.
				  			</td>
				  		{% else %}
				  		<tr>
				  			<td onClick="document.location = '/principal_admin/{{ tema_conteudo }}/{{pergunta_inicial.id}}/'">
				  				{{ pergunta.getItemCorreto.getDescricao }}
				  			</td>
				  		{% endif %}
					</tr>
				</table>


				<table class="table table-bordered table-hover">
					<caption>Pergunta Anterior</caption>
					<tr class="info">
						</td><td>Descriçao</td>
					</tr>
						{% if existeAnterior == False %}
						<tr class="danger link">
				  			<td>
				  				Nao Existe Pergunta Anterior.
				  			</td>
				  		{% else %}
				  		<tr>
				  			<td onClick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaAnterior.id}}'">
				  				{{ perguntaAnterior.getDescricao }}
				  			</td>
				  		{% endif %}
					</tr>
				</table>

				<table class="table table-bordered table-hover">
					<caption>Pergunta Próxima</caption>
					<tr class="info">
						</td><td>Descriçao</td>
					</tr>
						{% if existeProximo == False %}
						<tr class="danger link">
				  			<td>
				  				Nao Existe Pergunta Proxima.
				  			</td>
				  		{% else %}
				  		<tr>
				  			<td onClick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaProximo.id}}'">
				  				{{ perguntaProximo.getDescricao }}
				  			</td>
				  		{% endif %}
					</tr>
				</table>

			</div>

			<div class="modal-footer">
				<center>
					<div class="tela-opcoes-1">
						<div class="btn-group btn-group-justified">
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
<!-- end modal  -->

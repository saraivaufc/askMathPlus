<!-- Modal Detalhes Pergunta -->
<div class="modal fade" id="detalhes_pergunta_modal" tabindex="-1" role="dialog" aria-labelledby="contatoLabel" aria-hidden="true">
  	<div class="modal-dialog">
		<div class="modal-content">
		    <div class="modal-header">
		        <h2 class="modal-title text-center" id="myModalLabel">{{conteudo.tema}}</h2>
		    </div>
		    <div class="modal-body">
		    	<table class="table table-bordered">
		    		<h3>Sobre a Pontuacao</h3>
					<tr class="active">
						</td><td>Pontos</td>
					</tr>
					<tr>
						<td>
							{{pergunta.pontos}}
						</td>
					</tr>
				</table>

				<hr/>
				<h3>Mais Detalhes</h3>
				<div class="list-group">
				  	<a  class="list-group-item active">
				    	Item Correto
				  	</a>
				  		{% if pergunta.item_correto_id == None %}
				  			<a class="list-group-item list-group-item-danger">
				  			Nao Existe Item Correto...
				  		{% else %}
				  			<a class="list-group-item">
				  			{{ pergunta.getItemCorreto.getDescricao }}
				  		{% endif %}
				  	</a>

				  	<a></a>

				  	<a class="list-group-item active">
				    	Pergunta Anterior
				  	</a>
				  		{% if existeAnterior == False %}
				  			<a class="list-group-item list-group-item-danger">
				  			Nao Existe Pergunta Anterior...
				  		{% else %}
				  			<a onclick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaAnterior.id}}'" class="list-group-item">
				  			{{ perguntaAnterior.getDescricao }}
				  		{% endif %}
				  	</a>

				  	<a></a>

				  	<a class="list-group-item active">
				    	Pergunta Próximo
				  	</a>
				  		{% if existeProximo == False %}
				  			<a class="list-group-item list-group-item-danger">
				  			Nao Existe Pergunta Proxima...
				  		{% else %}
				  			<a onclick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaProximo.id}}'" class="list-group-item">
				  			{{ perguntaProximo.getDescricao }}
				  		{% endif %}
				  	</a>


				</div>



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

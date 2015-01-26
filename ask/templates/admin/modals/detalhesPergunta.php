<!-- Modal Detalhes Pergunta -->
<div class="modal fade" id="detalhes_pergunta_modal" tabindex="-1" role="dialog" aria-labelledby="contatoLabel" aria-hidden="true">
  	<div class="modal-dialog">
		<div class="modal-content">
		    <div class="modal-header">
		        <h2 class="modal-title text-center" id="myModalLabel">{{conteudo.tema|title}}</h2>
		    </div>
		    <div class="modal-body">
		    	<table class="table table-bordered">
		    		<caption>Sobre a Pontuacao</caption>
					<tr class="info">
						</td><td>Pontos</td>
					</tr>
						<td>
							{{pergunta.pontos|default_if_none:"0"}}
						</td>
					</tr>
				</table>

				<hr/>

				<table class="table table-bordered table-hover">
					<caption>Item Correto</caption>
					<tr class="info">
						</td><td>Descriçao</td>
					</tr>
						{% if pergunta.getDescricaoItemCorreto == None %}
						<tr class="danger link">
				  			<td>
				  				Nao Existe Item Correto.
				  			</td>
				  		{% else %}
				  		<tr>
				  			<td class="text-justify">
				  				<t>{{ pergunta.getDescricaoItemCorreto|safe|truncatechars_html:80 }}</t>
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
				  		<tr class="pointer  text-justify">
				  			<td onClick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaAnterior.id}}'">
				  				<t>{{ perguntaAnterior.getDescricao|safe|truncatechars_html:80 }}</t>
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
				  		<tr class="pointer text-justify ">
				  			<td onClick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaProximo.id}}'">
				  				<t>{{ perguntaProximo.getDescricao|safe|truncatechars_html:80 }}</t>
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

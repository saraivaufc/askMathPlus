<!-- Modal Detalhes Conteduo -->
<div class="modal fade" id="detalhes_conteudo_modal" tabindex="-1" role="dialog" aria-labelledby="contatoLabel" aria-hidden="true">
  	<div class="modal-dialog">
		<div class="modal-content">
		    <div class="modal-header">
		        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
		        <h2 class="modal-title text-center" id="myModalLabel">{{conteudo.tema}}</h2>
		    </div>
		    <div class="modal-body">
		    	<table class="table table-bordered">
		    		<h3>Turmas</h3>
					<tr class="info">
						</td><td>Semestre</td><td>Disciplina</td><td>Professor</td>
					</tr>

					{% for i in turmas %}
						<tr>
							<td>
								{{i.semestre}}
							</td>
							<td>
								{{i.disciplina}}
							</td>
							<td>
								{{i.professor}}
							</td>
						</tr>
					{% endfor %}
				</table>


				<hr/>

				<table class="table table-bordered">
		    		<h3>Mais Detalhes</h3>
					<tr class="info">
						</td><td>Numero de Questoes</td><td>Maximo de Pulos Permitido</td>
					</tr>
					<tr>
						<td>
							{{ conteudo.getQuantPerguntasTotal }}
						</td>
						<td>
							{{ conteudo.max_pulos }}
						</td>
					</tr>
				</table>

				<hr/>

				<div class="list-group">
				  	<a class="list-group-item active">
				    	Pergunta Inicial
				  	</a>
				  		{% if pergunta_inicial == None %}
				  			<a class="list-group-item list-group-item-danger">
				  			Nenhuma Pergunta Inicial
				  		{% else %}
				  			<a class="list-group-item">
				  			{{pergunta_inicial.getDescricao}}
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
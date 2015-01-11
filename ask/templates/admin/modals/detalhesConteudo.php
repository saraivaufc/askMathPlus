<!-- Modal Detalhes Conteduo -->
<div class="modal fade" id="detalhes_conteudo_modal" tabindex="-1" role="dialog" aria-labelledby="contatoLabel" aria-hidden="true">
  	<div class="modal-dialog">
		<div class="modal-content">
		    <div class="modal-header">
		        <h2 class="modal-title text-center" id="myModalLabel">{{conteudo.tema|title}}</h2>
		    </div>
		    <div class="modal-body">
		    	<table class="table table-bordered table-hover">
		    		<caption>Turmas</caption>
					<tr class="info text-center">
						</td><td>Semestre</td><td>Disciplina</td><td>Professor</td>
					</tr>

					{% for i in turmas %}
						<tr class="text-center">
							<td>
								{{i.semestre|default_if_none:"Nenhum"}}
							</td>
							<td>
								{{i.disciplina}}
							</td>
							<td>
								{{i.professor}}
							</td>
						</tr>
					{% empty %}
					<tr class="warning">
						<td colspan="3"><div class="text-center">Essa licao nao pertence a nenhuma turma.</div></td>
					</tr>
					{% endfor %}
				</table>


				<hr/>

				<table class="table table-bordered table-hover">
					<caption>Mais Detalhes</caption>
					<tr class="info text-center">
						</td><td>Número de Questões</td><td>Máximo de Pulos Permitido</td>
					</tr>
					<tr class="text-center">
						<td>
							{{ conteudo.getQuantPerguntasTotal|default_if_none:"0" }}
						</td>
						<td>
							{{ conteudo.max_pulos|default_if_none:"0" }}
						</td>
					</tr>
				</table>

				<hr/>

				<table class="table table-bordered table-hover">
					<caption>Pergunta Inicial</caption>
					<tr class="info text-center">
						</td><td>Descriçao</td>
					</tr>
						{% if pergunta_inicial == None %}
						<tr class="danger link text-center">
				  			<td>
				  				Nenhuma Pergunta Inicial.
				  			</td>
				  		{% else %}
				  		<tr>
				  			<td onClick="document.location = '/principal_admin/{{ tema_conteudo }}/{{pergunta_inicial.id}}/'">
				  				<t>{{ pergunta_inicial.getDescricao|safe }}</t>
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
									Fechar <span class="glyphicon glyphicon-remove hidden-xs"></span>
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

<div id="disciplinas" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
	<div class="modal-content">
	  
	  	<div class="modal-body">
	  		<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
			<h3 id="myModalLabel">Escolha uma disciplina.</h3>
			<center>
				<div>
				<form  class="form-horizontal" role="form" action="/principal/" method="POST">{% csrf_token %}
					<div class="table-responsive">
					<table id="disciplinas" class="table table-bordered disciplinas">
						<tr class="info active text-center">
							<td>Escolher</td><td>Nome</td>
						</tr>
					</table>
					</div>
						<div class="btn-group btn-group-justified tela-opcoes-1">
							<div class="btn-group">
								<button type="submit" class="btn ui-btn btn-primary">
									Escolher <span class="glyphicon glyphicon-ok-circle hidden-xs"></span>
								</button>
							</div>
						</div>
				</form>
				</div>
			</center>
		</div>
	</div>
  </div>
</div>
	<!--  Fim Modal Contatos -->
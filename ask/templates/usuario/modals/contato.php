<!-- Modal Contato -->
	<div class="modal fade" id="contato" tabindex="-1" role="dialog" aria-labelledby="contatoLabel" aria-hidden="true">
	  <div class="modal-dialog">
	    <div class="modal-content">
	      <div class="modal-header">
	        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
	        <h3 class="modal-title text-center" id="myModalLabel">Entrar em Contato</h3>
	      </div>
	      <div class="modal-body">
			<center>
			<div class="form-contato">
				<form class="form-horizontal" method="post" action="/contato/" role="form">{% csrf_token %}

					<input type="hidden" id="page_atual" name="page_atual" value={% block page_atual %}"/principal/"{% endblock %}>
					<div class="modal-body">
						<div class="form-group">
							<label class="row-sm-4 control-label">Nome</label>
							<div class="row-sm-8">
								<input type="text" class="form-control" name="nome" autofocus required>
							</div>
						</div>
						<div class="form-group">
							<label class="row-sm-4 control-label">Email</label>
							<div class="row-sm-8">
							<input type="email" class="form-control" name="email" required>
							</div>
						</div>
						<div class="form-group">
							<label class="row-sm-4 control-label">Mensagem</label>
							<div class="row-sm-8">
								<textarea class="form-control" name="mensagem" required></textarea>
							</div>
						</div>
					</div>
					</div>
					<div class="modal-footer">
						<center>
							<div class="btn-group btn-group-justified tela-opcoes-2">
								<div class="btn-group">
									<button type="button" class="btn btn-default" data-dismiss="modal">Cancelar</button>
								</div>
								<div class="btn-group">
									<button type="submit" class="btn btn-primary" >Enviar</button>
								</div>
							</div>
						</center>
					</div>
				</form>
			</div>
			
			</center>
			
		</div>
	  </div>
	</div>
	<!--  Fim Modal Contatos -->
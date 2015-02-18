<div id="contato" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
	<div class="modal-content">
	  
	  	<div class="modal-body">
	  		<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
			<h3 id="myModalLabel">Gostaríamos muito de ouvir de você</h3>
	  		
			<form class="form-horizontal col-sm-12"  action="/contato/" method="POST">{% csrf_token %}
				<br>
				<div class="form-group">
					<label>Nome</label>
					<input class="form-control required" placeholder="Seu nome" name="name" data-placement="top" data-trigger="manual" data-content="Deve ter pelo menos 3 caracteres, e deve conter apenas letras." type="text" required>
				</div>

				<div class="form-group">
					<label>Mensagem</label>
					<textarea class="form-control" placeholder="Sua mensagem aqui..." name="messager" data-placement="top" data-trigger="manual" required></textarea>
				</div>
			  
				<div class="form-group">
					<label>E-Mail</label>
					<input class="form-control email" placeholder="email@service.com (para que possamos entrar em contato com você)" name="email" data-placement="top" data-trigger="manual" data-content="Deve ser um endereço de e-mail válido (usuario@gmail.com)" type="text" required>
				</div>
			  
				<div class="form-group">
					<button type="submit" class="btn btn-success pull-right">Enviar!</button>
					<p class="help-block pull-left text-danger hide" id="form-error">&nbsp; O Formulário não é válido. </p>
				</div>			
			</form>
			<div class="modal-footer">
				<button class="btn" data-dismiss="modal" aria-hidden="true">Cancelar</button>
			</div>
		</div>
	</div>
  </div>
</div>
	<!--  Fim Modal Contatos -->

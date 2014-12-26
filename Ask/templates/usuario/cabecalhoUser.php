{% extends 'basico.php' %}

{% block menu %}
<div id="barra-menu">
    <div class="nav navbar bg-primary">
        <div class="container-fluid">
          	<div class="navbar-header">
            	<a class="navbar-brand" href="/principal/">Principal</a>
          	</div>
	        <div>
	            <ul class="nav navbar-nav">
	            	{% block botoes_adicionais_esq %}
			            <li><a onclick="window.open('/forum')"  href="#">Forum</a></li>
	            	{% endblock %}
	            </ul>
	            
	            <ul class="nav navbar-nav navbar-right">
	        	  	{% block voltar_all %}
	             		<li id="voltar"><a onclick="document.location = '{% block voltar %}/principal/{% endblock %}'" href="#">Voltar</a></li>
	              	{% endblock %}
	              	<li><a data-toggle="modal" data-target="#contato" href="#">Contato</a></li>
	             	 <li><a data-toggle="modal" data-target="#sobre" href="#">Sobre</a></li>
	              	{% block sair_all %}
	              		<li><a  href="/logout/">Sair</a></li>
	              	{% endblock %}
	            </ul>
	        </div><!--/.nav-collapse -->
        </div><!--/.container-fluid -->
    </div><!--/.nav navbar -->
</div><!-- /.barra-menu -->

<!-- Modal Contato -->
<div class="modal fade" id="contato" tabindex="-1" role="dialog" aria-labelledby="contatoLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title" id="myModalLabel">Entrar em Contato</h4>
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
				<div class="modal-footer">
					<div class="btn-group btn-group-justified">
						<div class="btn-group">
							<button type="button" class="btn btn-default" data-dismiss="modal">Cancelar</button>
						</div>
						<div class="btn-group">
							<button type="submit" class="btn btn-primary" >Enviar</button>
						</div>
					</div>
				</div>
			</form>
		</div>
		
		</center>
		</div>
	</div>
  </div>
</div>


<!-- Modal Sobre -->
<div class="modal fade" id="sobre" tabindex="-1" role="dialog" aria-labelledby="sobreLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title" id="sobreLabel">Sobre</h4>
      </div>
      <div class="modal-body">
		<center>
		<div class="form-contato">
			<p>Bem, aqui é onde será deixado a descrição do projeto do Administrador para os unusario :P</p>
		</div>
		
		</center>
		</div>
	</div>
  </div>
</div>

{% endblock %}
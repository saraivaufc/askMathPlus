{% extends 'basico.php' %}

{% block menu %}
<div class="barra-menu">

<nav class="navbar bg-primary">
  <div class="container-fluid">
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav navbar-left">
        
        <li><a class="nav-item" href="/principal/">Principal</a></li>
        {% block botoes_adicionais_esq %}
        <li><a class="nav-item"  onclick="window.open('/forum')"  href="#">Fórum</a></li>
		<li><a class="nav-item"  href="/principal/estatisticas">Estatisticas</a></li>
        {% endblock %}
       
      </ul>

      <ul class="nav navbar-nav navbar-right">

			{% block voltar_all %}
        	<li  id="voltar"><a  class="nav-item" onclick="document.location = {% block voltar %}/principal/{% endblock %}">Voltar</a></li>
        	{% endblock %}

			<li><a class="nav-item" data-toggle="modal" data-target="#contato" href="#">Contato</a></li>
			<li><a class="nav-item" data-toggle="modal" data-target="#sobre" href="#">Sobre</a></li>

			{% block sair_all %}
        	<li><a class="nav-item" href="/logout/">Sair</a></li>
        	{% endblock %}
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>

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


</div>
{% endblock %}
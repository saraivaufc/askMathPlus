{% extends 'basico.php' %}

{% block menu %}
<div id="barra-menu">
	<div class="nav navbar bg-primary">
		<div class="container-fluid">
			<div class="row">
				<div class="col-xs-6 col-sm-5 col-md-3">
					<div class="navbar-header">
						<a class="navbar-brand" href="/principal/">
							<div id="title-system">
								AskMath <span class="glyphicon glyphicon-home"></span>
							</div>
						</a>
					</div>
					<ul class="nav navbar-nav">
						{% block botoes_adicionais_esq %}
							<li>
								<a id="forum" data-container="body" data-toggle="popover" data-placement="top" data-content="Use esse forum para quando tiver alguma duvida e nescessitar de ajuda de outros usuários ou bolsistas..."  onclick="window.open('/forum')">
									Forum <span class="glyphicon glyphicon-globe"></span>
								</a>
							</li>
						{% endblock %}
					</ul>
				</div>

				<div class="col-xs-6  col-sm-7 col-md-4 col-md-offset-5">
					<ul class="nav navbar-nav navbar-right">
						<li>
							<a href="/principal/">
								<span class="glyphicon glyphicon-user"></span> {{ usuario.username }}
							</a>
						</li>
						{% block botoes-menu-dir %}
						<li>
							<a data-toggle="modal" data-target="#contato">
								Contato <span class="glyphicon glyphicon-envelope"></span>
							</a>
						</li>
						 <li>
							<a data-toggle="modal" data-target="#sobre">
								Sobre <span class="glyphicon glyphicon-exclamation-sign"></span>
							</a>
						 </li>
						 {% endblock %}
						 
						{% block sair_all %}
							<li>
								<a  href="/logout/">
									Sair <span class="glyphicon glyphicon-log-out"></span>
								</a>
							</li>
						{% endblock %}
					</ul>
				</div>
			</div>
		</div><!--/.container-fluid -->
	</div><!--/.nav navbar -->    
</div><!-- /.barra-menu -->


<div class="font-dconteudo">
 	{% include 'usuario/modals/sobre.php' %}
 	{% include 'usuario/modals/contato.php' %}
</div>


{% endblock %}

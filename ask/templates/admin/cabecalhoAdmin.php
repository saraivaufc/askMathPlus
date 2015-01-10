{% extends 'basico.php' %}

{% block user-scripts %}
	<script type="text/javascript" src="/static/javascript/scripts_admin.js" ></script>
	<script type="text/javascript" src="/static/javascript/metro_admin.js" ></script>
{% endblock %}

{% block menu %}
<div id="barra-menu">
	<div class="nav navbar bg-primary">
		<div class="container-fluid">
			<div class="row">
				<div class="col-xs-6 col-sm-9 col-md-6">
					<div class="navbar-header">
						<a class="navbar-brand" href="/principal_admin/">
							<div id="title-system">
								AskMath <span class="glyphicon glyphicon-home"></span>
							</div>
						</a>
					</div>
						<ul class="nav navbar-nav">
							{% block botoes_adicionais_esq %}
								<li>
									<a id="forum" data-container="body" data-toggle="popover" data-placement="top" data-content="Use esse forum para responder as dúvidas dos usuários."  onclick="window.open('/forum')">
										Forum <span class="glyphicon glyphicon-globe"></span>
									</a>
								</li>
								<li>
									<a id="gerenciador"  data-container="body" data-toggle="popover" data-placement="top" data-content="Use ess gerenciador para adicionar, remover, buscar e editar os modelos."  onclick="window.open('/admin/')">
										Gerenciador <span class="glyphicon glyphicon-wrench"></span>
									</a>
								</li>
								<li>
									<a id="editor-latex" data-container="body" data-toggle="popover" data-placement="top" data-content="Esse editor lhe ajudará quando nescessitar adicionar Latex nos modelos."  onclick="window.open('http://latex.codecogs.com/')">
										Editor Latex <span class="glyphicon glyphicon-edit"></span>
									</a>
								</li>
							{% endblock %}
						</ul>
				</div>
				<div class="col-xs-6 col-sm-3 col-md-6">
						<ul class="nav navbar-nav navbar-right">
							<li>
								<a href="/principal_admin/">
									<span class="glyphicon glyphicon-user"></span> {{ usuario.username }}
								</a>
							</li>
							<li class="hidden-sm">
								<a data-toggle="modal" data-target="#contato">
									Contato <span class="glyphicon glyphicon-envelope"></span>
								</a>
							</li>
							 <li class="hidden-sm">
								<a data-toggle="modal" data-target="#sobre">
									Sobre <span class="glyphicon glyphicon-exclamation-sign"></span>
								</a>
							 </li>
							 
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

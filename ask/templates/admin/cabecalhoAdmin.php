{% extends 'basico.php' %}

{% block user-scripts %}
	<script type="text/javascript" src="/static/javascript/scripts_admin.js" ></script>
	<script type="text/javascript" src="/static/javascript/metro_admin.js" ></script>
{% endblock %}

{% block menu %}
	<!-- Static navbar -->
	<div class="navbar navbar-default" role="navigation">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand" href="/principal_admin/">
					AskMath <span class="glyphicon glyphicon-home"></span>
				</a>
			</div>

			<div class="navbar-collapse collapse">
				<ul class="nav navbar-nav">
					<li>
						<a href="/forum/">
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
				</ul>

				<ul class="nav navbar-nav navbar-right">
					<li>
						<a href="/principal/">
							<span class="glyphicon glyphicon-user"></span> {{ usuario.username }}
						</a>
					</li>
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
					<li>
						<a href="/logout/">
							Sair <span class="glyphicon glyphicon-log-out"></span>
						</a>
					</li>
				</ul>
			</div><!--/.nav-collapse -->
		</div><!--/.container-fluid -->
	</div><!--/ .navbar -->
	<div class="font-dconteudo">
		{% include 'usuario/modals/sobre.php' %}
		{% include 'usuario/modals/contato.php' %}
	</div>
{% endblock %}

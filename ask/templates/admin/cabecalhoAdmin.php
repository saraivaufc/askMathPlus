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
				<button type="button" class="navbar-toggle" id="navOpcoes" data-toggle="collapse" data-target=".navbar-collapse">
					<span class="glyphicon glyphicon-th-large"></span>
				</button>
				<a class="navbar-brand" href="/principal_admin/">
					AskMath <span class="glyphicon glyphicon-home"></span>
				</a>
			</div>

			<div id="obcoesMenu" class="navbar-collapse collapse">
				<ul class="nav navbar-nav">
					<li>
						<a id="forum" onClick="window.open('/forum/')" >
							Forum <span class="glyphicon glyphicon-globe"></span>
						</a>
					</li>
					<li>
						<a id="gerenciador" onclick="window.open('/admin/')">
							Gerenciador <span class="glyphicon glyphicon-wrench"></span>
						</a>
					</li>
					<li>
						<a id="editor-latex" onclick="window.open('http://latex.codecogs.com/')">
							Editor Latex <span class="glyphicon glyphicon-edit"></span>
						</a>
					</li>
				</ul>

				<ul class="nav navbar-nav navbar-right">
					<li>
						<a href="/principal_admin/">
							<span class="glyphicon glyphicon-user"></span> {{ usuario.username }}
						</a>
					</li>
					<li>
						<a data-toggle="modal" data-target="#contato">
							Contato <span class="glyphicon glyphicon-envelope "></span>
						</a>
					</li>
					<li>
						<a data-toggle="modal" data-target="#sobre">
							Sobre <span class="glyphicon glyphicon-exclamation-sign "></span>
						</a>
					</li>
					<li>
						<a href="/logout/">
							Sair <span class="glyphicon glyphicon-log-out "></span>
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

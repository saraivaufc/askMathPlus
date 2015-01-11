{% extends 'basico.php' %}

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
				<a class="navbar-brand" href="/principal/">
					AskMath <span class="glyphicon glyphicon-home"></span>
				</a>
			</div>

			<div class="navbar-collapse collapse">
				<ul class="nav navbar-nav">
					<li><a href="/forum/">
						Forum <span class="glyphicon glyphicon-globe"></span>
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

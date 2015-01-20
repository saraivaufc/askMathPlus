{% extends 'basico.php' %}


{% block menu %}
<div id="navbar" class="navbar-wrapper">
	<!-- Static navbar -->
	<div class="navbar navbar-custom" role="navigation">
		<div class="container-fluid">
			<div class="navbar-header">
				<button type="button" id="navOpcoes" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand">
					AskMath
				</a>
			</div>

			<div id="obcoesMenu" class="navbar-collapse collapse">
				<ul class="nav navbar-nav">
					<li>
						<a   href="{% block home %}{% endblock %}">
							Inicio  <span class="glyphicon glyphicon-home "></span>
						</a>
					</li>
				{% block nav-esq %}
				{% endblock %}
				</ul>

				<ul class="nav navbar-nav navbar-right">
				{% block nav-dir %}
					{% endblock %}
				</ul>
			</div><!--/.nav-collapse -->
		</div><!--/.container-fluid -->
	</div><!--/ .navbar -->
</div>

<div class="font-dconteudo">
		{% include 'usuario/modals/sobre.php' %}
		{% include 'usuario/modals/contato.php' %}
</div>

{% endblock %}
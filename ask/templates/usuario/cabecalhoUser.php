{% extends 'header.php' %}

{% block home %}/principal/{% endblock %}

{% block nav-esq %}
	<li>
		<a href="/forum/" >
			Forum <span class="glyphicon glyphicon-globe"></span>
		</a>
	</li>
	<li id="menu_disciplina">
		<a data-toggle="modal" data-rel="dialog"  data-target="#disciplinas">
			Disciplinas <span class="glyphicon glyphicon-th-list"></span>
		</a>
	</li>
{% endblock %}

{% block nav-dir %}
	<li>
		<a href="/principal/">
			<span class="glyphicon glyphicon-user"></span> {{request.user.username }}
		</a>
	</li>
	<li>
		<a data-toggle="modal" data-rel="dialog"  data-target="#contato">
			Contato <span class="glyphicon glyphicon-envelope"></span>
		</a>
	</li>
	<li>
		<a href="/logout/">
			Sair <span class="glyphicon glyphicon-log-out"></span>
		</a>
	</li>

{% include 'usuario/modals/disciplinas.php' %}
{% endblock %}

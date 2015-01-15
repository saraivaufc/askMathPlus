{% extends 'header.php' %}

{% block home %}/principal/{% endblock %}

{% block nav-esq %}
	<li>
		<a onClick="window.open('/forum/')" >
			Forum <span class="glyphicon glyphicon-globe"></span>
		</a>
	</li>
{% endblock %}

{% block nav-dir %}
	<li>
		<a href="/principal/">
			<span class="glyphicon glyphicon-user"></span>
			{% if  usuario.first_name == ""  %}
				{{ usuario.username }}
			{% else %}
				{{ usuario.first_name }}
			{% endif %}
		</a>
	</li>
	<li>
		<a data-toggle="modal" data-rel="dialog"  data-target="#contato">
			Contato <span class="glyphicon glyphicon-envelope"></span>
		</a>
	</li>
	<li>
		<a  data-toggle="modal" data-rel="dialog" data-target="#sobre">
			Sobre <span class="glyphicon glyphicon-exclamation-sign"></span>
		</a>
	</li>
	<li>
		<a href="/logout/">
			Sair <span class="glyphicon glyphicon-log-out"></span>
		</a>
	</li>
{% endblock %}


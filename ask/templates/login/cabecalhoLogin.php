{% extends 'header.php' %}

{% block home %}/principal/{% endblock %}

{% block nav-esq %}
	<li>
		<a href="/forum/" >
			Forum <span class="glyphicon glyphicon-globe"></span>
		</a>
	</li>
{% endblock %}

{% block nav-dir %}
	<li>
		<a data-toggle="modal" data-rel="dialog"  data-target="#contato">
			Contato <span class="glyphicon glyphicon-envelope"></span>
		</a>
	</li>
{% endblock %}


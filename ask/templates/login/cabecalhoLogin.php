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
		<a data-toggle="modal" data-rel="dialog"  data-target="#contato">
			Contato <span class="glyphicon glyphicon-envelope"></span>
		</a>
	</li>
	<li>
		<a  data-toggle="modal" data-rel="dialog" data-target="#sobre">
			Sobre <span class="glyphicon glyphicon-exclamation-sign"></span>
		</a>
	</li>
{% endblock %}

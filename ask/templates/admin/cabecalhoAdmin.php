{% extends 'header.php' %}

{% block home %}/principal_admin/{% endblock %}


{% block user-scripts %}
	<script type="text/javascript" src="/static/javascript/scripts_admin.js" ></script>
	<script type="text/javascript" src="/static/javascript/metro_admin.js" ></script>
{% endblock %}


{% block nav-esq %}
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
{% endblock %}

{% block nav-dir %}
	<li>
		<a href="/principal_admin/">
			<span class="glyphicon glyphicon-user"></span>
			{% if  usuario.first_name == ""  %}
				{{ usuario.username }}
			{% else %}
				{{ usuario.first_name }}
			{% endif %}
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
{% endblock %}
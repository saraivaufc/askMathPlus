{% extends 'header.php' %}

{% block home %}/principal_admin/{% endblock %}


{% block user-scripts %}
	<script type="text/javascript" src="/static/javascript/scripts_admin.js" ></script>
	<script type="text/javascript" src="/static/javascript/metro_admin.js" ></script>
{% endblock %}


{% block nav-esq %}
	<li>
		<a href="/forum/" >
			Forum <span class="glyphicon glyphicon-globe"></span>
		</a>
	</li>
	{% block gerenciador %}
	<li>
		
		<a id="gerenciador"  href="/gerenciador/" >
			Gerenciador <span class="glyphicon glyphicon-wrench"></span>
		</a>
	</li>
	{% endblock %}
	<li>
		<a id="editor-latex" onclick="window.open('http://latex.codecogs.com/eqneditor/editor.php')">
			Editor Latex <span class="glyphicon glyphicon-edit"></span>
		</a>
	</li>
{% endblock %}

{% block nav-dir %}
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
{% endblock %}
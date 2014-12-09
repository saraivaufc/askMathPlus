{% load staticfiles %}

<html>
<head>
	<meta charset="UTF-8"/>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	
	<link rel="stylesheet" type="text/css" href="/static/css/estilo.css"/>
	<link rel="stylesheet" type="text/css" media="only screen and (max-width:300px)" href="/static/css/estilo_moveis300.css"/>
	<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="/static/css/estilo.css"/>
	<link rel="stylesheet" type="text/css" media="only screen and (max-width:300px)" href="/static/css/estilo_moveis300.css"/>
	<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.css">

{% block head %}
    
    <title>
        {% block titulo %}
        {% endblock %}
    </title>
    <style type="text/css">
        {% block estilo %}
        {% endblock %}
    </style>
    <script type="text/javascript">
        {% block funcoes %}
        {% endblock %}
    </script>
    
{% endblock %}
</head>

<body>
{% block body %}

	{% block cabecalho_all %}
	<div class="cabecalho">
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-12 col-xs-12">
				{% block cabecalho %}
				{% endblock %}
				</div>
			</div>
		</div>
	</div>
	{% endblock %}

	{% block menu_all %}
	<div class="menu">
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-12 col-xs-12">
				{% block menu %}
				{% endblock %}
				</div>
			</div>
		</div>
	</div>
	{% endblock %}

	{% block conteudo_all %}
	<div class="conteudo">
		<div class="container-fluid">
			<div class="row">

			{% block conteudo %}
				<div class="col-md-5 col-xs-12">
					{% block conteudo-left %}
					{% endblock %}
				</div>
				<div class="col-md-7 col-xs-12">
					{% block conteudo-right %}
					{% endblock %}
				</div>
			{% endblock %}
			</div>
		</div>
	</div>
	{% endblock %}
	
	{% block rodape_all %}
	<div  class="rodape">
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-12 col-xs-12">
				{% block rodape %}
				
				{% endblock %}
				</div>
			</div>
		</div>
	</div>
	{% endblock %}

{% endblock %}
</body>
	<script type="text/javascript" src="/static/javascript/jquery-2.1.1.min.js"></script>
	<script type="text/javascript" src="/static/javascript/scripts.js" ></script>
	<script type="text/javascript" src="/static/javascript/jquery-2.1.1.min.js" ></script>
	<script type="text/javascript" src="/static/javascript/editor.js"></script>
	<script type="text/javascript" src="/static/bootstrap/js/bootstrap.js"></script>
</html>

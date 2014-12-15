{% load staticfiles %}


<html lang="pt">
<head>
	<meta charset="UTF-8"/>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	
	<link rel="stylesheet" type="text/css" href="/static/css/estilo.css"/>
	<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="/static/css/jquery.jscrollpane.css">

{% block head %}
    
    <title>
        {% block titulo %}
        {% endblock %}
    </title>
    <style type="text/css">
        {% block estilo %}
        {% endblock %}
    </style>
    
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

	<div class="nav">
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
	</div>

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
					<center><div id="creditos">AskMath | Copyright © 2014-2015 - PET Conexao de Saberes - UFC - (88) 9316-4340 - saraiva@alu.ufc.br</div></center>
				{% endblock %}
				</div>
			</div>
		</div>
	</div>
	{% endblock %}

{% endblock %}
</body>
	<script type="text/javascript" src="/static/javascript/jquery-2.1.1.min.js"></script>
	<script type="text/javascript" src="/static/javascript/latexit.js"></script>
	<script type="text/javascript" src="/static/javascript/scripts.js" ></script>
	<script type="text/javascript" src="/static/javascript/editor.js"></script>
	<script type="text/javascript" src="/static/bootstrap/js/bootstrap.min.js"></script>
	<script type="text/javascript" src="/static/javascript/jquery.jscrollpane.min.js"></script>
	<script type="text/javascript" src="/static/javascript/jquery.mousewheel.js"></script>

	<script type="text/javascript">
        {% block funcoes %}
        {% endblock %}
    </script>
</html>

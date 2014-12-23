{% load staticfiles %}

<html lang="pt">
<head>
	<meta charset="UTF-8"/>
	<link xmlns="http://www.w3.org/1999/xhtml" rel="icon" type="image/png" id="favicon" href="/static/imagens/icon.png" />
	<link rel="stylesheet" type="text/css" href="/static/css/site.css" />
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
    <!--[if lt IE 9]>
		<script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->
	<script type="text/javascript" src="/static/javascript/jquery-2.1.1.min.js"></script>
	<script type="text/javascript" src="/static/javascript/latexit.js"></script>
	<script type="text/javascript" src="/static/javascript/scripts.js" ></script>
	<script type="text/javascript" src="/static/javascript/metro.js" ></script>
	<script type="text/javascript" src="/static/javascript/editor.js"></script>
	<script type="text/javascript" src="/static/bootstrap/js/bootstrap.min.js"></script>
	<script type="text/javascript" src="/static/javascript/jquery.jscrollpane.min.js"></script>
	<script type="text/javascript" src="/static/javascript/jquery.mousewheel.js"></script>

	<script type="text/javascript">
        {% block funcoes %}
        {% endblock %}
    </script>
    
{% endblock %}
</head>

<body>
{% block body %}

	<header>
	{% block cabecalho_all %}
	<div id="cabecalho">
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
	<nav id="menu">
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-12 col-xs-12">
				{% block menu %}
				{% endblock %}
				</div>
			</div>
		</div>
	</nav>
	{% endblock %}

	</header>

	{% block conteudo_all %}
	<section id="conteudo">
		<div class="container-fluid">
			<div class="row">

			{% block conteudo %}
				
				<div class="col">
					<div class="col-md-5 col-xs-12">
						<div id="conteudo-left">
							{% block conteudo-left %}
							{% endblock %}
						</div>
					</div>
				</div>

				<div class="col">
					<div class="col-md-7 col-xs-12">
						<div id="conteudo-right">
							{% block conteudo-right %}
							{% endblock %}
						</div>
					</div>
				</div>
			{% endblock %}
			</div>
		</div>
	</section>
	{% endblock %}
	
	{% block rodape_all %}
	<footer id="rodape">
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-12 col-xs-12">
				{% block rodape %}
					<center><div id="creditos">AskMath | Copyright &copy; 2014-2015 - Universidade Federal do Ceara - UFC - (88) 9316-4340 - saraiva@alu.ufc.br</div></center>
				{% endblock %}
				</div>
			</div>
		</div>
	</footer>
	{% endblock %}

{% endblock %}
</body>
</html>

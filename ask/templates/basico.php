{% load staticfiles %}
{% load webdesign %}

</html>

<html lang="pt">
<head>
	<meta charset="UTF-8"/>

	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="AskMath, simples, intuitivo e poderoso sistema de perguntas e respostas criado para a Universidade Federal do Ceará.">
	<meta name="keywords" content="Universidade, Sistema, Educação, Estudantes, Perguntas e Respostas">
	<meta name="author" content="Ciano Saraiva">

	<!-- Favicons -->
	<link rel="icon" type="image/png" id="favicon" href="/static/imagens/icon.png" />

	<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap-theme.min.css">
	<link rel="stylesheet" type="text/css" href="/static/css/jquery.jscrollpane.css">

	<link rel="stylesheet"  href="/static/css/normal.css" />
	<link rel="stylesheet" media="(min-width: 1600px)" href="/static/css/grande.css" />
	<link rel="stylesheet" media="(max-width: 979px)" href="/static/css/pequeno.css" />

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
		<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
		<script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
	<![endif]-->

    
	<script type="text/javascript" src="/static/javascript/jquery-2.1.3.min.js"></script>
	<script type="text/javascript" src="/static/javascript/latexit.js"></script>
	{% block user-scripts %}
	<script type="text/javascript" src="/static/javascript/scripts.js" ></script>
	<script type="text/javascript" src="/static/javascript/metro.js" ></script>
	{% endblock %}
	<script type="text/javascript" src="/static/javascript/editor.js"></script>
	<script type="text/javascript" src="/static/javascript/jquery.jscrollpane.min.js"></script>
	<script type="text/javascript" src="/static/javascript/jquery.mousewheel.js"></script>

	<script type="text/javascript" src="/static/bootstrap/js/bootstrap.min.js"></script>
	<script type="text/javascript" src="/static/bootstrap/js/bootbox.min.js"></script>


	<script type="text/javascript">
        {% block funcoes %}
        {% endblock %}
    </script>
    
{% endblock %}
</head>

<body>
<div id="container-site">
{% block body %}
<div class="row">
<div class="col-xs-12 col-sm-12 col-md-12">
	<header>
		<div id="container-fluid">
			<div class="row">
				<div class="col-md-12">
					{% block cabecalho_all %}
					<div id="cabecalho">
						<div class="row">
							<div class="col-md-12">
							{% block cabecalho %}
								<div id="logo">

								</div>
							{% endblock %}
							</div>
						</div>
					</div>
					{% endblock %}

					{% block menu_all %}
					<div id="menu">
						<div class="row">
							<div class="col-xs-12 col-sm-12 col-md-12">
							{% block menu %}
							{% endblock %}
							</div>
						</div>
					</div>
					{% endblock %}
				</div>
			</div>
		</div>
	</header>

	{% block conteudo_all %}
	<section id="conteudo">
		<div id="container-fluid">
			<div class="row">
				{% block conteudo %}
						<div class="col-xs-5 col-sm-5 col-md-5">
							<div id="conteudo-left">
								{% block conteudo-left %}
								{% endblock %}
							</div>
						</div>

						<div class="col-xs-7 col-sm-7  col-md-7">
							<div id="conteudo-right">
								{% block conteudo-right %}
								{% endblock %}
							</div>
						</div>
				{% endblock %}
			</div>
		</div>
	</section>
	{% endblock %}
	
	{% block rodape_all %}
	<footer id="rodape">
		<div id="container-fluid">
			<div class="row">
				<div class="col-xs-12 col-sm-12 col-md-12">
					{% block rodape %}
						<center id="creditos">AskMath | Copyright &copy; 2015 - Programa De Educação Tutorial - Tecnologia Da Informação - PETTI</center>
					{% endblock %}
				</div>
			</div>
		</div>
	</footer>
	{% endblock %}
</div>
</div>
{% endblock %}
</div>
</body>
</html>

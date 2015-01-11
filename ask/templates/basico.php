{% load staticfiles %}
{% load webdesign %}


</html>

<html lang="pt">
	<head>
		{% block head %}
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

			<link rel="stylesheet" href="/static/css/base.css" />
			<link rel="stylesheet" media="(min-width: 1200px)" href="/static/css/large.css" />
			<link rel="stylesheet" media="(min-width: 768px) and (max-width: 979px)" href="/static/css/tablet.css" />
			<link rel="stylesheet" media="(max-width: 767px)" href="/static/css/tablet.css" />
			<link rel="stylesheet" media="(max-width: 480px)" href="/static/css/phone.css" />
			
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
		<div class="container-fluid">
		{% block body %}

		<header>
			{% block cabecalho_all %}
				<div id="cabecalho">
					{% block cabecalho %}
						<img id="logo" src="/static/imagens/background.jpg">
						</img>
					{% endblock %}
				</div>
			{% endblock %}
			
			{% block menu_all %}
				<div id="menu">
					{% block menu %}
					{% endblock %}
				</div>
			{% endblock %}
		</header>

		<section>
			{% block conteudo_all %}
				<div id="conteudo">
					<div class="row">
					<div class="col-md-12 col-xs-12">
					{% block conteudo %}
						<div class="row">
							<div class="col-md-5">
								<div id="conteudo-left">
									{% block conteudo-left %}
									{% endblock %}
								</div>
							</div>
							<div class="col-md-7">
								<div id="conteudo-right">
									{% block conteudo-right %}
									{% endblock %}
								</div>
							</div>
						</div>
					{% endblock %}
					</div>
					</div>
				</div>
			{% endblock %}
		</section>

		<footer>
			{% block rodape_all %}
				<div id="rodape">
					{% block rodape %}
						<center id="creditos">AskMath | Copyright &copy; 2015 - Programa De Educação Tutorial - Tecnologia Da Informação - PETTI</center>
					{% endblock %}
				</div>
			{% endblock %}
		</footer>
			
		{% endblock %}
		</div>
	</body>
</html>


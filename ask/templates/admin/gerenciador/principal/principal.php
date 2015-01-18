{% extends 'admin/cabecalhoAdmin.php' %}

{% block gerenciador %}
<li class="active">
	
	<a id="gerenciador"  href="/gerenciador/" >
		Gerenciador <span class="glyphicon glyphicon-wrench"></span>
	</a>
</li>
{% endblock %}

{% block titulo %}{{conteudo.tema}}{% endblock %}

{% block estilo %}
	#conteudo{
		background-color: #337AB7;
	}
{% endblock %}


{% block conteudo-left-all %}
	<div class="col-sm-4 col-md-4 col-lg-4">
		<div class="row">
			<div id="conteudo-left">
				{% block conteudo-left %}
				<ul class="list-group text-center"  style="vertical-align: middle;">
					<br>
					<div class="container-fluid">
						<div class="row">
							 <div class="list-group-item active">Escolha uma Opcao</div>
						</div>
						<div class="row">
							 <div class="list-group-item">
								 <div class="container-fluid">
								 	<div class="col-xs-6  col-md-8 text-center">
								 		Turma	
								 	</div>
								 	<div class="col-xs-6 col-md-4 text-right" value="1">
								 		<span class="glyphicon glyphicon-plus pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-remove pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-edit pointer"></span>
								 	</div>
								 </div>
							 </div>
						</div>
						<div class="row">
							 <div class="list-group-item">
								 <div class="container-fluid">
								 	<div class="col-xs-6 col-md-8 text-center">
								 		Licao
								 	</div>
								 	<div class="col-xs-6 col-md-4 text-right" value="2">
								 		<span class="glyphicon glyphicon-plus pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-remove pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-edit pointer"></span>
								 	</div>
								 </div>
							 </div>
						</div>
						<div class="row">
							 <div class="list-group-item">
								 <div class="container-fluid">
								 	<div class="col-xs-6 col-md-8 text-center">
								 		Pergunta	
								 	</div>
								 	<div class="col-xs-6 col-md-4 text-right" value="3">
								 		<span class="glyphicon glyphicon-plus pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-remove pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-edit pointer"></span>
								 	</div>
								 </div>
							 </div>
						</div>
						<div class="row">
							 <div class="list-group-item">
								 <div class="container-fluid">
								 	<div class="col-xs-6 col-md-8 text-center">
								 		Ajuda
								 	</div>
								 	<div class="col-xs-6 col-md-4 text-right value=" value="4">
								 		<span class="glyphicon glyphicon-plus pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-remove pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-edit pointer"></span>
								 	</div>
								 </div>
							 </div>
						</div>
						<div class="row">
							 <div class="list-group-item">
								 <div class="container-fluid">
								 	<div class="col-xs-6 col-md-8 text-center">
								 		Item	
								 	</div>
								 	<div class="col-xs-6 col-md-4 text-right " value="5">
								 		<span class="glyphicon glyphicon-plus pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-remove pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-edit pointer"></span>
								 	</div>
								 </div>
							 </div>
						</div>
						<div class="row">
							 <div class="list-group-item">
								 <div class="container-fluid">
								 	<div class="col-xs-6 col-md-8 text-center">
								 		Deficiencia	
								 	</div>
								 	<div class="col-xs-6 col-md-4 text-right" value="6" >
								 		<span class="glyphicon glyphicon-plus pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-remove pointer"></span>&nbsp;
								 		<span class="glyphicon glyphicon-edit pointer"></span>
								 	</div>
								 </div>
							 </div>
						</div>
					</div>
				</ul>
				{% endblock %}
			</div>
		</div>
	</div>
{% endblock %}
{% block conteudo-right-all %}
{% block conteudo-right-visible %}
<div class="col-sm-8 col-md-8 col-lg-8 hidden-xs">
{%  endblock %}
	<div class="row">
		<div id="conteudo-right">
			{% block conteudo-right %}


			{% endblock %}
		</div>
	</div>
</div>
{% endblock %}
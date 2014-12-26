{% extends 'usuario/cabecalhoUser.php' %}

{% block estilo %}
	#conteudo-left{
		background-color: #FFFFFF;
	}
	#conteudo-right{
		background-color: #BCD;
	}
{% endblock %}


{% block conteudo%}
	<div class="col-md-3 col-xs-12">
		<div id="conteudo-left" class="center-block">
			<br>
			<div id="list-estatistica" class="list-group">
			  	<a href="#" class="list-group-item active">Escolhar Uma Opçao:</a>

			  	<a href="/principal/estatisticas/1" class="list-group-item">Numero de Respostas Certas e Erradas.</a>
			  	<a href="/principal/estatisticas/2" class="list-group-item">Quantidade de Pulos.</a>
			  	<a href="/principal/estatisticas/3" class="list-group-item">Top 5 dos Conteudos com Menos Erros Cometidos.</a>
			  	<a href="/principal/estatisticas/4" class="list-group-item">Analise Geral</a>
			</div>
		</div>
	</div>

	<div class="col-md-9 col-xs-12">
		<div id="conteudo-right">
			<div id="table-est">
				<div class="table-responsive">
				<table id="table-estatisticas"  class="table table-bordered">
					{% block table_estatistica %}
					{% endblock %}
				</table>
				</div>
			</div>
		</div>
	</div>
{% endblock %}
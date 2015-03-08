{% extends 'usuario/secundario/secundarioOpcoes.php' %}

{% block titulo-inicial  %}
	<h3>Licao Concluida Com Exito</h3>
{% endblock %}


{% block conteudo-left-visible %}
	<div class="col-sm-5 col-md-4 col-lg-5">
{% endblock %}

{% block pontuacao %}
	<div class="col-xs-6 col-sm-3 col-md-3">
		<div class="row">
			<h4>Questões : {{ conteudo.getPerguntasOrdenadas|length }}</h4>
		</div>
	</div>
	<div class="col-xs-6 col-sm-3 col-md-3">
		<div class="row">
			<h4>Pontos : {{ pontosAcumulados }}</h4>
		</div>
	</div>
	<div class="col-xs-6 col-sm-3 col-md-3">
		<div class="row">
			<h4>Saltos : {{ pulosRealizados }}</h4>
		</div>
	</div>
	<div class="col-xs-6 col-sm-3 col-md-3">
		<div class="row">
			<h4>Ajudas : {{ vezesPediuAjuda }}</h4>
		</div>
	</div>
{% endblock %}


{% block requisitos %}
{% endblock %}

{% block sugestoes %}
	<a data-toggle="modal" data-target="#sugestoes_modal" class="list-group-item active">
	    SUGESTÕES DE ESTUDOS <span class="glyphicon glyphicon-info-sign"></span>
	</a>
	{% for c in conteudo.getSugestoes %}
		<a  onclick="window.open('/principal/opcoes/{{ c.getTema }}')" class="list-group-item">
			<t>{{ c.tema|title }}</t>
		</a>
	{% empty %}
		<a class="list-group-item list-group-item-warning">Nao existe sugestoes para essa Licao</a>
	{% endfor %}
{% endblock %}

{%  block barra-inferior %}
	<div class="barra-responder tela-opcoes-1">
		<div class="btn-group btn-group-justified fixer-bottom">
			<div class="btn-group">
				<button  type="button"  onclick="window.location='/principal/'" class="btn ui-btn btn-primary">
					Voltar Inicio <span class="glyphicon glyphicon-th"></span>
				</button>
			</div>
		</div>
	</div>
{% endblock %}


{% block modals %}
	{% include 'usuario/modals/sugestoes.php' %}	
{% endblock %}

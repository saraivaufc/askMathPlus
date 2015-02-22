{% extends 'usuario/secundario/secundarioOpcoes.php' %}

{% block titulo-inicial  %}
	Seu Andamento na Liçao
{% endblock %}

{% block conteudo-left-visible %}
	<div class="col-sm-5 col-md-4 col-lg-5 hidden-xs">
{% endblock %}

{% block pontuacao %}
	<div class="col-xs-6 col-sm-3 col-md-3">
		<div class="row">
			ACERTOS : {{ questoesCorretas|default_if_none:"0" }}
		</div>
	</div>
	<div class="col-xs-6 col-sm-3 col-md-3">
		<div class="row">
			ERRORS : {{ questoesErradas|default_if_none:"0" }}
		</div>
	</div>
	<div class="col-xs-6 col-sm-3 col-md-3">
		<div class="row">
			SALTOS : {{ pulosRealizados|default_if_none:"0" }}
		</div>
	</div>
	<div class="col-xs-6 col-sm-3 col-md-3">
		<div class="row">
			AJUDAS : {{ vezesPediuAjuda|default_if_none:"0" }}
		</div>
	</div>
{% endblock %}

{% block requisitos %}
{% endblock %}

{% block sugestoes %}
	<a data-toggle="modal" data-target="#sugestoes_modal" class="list-group-item active">
	    SUGESTÕES DE ESTUDOS <span class="glyphicon glyphicon-info-sign hidden-xs"></span>
	</a>
	{% for c in conteudo.getSugestoes %}
		<a  onclick="window.open('/principal/opcoes/{{ c.getTema }}')"  class="list-group-item">{{ c.tema|title }}</a>
	{% empty %}
		<a class="list-group-item list-group-item-warning">Nao existe sugestoes para essa Licao</a>
	{% endfor %}
{% endblock %}

{%  block barra-inferior %}
	<div class="barra-responder tela-opcoes-2">
		<div class="btn-group btn-group-justified fixer-bottom">
			<div class="btn-group">
				<button  type="button"  onclick="window.location='/principal/'" class="btn ui-btn btn-primary">
					Voltar Início <span class="glyphicon glyphicon-th"></span>
				</button>
			</div>
			<div class="btn-group">
				<button  type="button"  onclick="window.location='/principal/{{ conteudo.getTema }}'" class="btn ui-btn btn-success">
					Continuar <span class="glyphicon glyphicon-arrow-right"></span>
				</button>
			</div>
		</div>
	</div>
{% endblock %}

{% block modals %}
	{% include 'usuario/modals/sugestoes.php' %}	
{% endblock %}

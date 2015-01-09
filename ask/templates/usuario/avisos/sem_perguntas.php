{% extends 'usuario/secundario/secundarioOpcoes.php' %}

{% block titulo-inicial  %}
	<h3>Licao Nao Possui Perguntas</h3>
{% endblock %}

{% block table-pontuacao-all %}

{% endblock %}

{% block sugestoes %}
	<a class="list-group-item default"></a>
	<a data-toggle="modal" data-target="#sugestoes_modal" class="list-group-item active">
	    SUGESTÕES DE ESTUDOS <span class="glyphicon glyphicon-info-sign"></span>
	</a>
	{% for c in conteudo.getSugestoes %}
		<a  onclick="window.open('/principal/opcoes/{{ c.getTema }}')" class="list-group-item">{{ c.tema }}</a>
	{% empty %}
		<a class="list-group-item list-group-item-warning">Nao existe sugestoes para essa Licao</a>
	{% endfor %}
{% endblock %}

{%  block barra-inferior %}
	<div class="barra-responder tela-opcoes-1">
		<div class="btn-group btn-group-justified fixer-bottom">
			<div class="btn-group">
				<button  type="button"  onclick="window.location='/principal/'" class="btn btn-primary">
					Voltar Início <span class="glyphicon glyphicon-th"></span>
				</button>
			</div>
		</div>
	</div>
{% endblock %}

{%  block modals %}
	{% include 'usuario/modals/requisitos.php' %}	
	{% include 'usuario/modals/sugestoes.php' %}	
{% endblock %}

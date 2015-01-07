{% extends 'usuario/secundario/secundarioOpcoes.php' %}

{% block titulo-inicial  %}
	<h3>Licao Nao Possui Perguntas</h3>
{% endblock %}

{% block table-pontuacao-all %}

{% endblock %}

{% block sugestoes %}
	<a class="list-group-item"></a>
	<a data-toggle="modal" href="#" data-target="#sugestoes_modal" class="list-group-item active">
	    SUGESTOES DE ESTUDOS(*)
	</a>
	{% for c in conteudo.getSugestoes %}
		<a  onclick="window.open('/principal/opcoes/{{ c.getTema }}')" href="#" class="list-group-item">{{ c.tema }}</a>
	{% endfor %}
{% endblock %}

{%  block barra-inferior %}
	<div class="barra-responder tela-opcoes-1">
		<div class="btn-group btn-group-justified fixer-bottom">
			<div class="btn-group">
				<button  type="button"  onclick="window.location='/principal/'" class="btn btn-primary">
					Voltar Inicio
				</button>
			</div>
		</div>
	</div>
{% endblock %}

{%  block modals %}
	{% include 'usuario/modals/requisitos.php' %}	
	{% include 'usuario/modals/sugestoes.php' %}	
{% endblock %}
{% extends 'usuario/secundario/secundarioOpcoes.php' %}

{% block titulo-inicial  %}
	Seu Andamento na Liçao
{% endblock %}


{% block table-pontuacao %}
	<tr>
		<td class="text-center">
			QUESTÕES
		</td>
		<td class="text-center">
			PONTOS
		</td>
		<td class="text-center">
			ACERTOS
		</td>
		<td class="text-center">
			ERRORS
		</td>
		<td class="text-center">
			SALTOS
		</td>
		<td class="text-center">
			PEDIU AJUDA
		</td>
	</tr>
	<tr>
		<td class="text-center">
			{{ conteudo.getQuantPerguntasTotal|default_if_none:"0" }}
		</td>
		<td class="text-center">
			{{ pontosAcumulados|default_if_none:"0" }}
		</td>
		
		<td class="text-center">
			{{ questoesCorretas|default_if_none:"0" }}
		</td>
		
		<td class="text-center">
			{{ questoesErradas|default_if_none:"0" }}
		</td>
		<td class="text-center">
			{{ pulosRealizados|default_if_none:"0" }}
		</td>
		
		<td class="text-center">
			{{ vezesPediuAjuda|default_if_none:"0" }}
		</td>
		
	</tr>
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
				<button  type="button"  onclick="window.location='/principal/'" class="btn btn-primary">
					Voltar Início <span class="glyphicon glyphicon-th hidden-xs"></span>
				</button>
			</div>
			<div class="btn-group">
				<button  type="button"  onclick="window.location='/principal/{{ conteudo.getTema }}'" class="btn btn-success">
					Continuar <span class="glyphicon glyphicon-arrow-right hidden-xs"></span>
				</button>
			</div>
		</div>
	</div>
{% endblock %}

{% block modals %}
	{% include 'usuario/modals/sugestoes.php' %}	
{% endblock %}

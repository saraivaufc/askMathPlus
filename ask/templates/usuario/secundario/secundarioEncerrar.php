{% extends 'usuario/secundario/secundarioOpcoes.php' %}

{% block titulo-inicial  %}
	Seu Andamento na Liçao
{% endblock %}


{% block table-pontuacao %}
	<tr>
		<td class="text-center">
			QUESTOES TOTAL
		</td>
		<td class="text-center">
			{{ conteudo.getQuantPerguntasTotal }}
		</td>
		<td class="text-center">
			PONTOS ACUMULADOS
		</td>
		<td class="text-center">
			{{ pontosAcumulados }}
		</td>
	</tr>
	<tr>
		<td class="text-center">
			VEZES QUE ACERTOU
		</td>
		<td class="text-center">
			{{ questoesCorretas }}
		</td>
		<td class="text-center">
			VEZES QUE ERROU
		</td>
		<td class="text-center">
			{{ questoesErradas }}
		</td>
	</tr>
	<tr>
		<td class="text-center">
			SALTOS REALIZADOS
		</td>
		<td class="text-center">
			{{ pulosRealizados }}
		</td>
		<td class="text-center">
			VEZES QUE PEDIU AJUDA
		</td>
		<td class="text-center">
			{{ vezesPediuAjuda }}
		</td>
		
	</tr>
{% endblock %}

{% block requisitos %}
{% endblock %}

{% block sugestoes %}
	<a data-toggle="modal" data-target="#sugestoes_modal" class="list-group-item active">
	    SUGESTOES DE ESTUDOS <span class="glyphicon glyphicon-info-sign"></span>
	</a>
	{% for c in conteudo.getSugestoes %}
		<a  onclick="window.open('/principal/opcoes/{{ c.getTema }}')"  class="list-group-item">{{ c.tema }}</a>
	{% endfor %}
{% endblock %}

{%  block barra-inferior %}
	<div class="barra-responder tela-opcoes-2">
		<div class="btn-group btn-group-justified fixer-bottom">
			<div class="btn-group">
				<button  type="button"  onclick="window.location='/principal/'" class="btn btn-primary">
					Voltar Inicio <span class="glyphicon glyphicon-th"></span>
				</button>
			</div>
			<div class="btn-group">
				<button  type="button"  onclick="window.location='/principal/{{ conteudo.getTema }}'" class="btn btn-success">
					Continuar <span class="glyphicon glyphicon-arrow-right"></span>
				</button>
			</div>
		</div>
	</div>
{% endblock %}

{% block modals %}
	{% include 'usuario/modals/sugestoes.php' %}	
{% endblock %}
{% extends 'usuario/secundario/secundarioOpcoes.php' %}

{% block titulo-inicial  %}
	<h3>Licao Concluida Com Exito</h3>
{% endblock %}

{% block table-pontuacao %}
	<tr>
		<td class="text-center">
			QUESTOES TOTAL = {{ conteudo.getQuantPerguntasTotal }}
		</td>
	</tr>
	<tr>
		<td class="text-center">
			PULOS REALIZADOS = {{ pulosRealizados }}
		</td>
	</tr>
	<tr>
		<td class="text-center">
			VEZES QUE PEDIU AJUDA = {{ vezesPediuAjuda }}
		</td>
	</tr>
	<tr>
		<td class="text-center">
			PONTOS ACUMULADOS = {{ pontosAcumulados }}
		</td>
	</tr>
{% endblock %}


{% block requisitos %}
{% endblock %}

{% block sugestoes %}
	<a data-toggle="modal" href="#" data-target="#sugestoes_modal" class="list-group-item active">
	    SUGESTOES DE ESTUDOS <span class="glyphicon glyphicon-info-sign"></span>
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
					Voltar Inicio <span class="glyphicon glyphicon-th"></span>
				</button>
			</div>
		</div>
	</div>
{% endblock %}


{% block modals %}
	{% include 'usuario/modals/sugestoes.php' %}	
{% endblock %}
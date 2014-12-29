{% extends 'usuario/secundario/secundarioOpcoes.php' %}

{% block titulo-inicial  %}
	<h3>Licao Nao Possui Perguntas</h3>
{% endblock %}

{% block table-pontuacao-all %}

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
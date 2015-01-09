{% extends 'usuario/secundario/secundario.php' %}

{% block funcoes %}{% endblock %}

	{%  block titulo-inicial %}
		Sobre esta Licao
	{% endblock %}
					 	
	{%  block table-pontuacao %}
	<tr>
		<td class="text-center">
			NUMERO DE QUESTÕES
		</td>
		<td class="text-center">
			SALTOS DISPONÍVEIS
		</td>
	</tr>
	<tr>
		<td class="text-center">
			{{ conteudo.getQuantPerguntasTotal }}
		</td>
		<td class="text-center">
			{{ conteudo.max_pulos }}
		</td>
	</tr>
	{% endblock %}

	{% block outros-conteudos-all %}
	<div id="requisitos">
		<div class="list-group">
			{% block outros-conteudos %}
				{% block requisitos %}
					<a data-toggle="modal" data-target="#requisitos_modal" class="list-group-item active">
					    REQUISITOS <span class="glyphicon glyphicon-info-sign"></span>
					</a>
					{% for c in conteudo.getRequisitos %}
						<a  onclick="window.open('/principal/opcoes/{{ c.getTema }}')" class="list-group-item">
							{{ c.tema }}
						</a>
					{% endfor %}
				{% endblock %}
				{% block sugestoes %}

				{% endblock %}
			{% endblock %}
		</div>
	</div>
	{% endblock %}

	{%  block barra-inferior %}
	{% if existePulos == False %}
		<div class="barra-responder tela-opcoes-2">
	{% else %}
		<div class="barra-responder tela-opcoes-3">
	{% endif %}
			<div class="btn-group btn-group-justified fixer-bottom">
				<div class="btn-group">
					<button  type="button"  onclick="window.location='/principal/'" class="btn btn-primary">
						Voltar Início <span class="glyphicon glyphicon-th"></span>
					</button>
				</div>
				<div class="btn-group">
					<button  type="button"  onclick="window.location='/principal/{{ conteudo.getTema }}'" class="btn btn-success">
						{% if respondeuPergunta %}
							Refazer Lição <span class="glyphicon glyphicon-repeat"></span>
						{% else %}
							Iniciar Lição <span class="glyphicon glyphicon-play"></span>
						{% endif %}
					</button>
				</div>
				{% if existePulos %}
					<div class="btn-group">
						<button type="button"  data-toggle="modal" href="#" data-target="#questoes_saltadas_modal" class="btn btn-primary">
							Rever Saltos <span class="glyphicon glyphicon-retweet"></span>
						</button>
					</div>
				{% endif %}
				
			</div>
	</div>
	{% endblock %}

	{% block modals %}
		{% include 'usuario/modals/questoesSaltadas.php' %}
		{% include 'usuario/modals/requisitos.php' %}
	{% endblock %}

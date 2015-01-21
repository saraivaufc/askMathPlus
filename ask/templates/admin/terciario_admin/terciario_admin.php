{% extends 'admin/secundario_admin/secundario_admin.php' %}

{% block conteudo-left-visible %}
<div class="col-sm-5 col-md-4 col-lg-5 hidden-xs">
{% endblock %}

{% block panel %}
	<div class="panel-title" id="pontuacao-pergunta">
 		<center>
 			<h3>
 			{%  block titulo-inicial %}
	    		Essa Pergunta Vale {{ pergunta.pontos }} Pontos.
	    	{% endblock %}
	    	</h3>
	    </center>
  	</div>
 	<div class="panel-footer">
		<div class="espacamento">
		  	<t><p>{{ pergunta.descricao|safe }}</p></t>
		<hr/>
		<form method="POST" id="perguntas" name="resposta">{%csrf_token %} 
			<input id="pergunta_atual" name="pergunta_atual" value="{{pergunta.id}}" type="hidden"> 
			<input id="conteudo_atual" name="conteudo_atual" value="{{conteudo.id}}" type="hidden">
			<ol>
			{% for item in pergunta.getItens %}
				<li type="A">
					<div class="font-dconteudo">
						<input name="opcao" value="{{item.id|safe}}" required="" type="radio">
						<t>{{ item.descricao | safe }}</t>
					</div>
				</li>
				<br>
			{% empty %}
				<div class="font-dconteudo">
					<t><p>Essa pergunta nao possui itens.</p></t>
				</div>
			{% endfor %}
			</ol>
		</form>
		</div>
	</div>
{% endblock %}

{% block barra-inferior %}
	{% if existeAjuda %}
		{% if existeAnterior %}
			{% if existeProximo %}
				<div class="barra-responder tela-opcoes-5">
			{% else %}
				<div class="barra-responder tela-opcoes-5">
			{% endif %}
		{% else %}
			{% if existeProximo %}
				<div class="barra-responder tela-opcoes-4">
			{% else %}
				<div class="barra-responder tela-opcoes-3">
			{% endif %}
		{% endif %}
	{% else %}
		{% if existeAnterior %}
			{% if existeProximo %}
				<div class="barra-responder tela-opcoes-4">
			{% else %}
				<div class="barra-responder tela-opcoes-3">
			{% endif %}
		{% else %}
			{% if existeProximo %}
				<div class="barra-responder tela-opcoes-3">
			{% else %}
				<div class="barra-responder tela-opcoes-2">
			{% endif %}
		{% endif %}
	{% endif %}
		<div class="btn-group btn-group-justified fixer-bottom" role="toolbar">
			{% if existeAnterior  %}
				<div class="btn-group">
				<button  type="button" onclick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaAnterior.id}}'" class="btn btn-primary">
					Anterior <span class="glyphicon glyphicon-chevron-left"></span>
				</button>
			</div>
			{% endif %}
			<div class="btn-group">
				<button  type="button"  onclick="window.location='/principal_admin/{{conteudo.getTema}}'" class="btn btn-primary">
					Voltar <span class="glyphicon glyphicon-list"></span>
				</button>
			</div>
			{% if existeAjuda %}
			<div id="ajuda" class="btn-group">	
				<button  type="button" class="btn btn-primary" data-toggle="modal" data-target="#ajuda_modal">
					Ver Ajuda <span class="glyphicon glyphicon-question-sign"></span>
				</button>
			</div>
			{% endif %}
			<div class="btn-group">
				<button  type="button"  data-toggle="modal" data-target="#detalhes_pergunta_modal" class="btn btn-primary">
					Detalhes <span class="glyphicon glyphicon-exclamation-sign"></span>
				</button>
			</div>
			{% if existeProximo %}
			<div class="btn-group">
				<button  type="button" onclick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaProximo.id}}'" class="btn btn-primary">
					Próxima <span class="glyphicon glyphicon-chevron-right"></span>
				</button>
			</div>
			{% endif %}
		</div>
	</div>
{% endblock %}

{% block modals %}
	{% include 'usuario/modals/ajuda.php' %}
	{% include 'admin/modals/detalhesPergunta.php' %}
{% endblock %}

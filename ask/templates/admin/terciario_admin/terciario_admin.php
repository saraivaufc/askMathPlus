{% extends 'admin/secundario_admin/secundario_admin.php' %}

{% block conteudo-left-visible %}
<div class="col-sm-5 col-md-4 col-lg-5 hidden-xs">
{% endblock %}

{% block panel %}
	<div class="panel-title" id="pontuacao-pergunta">
	 	<div class="text-center">
	 		<div class="row">
			{%  block pontuacao %}
				<div class="col-xs-4 col-sm-4 col-md-4">
					<div class="row">
						<h4>Pontos : {{ pergunta.pontos }}</h4>
					</div>	
				</div>
				<div class="col-xs-4 col-sm-4 col-md-4">
					<div class="row">
						<h4>Questão : {{ numeroPergunta }} / {{ perguntasTotal|default_if_none:"0" }}</h4>
					</div>	
				</div>
				<div class="col-xs-4 col-sm-4 col-md-4">
					<div class="row">
						<h4>Item Correto : {{ pergunta.getNumeroItemCorreto }} </h4>
					</div>	
				</div>
			{% endblock %}
			</div>
		</div>
  	</div>
 	<div class="panel-footer">
 		


		<div class="espacamento">
		  	<t><p class="lead">{{ pergunta.descricao|safe }}</p></t>
		<hr/>
		<form method="POST" id="perguntas" name="resposta">{%csrf_token %} 
			<input id="pergunta_atual" name="pergunta_atual" value="{{pergunta.id}}" type="hidden"> 
			<input id="conteudo_atual" name="conteudo_atual" value="{{conteudo.id}}" type="hidden">
			<ol>
			{% for chave , item in pergunta.getItens.items %}
				<li type="A">
					<div class="font-dconteudo">
						<input name="opcao" value='{{chave}}' required type="radio">
						<t class="lead">{{ item|safe }}</t>
					</div>
				</li>
				<br>
			{% empty %}
				<div class="font-dconteudo">
					<t><p class="lead">Essa pergunta nao possui itens.</p></t>
				</div>
			{% endfor %}
			</ol>
		</form>
		</div>
	</div>
{% endblock %}

{% block barra-inferior %}
	<div class="barra-responder tela-opcoes-5">
		<div class="btn-group btn-group-justified fixer-bottom" role="toolbar">
			<div class="btn-group">
				{% if existeAnterior  %}
				<button  type="button" onclick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaAnterior.id}}'" class="btn btn-primary">
				{% else %}
				<button  type="button" onclick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaAnterior.id}}'" class="btn btn-primary" disabled>
				{% endif %}	
					Anterior <span class="glyphicon glyphicon-chevron-left"></span>
				</button>
			</div>

			<div class="btn-group">
				<button  type="button"  onclick="window.location='/principal_admin/{{conteudo.getTema}}'" class="btn btn-primary">
					Voltar <span class="glyphicon glyphicon-list"></span>
				</button>
			</div>
			
			<div id="ajuda" class="btn-group">
				{% if existeAjuda  %}
				<button  type="button" class="btn btn-primary" data-toggle="modal" data-target="#ajuda_modal">
				{% else %}
				<button  type="button" class="btn btn-primary" data-toggle="modal" data-target="#ajuda_modal" disabled>
				{% endif %}
					Ver Ajuda <span class="glyphicon glyphicon-question-sign"></span>
				</button>
			</div>
			
			<div class="btn-group">
				<button  type="button"  data-toggle="modal" data-target="#detalhes_pergunta_modal" class="btn btn-primary">
					Detalhes <span class="glyphicon glyphicon-exclamation-sign"></span>
				</button>
			</div>
			
			<div class="btn-group">
				{% if existeProximo  %}
				<button  type="button" onclick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaProximo.id}}'" class="btn btn-primary">
				{% else %}
				<button  type="button" onclick="document.location = '/principal_admin/{{conteudo.getTema}}/{{perguntaProximo.id}}'" class="btn btn-primary" disabled>
				{% endif %}
					Próxima <span class="glyphicon glyphicon-chevron-right"></span>
				</button>
			</div>
		</div>
	</div>
{% endblock %}

{% block modals %}
	{% include 'usuario/modals/ajuda.php' %}
	{% include 'admin/modals/detalhesPergunta.php' %}
{% endblock %}

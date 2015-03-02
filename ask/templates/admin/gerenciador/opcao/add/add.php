{% extends my_template %}


{% block barra-superior %}
	<div class="col-xs-12 col-sm-12  col-md-12">
		<h3 class="text-center">
		{% if opcao == 1 %}
			Adicionar Nova Turma
		{%  elif  opcao == 2 %}
			Adicionar Nova Licao
		{% elif opcao == 3 %}
			Adicionar Nova Pergunta
		{% elif opcao == 4 %}
			Adicionar Novo Usuário
		{% else %}
			Sem Opcao Selecionada
		{% endif %}
		</h3>
	</div>
{% endblock %}

{% block opcoes-padrao %}
	<form  action="."  method="POST"  onsubmit="return validaAdd({{ opcao }});" >{% csrf_token %}
		<div class="table-responsive">
			<table class="table table-bordered table-condensed">
				{{ form.as_table }}		
			</table>
		</div>	
		<div class="btn-group">
			<button class="btn btn-default" onClick="window.location='/gerenciador/list/{{ opcao }}/'; return false; "  type="cancel">
				Cancelar <span class="glyphicon glyphicon-remove-circle"></span>
			</button>
			<button type="submit" class="btn btn-primary">
				Submeter <span class="glyphicon glyphicon-ok-circle hidden-xs"></span>
			</button>
		</div>
	</form>
{% endblock %}
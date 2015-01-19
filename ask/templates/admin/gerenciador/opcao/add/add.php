{% extends my_template %}

{% if opcao == 1 %}
	template_values['my_template'] = 'admin/gerenciador/opcao/turma/list.php'
{% elif  opcao == 2 %}
	template_values['my_template'] = 'admin/gerenciador/opcao/licao/list.php'
{% elif opcao == 3 %}
	template_values['my_template'] = 'admin/gerenciador/opcao/pergunta/list.php'
{% elif opcao == 4 %}
	template_values['my_template'] = 'admin/gerenciador/opcao/ajuda/list.php'
{% elif opcao == 5 %}
	template_values['my_template'] = 'admin/gerenciador/opcao/item/list.php'
{% elif opcao == 6 %}
	template_values['my_template'] = 'admin/gerenciador/opcao/deficiencia/list.php'
{% else %}

{% endif %}




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
			Adicionar Nova Ajuda
		{% elif opcao == 5 %}
			Adicionar Novo  Item
		{% elif opcao == 6 %}
			Adicionar Nova Deficiencia
		{% else %}
			Sem Opcao Selecionada
		{% endif %}
		</h3>
	</div>
{% endblock %}

{% block opcoes-padrao %}
	<form  action="."  method="POST" >{% csrf_token %}
		<div class="table-responsive">
			<table class="table table-bordered table-condensed">
				{{ form.as_table }}		
			</table>
		</div>	
		<div class="btn-group">
			<button class="btn btn-primary" onClick="window.location='/gerenciador/list/{{ opcao }}/'; return false; "  type="cancel">Cancelar</button>
			<button type="submit" class="btn btn-primary">Submeter</button>
		</div>
	</form>
{% endblock %}
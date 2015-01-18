{% extends 'admin/gerenciador/opcao/turma/list.php' %}

{% block botao-adicionar %}
{% endblock %}

{% block opcoes-padrao %}
	<form  action="."  method="POST" >{% csrf_token %}
		<div class="table-responsive">
			<table class="table table-bordered table-condensed">
				{{ form.as_table }}		
			</table>
		</div>	
		<div class="btn-group">
			<button class="btn btn-primary" onClick="window.location='/gerenciador/opcao/list/1/'" >Cancelar</button>
			<button type="submit" class="btn btn-primary">Submeter</button>
		</div>
	</form>
{% endblock %}

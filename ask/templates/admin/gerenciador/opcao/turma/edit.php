{% extends 'admin/gerenciador/opcao/turma/list.php' %}


{% block barra-superior %}
	<div class="col-xs-12 col-sm-12  col-md-12">
		<h3 class="text-center">Editar  Turma</h3>
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
			<button class="btn btn-primary" onClick="window.location='/gerenciador/list/1/'; return false; "  type="cancel">Cancelar</button>
			<button type="submit" class="btn btn-primary">Submeter</button>
		</div>
	</form>
{% endblock %}
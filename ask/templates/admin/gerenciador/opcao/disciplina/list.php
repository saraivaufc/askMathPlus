{% extends 'admin/gerenciador/opcao/opcao.php' %}

{% block classes-disciplina %}list-group-item-info{% endblock %}

{% block  descricao %}
<h3 class="text-center">
	Todas as Disciplinas
</h3>
{% endblock %}

{% block botao-adicionar %}
	<br>
	<div class="text-right">
		<button  onclick="window.location = '/gerenciador/add/1/'  " class="btn btn-success">
			Adicionar&nbsp;<span class="glyphicon glyphicon-plus"></span>
		</button>
	</div>
{% endblock %}

{% block opcoes-padrao %}
<div class="container-fluid">
	<div class="table-responsive">
		<table class="table table-bordered text-center">
			<div class="container-fluid">
				<tr>
					<div class="col-md-6">
						<td>Nome</td>
					</div>
					<div class="col-md-6">
						<td>Opcao</td>
					</div>
				</tr>
			</div>
			{%  for i in disciplinas %}
			<div class="container-fluid">
			<tr>
				<div class="col-md-6">
					<td>{{ i.nome }}</td>
				</div>
				<div class="col-md-6">
					<td>
						&nbsp;<span onClick="editDisciplina({{ i.id }})"  class="glyphicon glyphicon-edit pointer"></span>&nbsp;
						<span onClick="remDisciplina({{ i.id }})" class="glyphicon glyphicon-remove pointer"></span>&nbsp;
					</td>
				</div>
			</tr>
			</div>
			{% endfor %}
		</table>
	</div>
</div>
{% endblock %}

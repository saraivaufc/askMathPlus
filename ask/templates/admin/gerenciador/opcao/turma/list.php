{% extends 'admin/gerenciador/opcao/opcao.php' %}

{% block classes-turma %}list-group-item-info{% endblock %}

{% block  descricao %}
<h3 class="text-center">
	Todas as Turmas
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
<div class="table-responsive">
	<table class="table table-bordered text-center">
		<tr class="row">
			<div class="col-md-3">
				<td>Semestre</td>
			</div>
			<div class="col-md-3">
				<td>Disciplina</td>
			</div>
			<div class="col-md-3">
				<td>Professor</td>
			</div>
			<div class="col-md-3">
				<td>Opcao</td>
			</div>
		</tr>
		{%  for i in turmas %}
		<tr class="row">
			<div class="col-md-3">
				<td>{{ i.semestre }}</td>
			</div>
			<div class="col-md-3">
				<td>{{ i.disciplina }}</td>
			</div>
			<div class="col-md-3">
				<td>{{ i.professor }}</td>
			</div>
			<div class="col-md-3">
				<td>
					&nbsp;<span onClick="window.location = '/gerenciador/edit/1/{{ i.id }}/' " class="glyphicon glyphicon-edit pointer"></span>&nbsp;
					<span onClick="remTurma({{ i.id }})" class="glyphicon glyphicon-remove pointer"></span>&nbsp;
				</td>
			</div>
		</tr>
		{% endfor %}
	</table>
</div>

{% endblock %}

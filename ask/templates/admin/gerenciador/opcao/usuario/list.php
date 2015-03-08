{% extends 'admin/gerenciador/opcao/opcao.php' %}

{% block classes-usuario %}list-group-item-info{% endblock %}

{% block  descricao %}
<h3 class="text-center">
	Todas os Usuários
</h3>
{% endblock %}

{% block botao-adicionar %}
	<br>
	<div class="text-right">
		<button  onclick="window.location = '/gerenciador/add/4/'  " class="btn btn-success">
			Adicionar&nbsp;<span class="glyphicon glyphicon-plus"></span>
		</button>
	</div>
{% endblock %}

{% block opcoes-padrao %}
<div class="table-responsive">
	<table class="table table-bordered text-center">
		<tr>
			<div class="col-md-3">
				<td>Primeiro Nome</td>
			</div>
			<div class="col-md-3">
				<td>Último Nome</td>
			</div>
			<div class="col-md-3">
				<td>Nome de Usuário</td>
			</div>
			<div class="col-md-3">
				<td>Status de Administrador</td>
			</div>
			<div class="col-md-3">
				<td>Opção</td>
			</div>
		</tr>
		{%  for i in usuarios %}
		<tr>
			<div class="col-md-3">
				<td>{{ i.first_name }}</td>
			</div>
			<div class="col-md-3">
				<td>{{ i.last_name }}</td>
			</div>
			<div class="col-md-3">
				<td>{{ i.username }}</td>
			</div>
			<div class="col-md-3">
				<td>{{ i.is_staff }}</td>
			</div>
			<div class="col-md-3">
				<td>
					&nbsp;<span onClick="editUsuario({{ i.id }})"  class="glyphicon glyphicon-edit pointer"></span>&nbsp;
					<span onClick="remUsuario({{ i.id }})" class="glyphicon glyphicon-remove pointer"></span>&nbsp;
				</td>
			</div>
		</tr>
		{% endfor %}
	</table>
</div>

{% endblock %}

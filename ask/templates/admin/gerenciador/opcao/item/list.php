{% extends 'admin/gerenciador/opcao/opcao.php' %}

{% block classes-item %}list-group-item-info{% endblock %}

{% block  descricao %}
<h3 class="text-center">
	Todas os Itens
</h3>
{% endblock %}

{% block botao-adicionar %}
	<br>
	<div class="text-right">
		<button  onclick="window.location = '/gerenciador/add/5/'  " class="btn btn-success">
			Adicionar&nbsp;<span class="glyphicon glyphicon-plus"></span>
		</button>
	</div>
{% endblock %}

{% block opcoes-padrao %}
<div class="table-responsive">
	<table class="table table-bordered text-center">
		<tr class="row">
			<div class="col-md-4">
				<td>Conteudo</td>
			</div>
			<div class="col-md-4">
				<td>Pergunta</td>
			</div>
			<div class="col-md-4">
				<td>Descricao</td>
			</div>
			<div class="col-md-4">
				<td>Deficiencia</td>
			</div>
			<div class="col-md-4">
				<td>Opcao</td>
			</div>
		</tr>
		{%  for i in itens %}
		<tr class="row">
			<div class="col-md-4">
				<td><t>{{ i.getConteudo|safe }}<t></td>
			</div>
			<div class="col-md-4">
				<td><t>{{ i.getPergunta|safe }}<t></td>
			</div>
			<div class="col-md-4">
				<td><t>{{ i.getDescricaoMin|safe }}<t></td>
			</div>
			<div class="col-md-4">
				<td><t>{{ i.deficiencia|safe }}</t></td>
			</div>
			<div class="col-md-4">
				<td>
					&nbsp;<span  onClick="window.location = '/gerenciador/edit/5/{{ i.id }}/' " class="glyphicon glyphicon-edit pointer"></span>&nbsp;
					<span onClick="remItem({{ i.id }})" class="glyphicon glyphicon-remove pointer"></span>&nbsp;
				</td>
			</div>
		</tr>
		{% endfor %}
	</table>
</div>

{% endblock %}
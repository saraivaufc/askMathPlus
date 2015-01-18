{% extends 'admin/gerenciador/opcao/opcao.php' %}

{% block classes-item %}list-group-item-info{% endblock %}

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
					&nbsp;<span class="glyphicon glyphicon-edit pointer"></span>&nbsp;
					<span class="glyphicon glyphicon-remove pointer"></span>&nbsp;
				</td>
			</div>
		</tr>
		{% endfor %}
	</table>
</div>

{% endblock %}
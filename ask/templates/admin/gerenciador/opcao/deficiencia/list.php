{% extends 'admin/gerenciador/opcao/opcao.php' %}

{% block classes-deficiencia %}list-group-item-info{% endblock %}

{% block opcoes-padrao %}
<div class="table-responsive">
	<table class="table table-bordered text-center">
		<tr class="row">
			<div class="col-md-4">
				<td>Conteudo</td>
			</div>
			<div class="col-md-4">
				<td>Descricao</td>
			</div>
			<div class="col-md-4">
				<td>Opcao</td>
			</div>
		</tr>
		{%  for i in deficiencias%}
		<tr class="row">
			<div class="col-md-4">
				<td><t>{{ i.conteudo|safe }}<t></td>
			</div>
			<div class="col-md-4">
				<td><t>{{ i.getDescricaoMin|safe }}<t></td>
			</div>
			<div class="col-md-4">
				<td>
					&nbsp;<span onClick="window.location = '/gerenciador/edit/6/{{ i.id }}/' " class="glyphicon glyphicon-edit pointer"></span>&nbsp;
					<span onClick="remDeficiencia({{ i.id }})" class="glyphicon glyphicon-remove pointer"></span>&nbsp;
				</td>
			</div>
		</tr>
		{% endfor %}
	</table>
</div>

{% endblock %}
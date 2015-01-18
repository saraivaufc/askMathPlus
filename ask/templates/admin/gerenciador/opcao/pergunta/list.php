{% extends 'admin/gerenciador/opcao/opcao.php' %}

{% block classes-pergunta %}list-group-item-info{% endblock %}

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
		{%  for i in perguntas %}
		<tr class="row">
			<div class="col-md-4">
				<td>{{ i.conteudo_pertence }}</td>
			</div>
			<div class="col-md-4">
				<td><t>{{ i.getDescricaoMin|safe }}</t></td>
			</div>
			<div class="col-md-4">
				<td>
					&nbsp;<span  onClick="window.location = '/gerenciador/edit/3/{{ i.id }}/' " class="glyphicon glyphicon-edit pointer"></span>&nbsp;
					<span onClick="remPergunta({{ i.id }})" class="glyphicon glyphicon-remove pointer"></span>&nbsp;
				</td>
			</div>
		</tr>
		{% endfor %}
	</table>
</div>

{% endblock %}
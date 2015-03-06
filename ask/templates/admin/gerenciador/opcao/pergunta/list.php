{% extends 'admin/gerenciador/opcao/opcao.php' %}

{% block classes-pergunta %}list-group-item-info{% endblock %}

{% block  descricao %}
<h3 class="text-center">
	Todas as Perguntas
</h3>
{% endblock %}

{% block botao-adicionar %}
	<br>
	<div class="text-right">
		<button  onclick="window.location = '/gerenciador/add/3/'  " class="btn btn-success">
			Adicionar&nbsp;<span class="glyphicon glyphicon-plus"></span>
		</button>
	</div>
{% endblock %}

{% block opcoes-padrao %}
<div class="table-responsive">
	<table class="table table-bordered text-center">
		<tr class="row">
			<div class="col-md-4">
				<td>Lição</td>
			</div>
			<div class="col-md-4">
				<td>Descrição</td>
			</div>
			<div class="col-md-4">
				<td>Opção</td>
			</div>
		</tr>
		{%  for i in perguntas %}
		<tr class="row">
			<div class="col-md-4">
				<td>{{ i.conteudo_pertence }}</td>
			</div>
			<div class="col-md-4">
				<td><t>{{ i.getDescricao|safe|truncatechars_html:50 }}</t></td>
			</div>
			<div class="col-md-4">
				<td>

					&nbsp;
					<span onClick="viewPergunta({{ i.id }})" class="glyphicon glyphicon-eye-open pointer"></span>&nbsp;
					<span  onClick="editPergunta({{ i.id }})" class="glyphicon glyphicon-edit pointer"></span>&nbsp;
					<span onClick="remPergunta({{ i.id }})" class="glyphicon glyphicon-remove pointer"></span>&nbsp;
				</td>
			</div>
		</tr>
		{% endfor %}
	</table>
</div>

{% endblock %}
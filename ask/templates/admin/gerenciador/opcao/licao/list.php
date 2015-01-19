{% extends 'admin/gerenciador/opcao/opcao.php' %}

{% block classes-licao %}list-group-item-info{% endblock %}

{% block  descricao %}
<h3 class="text-center">
	Todas as Licoes
</h3>
{% endblock %}

{% block botao-adicionar %}
	<br>
	<div class="text-right">
		<button  onclick="window.location = '/gerenciador/add/2/'  " class="btn btn-success">
			Adicionar&nbsp;<span class="glyphicon glyphicon-plus"></span>
		</button>
	</div>
{% endblock %}

{% block opcoes-padrao %}
<div class="table-responsive">
	<table class="table table-bordered text-center">
		<tr class="row">
			<div class="col-md-3">
				<td>Tema</td>
			</div>
			<div class="col-md-3">
				<td>Perguntas</td>
			</div>
			<div class="col-md-3">
				<td>Maximo Pulos</td>
			</div>
			<div class="col-md-3">
				<td>Opcao</td>
			</div>
		</tr>
		{%  for i in conteudos %}
		<tr class="row">
			<div class="col-md-3">
				<td>{{ i.tema }}</td>
			</div>
			<div class="col-md-3">
				<td>{{ i.getQuantPerguntasTotal }}</td>
			</div>
			<div class="col-md-3">
				<td>{{ i.max_pulos }}</td>
			</div>
			<div class="col-md-3">
				<td>
					&nbsp;<span onClick="editLicao({{ i.id }})" class="glyphicon glyphicon-edit pointer"></span>&nbsp;
					<span onClick="remLicao({{ i.id }})" class="glyphicon glyphicon-remove pointer"></span>&nbsp;
				</td>
			</div>
		</tr>
		{% endfor %}
	</table>
</div>

{% endblock %}
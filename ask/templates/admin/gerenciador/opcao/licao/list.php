{% extends 'admin/gerenciador/opcao/opcao.php' %}

{% block classes-licao %}list-group-item-info{% endblock %}

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
					&nbsp;<span class="glyphicon glyphicon-edit pointer"></span>&nbsp;
					<span class="glyphicon glyphicon-remove pointer"></span>&nbsp;
				</td>
			</div>
		</tr>
		{% endfor %}
	</table>
</div>

{% endblock %}
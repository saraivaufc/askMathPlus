{% extends 'admin/gerenciador/opcao/turma/list.php' %}

{% block  descricao %}
{% endblock %}

{% block botao-adicionar %}
{% endblock %}

{% block opcoes-padrao %}
<div class="container-fluid">
	<div class="row">
		<center>
			<h1 class="text-center">
				{%  if ok %}
				Turma Editada com Sucesso!!!
				{% else %}
				Falha ao Editar a Turma!!!
				{% endif %}
			</h1>
			<div class="btn-group">
				<button  onclick="window.location='/gerenciador/list/1/' " class="btn btn-primary">Voltar as Turmas</button>
				{%  if ok == False %}
				<button onclick="window.location='/gerenciador/add/1/' " class="btn btn-primary">Tentar Novamente</button>
				{% endif %}	
			</div>
			
		</center>
	</div>
</div>
{% endblock %}
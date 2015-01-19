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
				Ajuda Editada com Sucesso!!!
				{% else %}
				Falha ao Editar a Ajuda!!!
				{% endif %}
			</h1>
			<div class="btn-group">
				<button  onclick="window.location='/gerenciador/list/4/' " class="btn btn-primary">Voltar as Ajudas</button>
				{%  if ok == False %}
				<button onclick="window.location='/gerenciador/edit/4/{{ id }}' " class="btn btn-primary">Tentar Novamente</button>
				{% endif %}	
			</div>
			
		</center>
	</div>
</div>
{% endblock %}
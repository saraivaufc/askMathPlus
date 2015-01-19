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
				Licao Adicionado com Sucesso!!!
				{% else %}
				Falha ao Adicionar Licao!!!
				{% endif %}
			</h1>
			<div class="btn-group">
				<button  onclick="window.location='/gerenciador/list/2/' " class="btn btn-primary">Voltar as Licoes</button>
				{%  if ok == False %}
				<button onclick="window.location='/gerenciador/add/2/' " class="btn btn-primary">Tentar Novamente</button>
				{% else %}
				<button onclick="window.location='/gerenciador/add/2/' " class="btn btn-primary">Adicionar Outra</button>
				{% endif %}	
			</div>
			
		</center>
	</div>
</div>
{% endblock %}
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
					{% if opcao == 1 %}
					 	Turma Editada Com Sucesso!!!
					 {%  elif opcao == 2 %}
					 	Licao Editada Com Sucesso!!!
					 {% elif opcao == 3 %}
					 	Pergunta Editada Com Sucesso!!!
					 {% else %}
					 	Nenhuma Opcao Selecionada!!!
					 {% endif %}
				{% else %}
					{% if opcao == 1 %}
					 	Falha ao Editar Turma!!!
					 {%  elif opcao == 2 %}
					 	Falha ao Editar Licao!!!
					 {% elif opcao == 3 %}
					 	Falha ao Editar Pergunta!!!
					 {% else %}
					 	Nenhuma Opcao Selecionada!!!
					 {% endif %}
				{% endif %}
			</h1>
			<div class="btn-group">
				{% if opcao >= 1 and opcao <= 3 %}
					<button  onclick="window.location='/gerenciador/list/{{ opcao }}/' " class="btn btn-primary">
				{%  else %}
					<button  onclick="window.location='/gerenciador/' " class="btn btn-primary">
				{% endif %}
				
				{% if opcao == 1 %}
				 	Voltar as Turmas
				 {%  elif opcao == 2 %}
				 	Voltar as Licoes
				 {% elif opcao == 3 %}
				 	Voltar as Perguntas
				 {% else %}
				 	Voltar as Opcoes
				 {% endif %}
				{%  if ok == False %}
				<button onclick="window.location='/gerenciador/edit/{{ opcao }}/{{ id }}' " class="btn btn-primary">Tentar Novamente</button>
				{% endif %}
				</div>
			</div>
			
		</center>
	</div>
</div>
{% endblock %}
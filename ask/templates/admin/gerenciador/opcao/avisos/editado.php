{% extends my_template %}

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
					 	Disciplina Editada Com Sucesso!!!
					 {%  elif opcao == 2 %}
					 	Licao Editada Com Sucesso!!!
					 {% elif opcao == 3 %}
					 	Pergunta Editada Com Sucesso!!!
					 {% elif opcao == 4 %}
					 	Usuário Editado Com Sucesso!!!
					 {% else %}
					 	Nenhuma Opcao Selecionada!!!
					 {% endif %}
				{% else %}
					{% if opcao == 1 %}
					 	Falha ao Editar Disciplina!!!
					 {%  elif opcao == 2 %}
					 	Falha ao Editar Licao!!!
					 {% elif opcao == 3 %}
					 	Falha ao Editar Pergunta!!!
					 {% elif opcao == 4 %}
					 	Falha ao Editar Usuário!!!
					 {% else %}
					 	Nenhuma Opcao Selecionada!!!
					 {% endif %}
				{% endif %}
			</h1>
			<div class="btn-group">
				{% if opcao >= 1 and opcao <= 4 %}
					<button  onclick="window.location='/gerenciador/list/{{ opcao }}/' " class="btn btn-primary">
				{%  else %}
					<button  onclick="window.location='/gerenciador/' " class="btn btn-primary">
				{% endif %}
				
				{% if opcao == 1 %}
				 	Voltar as Disciplinas
				 {%  elif opcao == 2 %}
				 	Voltar as Licoes
				 {% elif opcao == 3 %}
				 	Voltar as Perguntas
				 {% elif opcao == 4 %}
				 	Voltar os Usuário
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
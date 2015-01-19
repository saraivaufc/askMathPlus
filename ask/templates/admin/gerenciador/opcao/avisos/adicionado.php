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
					 	Turma Adicionada Com Sucesso!!!
					 {%  elif opcao == 2 %}
					 	Licao Adicionada Com Sucesso!!!
					 {% elif opcao == 3 %}
					 	Pergunta Adicionada Com Sucesso!!!
					 {% elif  opcao == 4 %}
					 	Ajuda Adicionada Com Sucesso!!!
					 {%  elif  opcao == 5 %}
					 	Item Adicionada Com Sucesso!!!
					 {% elif  opcao == 6  %}
					 	Deficiencia Adicionada Com Sucesso!!
					 {% else %}
					 	Nenhuma Opcao Selecionada!!!
					 {% endif %}

				{% else %}
					{% if opcao == 1 %}
					 	Falha ao Adicionar Turma!!!
					 {%  elif opcao == 2 %}
					 	Falha ao Adicionar Licao!!!
					 {% elif opcao == 3 %}
					 	Falha ao Adicionar Pergunta!!!
					 {% elif  opcao == 4 %}
					 	Falha ao Adicionar Ajuda!!!
					 {%  elif  opcao == 5 %}
					 	Falha ao Adicionar Item!!!
					 {% elif  opcao == 6  %}
					 	Falha ao Adicionar Deficiencia!!!
					 {% else %}
					 	Nenhuma Opcao Selecionada!!!
					 {% endif %}
				{% endif %}
			</h1>
			<div class="btn-group">
				{% if opcao == 1 %}
				 	<button  onclick="window.location='/gerenciador/list/1/' " class="btn btn-primary">Voltar as Turmas</button>
				 {%  elif opcao == 2 %}
				 	<button  onclick="window.location='/gerenciador/list/2/' " class="btn btn-primary">Voltar as Licoes</button>
				 {% elif opcao == 3 %}
				 	<button  onclick="window.location='/gerenciador/list/3/' " class="btn btn-primary">Voltar as Perguntas</button>
				 {% elif  opcao == 4 %}
				 	<button  onclick="window.location='/gerenciador/list/4/' " class="btn btn-primary">Voltar as Ajudas</button>
				 {%  elif  opcao == 5 %}
				 	<button  onclick="window.location='/gerenciador/list/5/' " class="btn btn-primary">Voltar aos Itens</button>
				 {% elif  opcao == 6  %}
				 	<button  onclick="window.location='/gerenciador/list/6/' " class="btn btn-primary">Voltar as Deficiencias</button>
				 {% else %}
				 	<button  onclick="window.location='/gerenciador/' " class="btn btn-primary">Voltar as Opcoes</button>
				 {% endif %}


				{%  if ok == False %}
				<button onclick="window.location='/gerenciador/add/{{ opcao }}/' " class="btn btn-primary">Tentar Novamente</button>
				{% else %}
				<button onclick="window.location='/gerenciador/add/{{ opcao }}/' " class="btn btn-primary">Adicionar Outra</button>
				{% endif %}	
			</div>
			
		</center>
	</div>
</div>
{% endblock %}
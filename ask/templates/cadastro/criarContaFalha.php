{% extends 'login/login.php' %}

{% block conteudo %}
	<center>
		<h1>Falha ao criar Usuario!!!</h1>
		<br>
		<h2>Erros:</h2>
		<h3>
		<ol>
		{% for i in errors %}
			<li>{{i}}</li>
		{% endfor %}
		</ol>
		</h3>
		<div>
			<div class="btn-group btn-group-justified tela-opcoes-1">
				<div class="btn-group">
					<button class="btn btn-default" onClick="document.location='/login/'">Voltar Login</button>	
				</div>
				<div class="btn-group">
					<button class="btn btn-primary" onClick="document.location='/criarConta/'">Tentar Novamente</button>
				</div>
			</div>
		</div>
	</center>
{% endblock %}

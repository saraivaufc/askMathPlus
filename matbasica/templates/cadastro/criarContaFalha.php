{% extends 'login/login.php' %}

{% block conteudo %}
	<center>
		<h1>Falha ao criar Usuario!!!</h1>
		<button class="btn botao caixa botao-1" onClick="document.location='/criarConta/'">Tentar Novamente</button>
	</center>
{% endblock %}

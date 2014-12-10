{% extends 'usuario/principal/principal.php' %}

{% block conteudo %}
	<center>
		<h1>Conteudo Concluido com Sucesso!!!</h1>
	</center>
	<br>
	<br>
	<div id="botao_concluido">
		<center>
			<button class="btn botao" onclick="window.location='/principal/'" >Voltar ao Inicio</button>
		</center>
	</div>
{% endblock %}
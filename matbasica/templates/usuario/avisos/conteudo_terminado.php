{% extends 'usuario/principal/principal.php' %}

{% block conteudo %}
	<center>
		<h1>Parabens!!!<br>Voce ja terminou "{{ conteudo.tema }}"</h1>
		<button class="btn botao" onclick="window.location='/principal/'" >Voltar ao Inicio</button>
	</center>
{% endblock %}
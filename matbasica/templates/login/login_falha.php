{% extends 'basico.php' %}

{% block titulo %}
    Falha Login
{% endblock %}

{% block body %}
		<div class="titulo-sistema">
			<div class="title-container">
				<center><h1>Falha ao Efetuar Login</h1>
			</div>
		</div>
		<center>
			<button class="botao caixa botao-1" onClick="document.location='/login/' ">Tentar Novamente</button>
		</center>
{% endblock %}

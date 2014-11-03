{% extends 'basico.php' %}

{% block titulo %}
    Falha Login
{% endblock %}

{% block cabecalhoall %}
		<div class="titulo-sistema">
			<div class="title-container">
				<center><h1>Usuário Criado Com Exito</h1>
			</div>
		</div>
{% endblock %}
{% block menuall %}
	<center>
		<button class="botao caixa botao-1" onClick="document.location='/login/' ">Fazer Login</button>
	</center>
{% endblock %}

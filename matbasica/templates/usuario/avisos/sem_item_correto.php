{% extends 'usuario/secundario/secundario.php' %}

{% block voltar %}document.location{% endblock %}

{% block conteudo-right %}
	<div class="conteudo-right bg-warning">
		<div class="font-dconteudo">
			<div class="descricao-pergunta">
				<div class="avisos-conteudo">
				<center>
					<h1>Pergunta nao possui item correto, contactar Administrador!!!</h1>
				</center>
				</div>
			</div>
		</div>
	</div>
{% endblock %}
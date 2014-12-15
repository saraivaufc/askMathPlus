{% extends 'usuario/secundario/secundario.php' %}


{%  block funcoes %}
	$(document).ready(function(){
		$(".jspPane").css("height","100%");
	});
{%  endblock %}

{% block conteudo-right %}
	<div class="conteudo-right bg-success">
		<div class="font-dconteudo">
			<div class="descricao-pergunta">
				<div class="avisos-conteudo">
				<center>
					<h1>Conteudo Concluido!!!</h1>
				</center>
				</div>
			</div>
		</div>
	</div>
{% endblock %}
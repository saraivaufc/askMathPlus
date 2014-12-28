{% extends 'usuario/secundario/secundario.php' %}


{%  block funcoes %}
	$(document).ready(function(){
		$(".jspPane").css("height","100%");
	});
{%  endblock %}

{% block conteudo-right %}
	<div class="conteudo-right bg-info">
		<div class="font-dconteudo">
			<div class="descricao-pergunta">
				<div class="avisos-conteudo">
				<center>
					<h1>Conteúdo Concluido!!!</h1>
				</center>
				</div>
			</div>
			<center>
				<div class="barra-responder tela-opcoes-1">	
					<div class="btn-group btn-group-justified fixer-bottom">
						<div class="btn-group">
							<button  type="button"  onclick="window.location='/principal/'" class="btn btn-info">
								Voltar Inicio
							</button>
						</div>
					</div>
				</div>
			</center>
		</div>
	</div>
{% endblock %}

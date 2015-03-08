{% extends 'usuario/secundario/secundario.php' %}

{% block voltar %}{% endblock %}

{%  block funcoes %}
	$(document).ready(function(){
		$(".jspPane").css("height","100%");
	});
{%  endblock %}

{% block conteudo-left-visible %}
	<div class="col-sm-5 col-md-4 col-lg-5 hidden-xs">
{% endblock %}

{% block conteudo-right %}
	<div class="conteudo-right bg-info">
		<div class="font-dconteudo">
			<div class="descricao-pergunta">
				<div class="avisos-conteudo">
				<center>
					<h1>
						Você errou porque a pergunta não possui item correto, entre em contato com o Administrador!!!
					</h1>
					<div class="barra-responder tela-opcoes-1">
						<div class="btn-group btn-group-justified fixer-bottom">
							<div class="btn-group">
								<button  type="button"  onclick="window.location=window.location" class="btn ui-btn btn-primary">
									Recarregar <span class="glyphicon glyphicon-refresh"></span>
								</button>
							</div>
						</div>
					</div>
				</center>

				</div>
			</div>
		</div>
	</div>
{% endblock %}

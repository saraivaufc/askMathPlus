{% extends 'usuario/cabecalhoUser.php' %}

{% block voltar_all %}
{% endblock %}


{% block titulo %}Principal{% endblock %}


{%  block funcoes %}
	$(document).ready(function(){
		$(".jspPane").css("height","95%");
	});
{%  endblock %}

{% block conteudo %}

<div class="col-md-12 col-xs-12">
	<div class="metro">

		<table id="container-metro">
			<tr id="linha-metro">
			<td>
			<div class="linha">
				{% for i in conteudos1 %}
					{% if i.tamanho_metro == 1 %}
						<div class="tile">
					{% endif %}
					
					{% if i.tamanho_metro == 2 %}
						<div class="tile tileLargo">
					{% endif %}
							<center class="font-metro">
								<div id="text-quadrado">
									<p id="cont">{{i.tema}}</p>
								</div>
							</center>
						</div>
				{% endfor %}
			</div>
			</td>
			</tr>

			<tr id="linha-metro">
			<td>
			<div class="linha">
				{% for i in conteudos2 %}
					{% if i.tamanho_metro == 1 %}
						<div class="tile">
					{% endif %}
					{% if i.tamanho_metro == 2 %}
						<div class="tile tileLargo">
					{% endif %}
							<center class="font-metro">
								<div id="text-quadrado">
									<p id="cont">{{i.tema}}</p>
								</div>
							</center>
						</div>
					{% endfor %}
			</div>
			</td>
			</tr>
			
			<tr id="linha-metro">
			<td>
			<div class="linha">
				{% for i in conteudos3 %}
					{% if i.tamanho_metro == 1 %}
						<div class="tile">
					{% endif %}
					
					{% if i.tamanho_metro == 2 %}
						<div class="tile tileLargo">
					{% endif %}
							<center class="font-metro">
								<div id="text-quadrado">
									<p id="cont">{{i.tema}}</p>
								</div>
							</center>
						</div>
				{% endfor %}
			</div>
			</td>
			</tr>
		</table>
	</div>
</div>

{% endblock %}

{% block voltar %}'/principal/'{% endblock %}

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
							<div class="text-center font-metro">
									{{i.tema}}
							</div>
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
									{{i.tema}}
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
									{{i.tema}}
							</center>
						</div>
				{% endfor %}
			</div>
			</td>
			</tr>
		</table>
	</div>
{% endblock %}

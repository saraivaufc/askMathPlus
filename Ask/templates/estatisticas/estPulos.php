{% extends 'estatisticas/estatisticas.php' %}


{% block voltar %}/principal/estatisticas{% endblock %}

{% block table_estatistica %}

	<tr class="bg-success">
		<td>Conteudo</td><td>Quantidade de Pulos</td>
	</tr>
	{% for l in list %}
		<tr>
		<td>{{ l.tema }}</td>
		<td>{{ l.pulos }}</td>
		</tr>
	{% endfor %}
{% endblock %}
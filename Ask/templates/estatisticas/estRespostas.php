{% extends 'estatisticas/estatisticas.php' %}


{% block table_estatistica %}

	<tr class="bg-success">
		<td>Conteudo</td><td>Total</td><td>Respondidas</td><td>Certas</td><td>Erradas</td>
	</tr>
	{% for l in list %}
		<tr>
		<td>{{ l.tema }}</td>
		<td>{{ l.total }}</td>
		<td>{{ l.respondidas }}</td>
		<td>{{ l.certas }}</td>
		<td>{{ l.erradas }}</td>
		</tr>
	{% endfor %}
{% endblock %}
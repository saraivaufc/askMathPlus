{% extends 'admin/gerenciador/principal/principal.php' %}

{% block conteudo-right-all %}
{% block conteudo-right-visible %}
<div class="col-sm-8 col-md-8 col-lg-8">
{%  endblock %}
	<div class="row">
		<div id="conteudo-right">
			{% block conteudo-right %}
			
			{% endblock %}
		</div>
	</div>
</div>
{% endblock %}
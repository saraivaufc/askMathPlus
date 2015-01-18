{% extends 'admin/gerenciador/principal/principal.php' %}

{% block conteudo-right-all %}
{% block conteudo-right-visible %}
<div class="col-sm-8 col-md-8 col-lg-8">
{%  endblock %}
	<div class="row">
		<div id="conteudo-right">
			{% block conteudo-right %}
			<div class="opcoes-padrao">
				<br>
				<div class="text-right">
					<button class="btn btn-success">
						Adicionar&nbsp;<span class="glyphicon glyphicon-plus"></span>
					</button>
				</div>
				<div class="container-fluid">
					<div class="row">	
						{% block  opcoes-padrao %}

						{% endblock %}
					</div>
				</div>
			</div>
			{% endblock %}
		</div>
	</div>
</div>
{% endblock %}
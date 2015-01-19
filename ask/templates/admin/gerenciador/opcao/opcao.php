{% extends 'admin/gerenciador/principal/principal.php' %}

{% block conteudo-right-all %}
{% block conteudo-right-visible %}
<div class="col-sm-8 col-md-8 col-lg-8">
{%  endblock %}
	<div class="row">
		<div id="conteudo-right">
			{% block conteudo-right %}
			<div class="opcoes-padrao">
				<div class="container-fluid">
					<div class="row">
						{% block barra-superior %}
							<div class="col-xs-8 col-sm-8  col-md-8">
								{% block  descricao %}

								{% endblock %}
							</div>
							<div class="col-xs-4 col-sm-4 col-md-4">
								{% block botao-adicionar %}
									
								{% endblock %}
							</div>
						{% endblock %}
					</div>
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
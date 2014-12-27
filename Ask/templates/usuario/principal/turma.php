{% extends 'usuario/cabecalhoUser.php' %}

{% block titulo %}
    Principal
{% endblock %}

{% block voltar_all %}
{% endblock %}

{% block conteudo %}

<center>
	<h1>Escolha uma Turma</h1>
</center>
	<div class="form-centro">
		<form  class="form-horizontal" role="form" action="." method="POST">{% csrf_token %}
			{% for i in turmas %}
				<div class="form-group">
					<div class="radio">
							<label>
								<input type="radio" name="opcao" id="opcao" value="{{i.id}}">
								{{i.semestre}} = {{i.nome}}
							</label>
					</div>
				</div>
			{% endfor %}

			<div class="btn-group btn-group-justified">
				<div class="btn-group">
					<button type="submit" class="btn btn-primary">Escolher</button>
				</div>
				<div class="btn-group">
					<button type="button" class="btn btn-primary" onClick="document.location='/logout/'">Sair</button>
				</div>
			</div>
		</form>
	</div>

{% endblock %}
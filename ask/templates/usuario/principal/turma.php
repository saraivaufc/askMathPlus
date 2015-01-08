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
	<center>
		<div id="escolher_turma">
		<form  class="form-horizontal" role="form" action="." method="POST">{% csrf_token %}
			<div class="table-responsive">
			<table class="table table-bordered">
			<tr class="info">
				<td></td><td>Semestre</td><td>Disciplina</td><td>Professor</td>
			</tr>

			{% for i in turmas %}
				<tr>
					<td>
						<input type="radio" name="opcao" id="opcao" value="{{i.id}}" required>
					</td>
					<td>
						{{i.semestre}}
					</td>
					<td>
						{{i.disciplina}}
					</td>
					<td>
						{{i.professor}}
					</td>
				</tr>
			{% endfor %}
			</table>
			</div>
				<div class="btn-group btn-group-justified tela-opcoes-3">
					<div class="btn-group">
						<button type="submit" class="btn btn-primary">
							Escolher <span class="glyphicon glyphicon-ok-circle"></span>
						</button>
					</div>
					<div class="btn-group">
						<button type="button" class="btn btn-primary" onClick="document.location='/logout/'">
							Sair <span class="glyphicon glyphicon-log-out"></span>
						</button>
					</div>
				</div>
		</form>
		</div>
	</center>

{% endblock %}
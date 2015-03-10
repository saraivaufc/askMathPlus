{% extends 'usuario/cabecalhoUser.php' %}

{% block titulo %}
    Disciplinas
{% endblock %}

{% block conteudo %}
<div class="container">
<center>
	<h1>Escolha uma Disciplina.</h1>
</center>
	<center>
		<div id="escolher_turma">
		<form  class="form-horizontal" role="form" action="/principal/" method="POST">{% csrf_token %}
				<div class="table-responsive">
				<table id="disciplinas" class="table table-bordered disciplinas">
					<tr class="info active text-center">
						<td colspan="2">Disciplinas</td>
					</tr>
				</table>
				</div>
				<div class="btn-group btn-group-justified tela-opcoes-3">
					<div class="btn-group">
						<button type="submit" class="btn ui-btn btn-primary">
							Escolher <span class="glyphicon glyphicon-ok-circle hidden-xs"></span>
						</button>
					</div>
					<div class="btn-group">
						<button type="button" class="btn ui-btn btn-primary" onClick="document.location='/logout/'">
							Sair <span class="glyphicon glyphicon-log-out hidden-xs"></span>
						</button>
					</div>
				</div>
			</form>
		</div>
	</center>
</div>
{% endblock %}

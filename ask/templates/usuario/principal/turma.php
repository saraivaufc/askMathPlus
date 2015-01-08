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
		<div class="form-login login">
		<form  class="form-horizontal" role="form" action="." method="POST">{% csrf_token %}
			{% for i in turmas %}
				<div class="form-group  text-left">
					<div class="radio">
							<label>
								<input type="radio" name="opcao" id="opcao" value="{{i.id}}">
								<p class="lead">{{i.semestre}} : {{i.nome}}</p>
							</label>
					</div>
				</div>
			{% endfor %}
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
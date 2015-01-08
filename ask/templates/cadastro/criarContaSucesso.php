{% extends 'login/login.php' %}

{% block conteudo %}
	<center>
		<div class="form-login center-block">
			<h1>Conta Criada com exito!!!</h1>
			<br>
			<div class="btn-group btn-group-justified tela-opcoes-3">
				<div class="btn-group">
					<button class="btn btn-default" onClick="document.location='/login/'">
						Voltar Login <span class="glyphicon glyphicon-log-in"></span>
					</button>	
				</div>
				<div class="btn-group">
					<button class="btn btn-primary" onClick="document.location='/criarConta/'">
						Criar Outra <span class="glyphicon glyphicon-plus-sign"></span>
					</button>
				</div>
			</div>
		</div>
	</center>
{% endblock %}

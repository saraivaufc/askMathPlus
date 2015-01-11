{% extends 'login/login.php' %}

{% block conteudo %}
	<div class="container">
		<center>
			<div class="form-login">
				<h1>Falha ao criar Usuario!!!</h1>
				<br>
				<h3>
				<ul class="list-group">
				<li class="list-group-item active">Erros</li>
				{% for i in errors %}
					<li class="list-group-item">{{i}}</li>
				{% endfor %}
				</ul>
				</h3>
				<div>
					<div class="btn-group btn-group-justified tela-opcoes-4">
						<div class="btn-group">
							<button class="btn btn-default" onClick="document.location='/login/'">
								Voltar Login <span class="glyphicon glyphicon-log-in"></span>
							</button>	
						</div>
						<div class="btn-group">
							<button class="btn btn-primary" onClick="document.location='/criarConta/'">
								Tentar Novamente <span class="glyphicon glyphicon-repeat"></span>
							</button>
						</div>
					</div>
				</div>
			</div>
		</center>
	</div>
{% endblock %}

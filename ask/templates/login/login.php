{% extends 'usuario/cabecalhoUser.php' %}

{% block titulo %}
    Login
{% endblock %}

{% block page_atual %}"/login/"{% endblock %}

{% block estilo %}
	.form-login label{
		font-weight: bold;
		font-size: 120%;
	}
{% endblock %}


{% block sair_all %}{% endblock %}

{% block conteudo %}
	<div class="conteudo">
		<center>
			<div class="form-login login">
				<form class="form form-horizontal" method="post" role="form" action=".">{% csrf_token %}
					<div class="col-sm-12">
						<h2>Realizar Login</h2>
					</div>
					<input name="next" value="/principal/" type="hidden">
					
					<div class="col-sm-2">

					</div>
					<div class="col-sm-8">
						<div class="form-group">
							<label>Usuário ou Email</label>
							<input id="id_username" class="form-control" maxlength="254" name="username" type="text" required autofocus autocomplete="on" placeholder="Seu nome de usuário ou email">
						</div>

						<div class="form-group">
							<label>Senha</label>
							<input id="id_password" class="form-control" name="password" type="password" required placeholder="Sua senha">
						</div>

						<div class="form-group">
							<div class="btn-group btn-group-justified">
								<div class="btn-group">
									<button type="button" class="form-control btn  btn-default"  onClick="document.location='/criarConta/'">
										Criar Conta <span class="glyphicon glyphicon-plus-sign"></span>
									</button>
								</div>
								<div class="btn-group">
									<button  type="submit" class="form-control btn btn-primary" name="post">
										Entrar <span class="glyphicon glyphicon-log-in"></span>
									</button>
								</div>
							</div>
						</div>
					</div>
					<div class="col-sm-2">

					</div>
				</form>
			</div>
		</center>
	</div>

{% endblock %}

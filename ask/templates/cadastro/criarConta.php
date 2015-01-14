{% extends 'login/login.php' %}

{% block page_atual %}"/criarConta/"{% endblock %}

{% block estilo %}
	.container{
		overflow-y:auto;
	}
{% endblock %}

{% block conteudo %}
<div class="container">
	<center>
		<form class="form-login form-horizontal" role="form" onSubmit="return validaCriarConta()"  method="post">{% csrf_token %}
			<div class="col-sm-12">
				<h2>Criar Conta</h2>
			</div>
		<div class="row">
			<fieldset class="col-sm-6 col-md-6">
				<legend class="hidden-xs">Usuário</legend>
					<div class="form-group">
						<label for="username" class=" control-label">Usuário</label>
						<div>
							<input id="username" class="form-control" name="username" required autofocus type="text" autocomplete="on" placeholder="Digite um nome de usuario">
						</div>
					</div>
					
					<div class="form-group">
						<label for="first_name" class="control-label">Primeiro Nome</label>
						<div>
							<input id="first_name" class="form-control" name="first_name" required type="text" autocomplete="on" placeholder="Digite seu primeiro nome">
						</div>
					</div>
					
					<div class="form-group">
						<label for="last_name" class="control-label">Último Nome</label>
						<div>
							<input id="last_name" class="form-control" name="last_name" required type="text" autocomplete="on" placeholder="Digite seu segundo nome">
						</div>
					</div>
			</fieldset>

			<fieldset class="col-sm-6  col-md-6">
				<legend class="hidden-xs">Conta</legend>
				<div class="form-group">
					<label for="email" class="control-label">Email</label>
					<div>
						<input id="email" class="form-control" name="email" required type="email" autocomplete="on" placeholder="Digite seu email">
					</div>
				</div>
				<div class="form-group " id="senha1">
					<label for="password" class="control-label">Senha</label>
					<div>
						<input id="password" class="form-control" name="password" required="" type="password" placeholder="Digite uma senha">
					</div>
				</div>
				<div class="form-group " id="senha2">
					<label for="password2" class="control-label">Repita a Senha</label>
					<div>
						<input id="password2" class="form-control" name="password2" required="" type="password" placeholder="Repita a senha">
					</div>
				</div>
			</fieldset>
		</div>
			<div class="form-group">
				<div class="btn-group btn-group-justified tela-opcoes-3">
					<div class="btn-group">
						<button class="form-control btn  btn-default" onclick="window.location='/login/'" >
							Voltar Login <span class="glyphicon glyphicon-log-in"></span>
						</button>
					</div>
					<div class="btn-group">
						<button class="form-control btn  btn-primary" type="submit">
							Criar Conta <span class="glyphicon glyphicon-plus-sign"></span>
						</button>
					</div>
				</div>
			</div>
		</form>
	</center>

	{% include 'usuario/modals/senhasDiferentes.php' %}
</div>
{% endblock %}

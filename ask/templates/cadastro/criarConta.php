{% extends 'usuario/cabecalhoUser.php' %}

{% block page_atual %}"/criarConta/"{% endblock %}

{% block botoes_adicionais_esq %}{% endblock %}
{% block voltar %}/login/{% endblock %}
{% block sair_all %}{% endblock %}

{% block titulo %}
    Criar Conta
{% endblock %}


{% block conteudo %}
<div class="conteudo">
<center>
	<div class="form-login">
		<form class="form form-horizontal" role="form" onSubmit="return validaCriarConta()"  method="post">{% csrf_token %}
			<div class="col-sm-4">
			</div>
			<div class="col-sm-8">
				<h2>Criar Conta</h2>
				<br>
			</div>
			
			<div class="form-group">
				<label for="username" class="col-sm-4 control-label">Usuario</label>
				<div class="col-sm-8">
					<input id="username" class="form-control" name="username" required autofocus type="text" autocomplete="on" placeholder="Digite um nome de usuario">
				</div>
			</div>
			
			<div class="form-group">
				<label for="first_name" class="col-sm-4 control-label">Primeiro Nome</label>
				<div class="col-sm-8">
					<input id="first_name" class="form-control" name="first_name" required type="text" autocomplete="on" placeholder="Digite seu primeiro nome">
				</div>
			</div>
			
			<div class="form-group">
				<label for="last_name" class="col-sm-4 control-label">Segundo Nome</label>
				<div class="col-sm-8">
					<input id="last_name" class="form-control" name="last_name" required type="text" autocomplete="on" placeholder="Digite seu segundo nome">
				</div>
			</div>

			<div class="form-group">
				<label for="email" class="col-sm-4 control-label">Email</label>
				<div class="col-sm-8">
					<input id="email" class="form-control" name="email" required type="email" autocomplete="on" placeholder="Digite seu email">
				</div>
			</div>
			<div class="form-group">
				<label for="password" class="col-sm-4 control-label">Senha</label>
				<div class="col-sm-8">
					<input id="password" class="form-control" name="password" required="" type="password" placeholder="Digite sua senha">
				</div>
			</div>
			<div class="form-group ">
				<label for="password2" class="col-sm-4 control-label">Repita a Senha</label>
				<div class="col-sm-8">
					<input id="password2" class="form-control" name="password2" required="" type="password" placeholder="Repita sua senha">
				</div>
			</div>
			<div class="form-group">
				<div class="col-sm-4">
					
				</div>
				<div class="col-sm-4">
					<button class="form-control btn  btn-default" onclick="window.location='/login/'" >Cancelar</button>
				</div>
				<div class="col-sm-4">
					<button class="form-control btn  btn-primary" type="submit">Criar Conta</button>
				</div>
			</div>
		</form>
	</div>
</center>	
</div>

{% endblock %}

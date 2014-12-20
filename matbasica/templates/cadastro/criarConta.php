{% extends 'login/login.php' %}

{% block titulo %}
    Criar Conta
{% endblock %}

{% block conteudo_all %}
<div class="conteudo">
<center>
	<div class="form-login">
		<form  action="/user/register/" class="form-horizontal" role="form" method="post">{% csrf_token %}
			
			<div class="form-group">
				<label>Usuário</label>
				<input class="form-control" name="username" required autofocus type="text" autocomplete="on">
			</div>
			
			<div class="form-group">
				<label>Primeiro Nome</label>
				<input class="form-control" name="first_name" required type="text" autocomplete="on">
			</div>
			
			<div class="form-group">
				<label>Segundo Nome</label>
				<input class="form-control" name="last_name" required type="text" autocomplete="on">
			</div>

			<div class="form-group">
				<label>Email</label>
				<input class="form-control" name="email" required type="email" autocomplete="on">
			</div>
			<div class="form-group">
				<label>Senha</label>
				<input class="form-control" name="password" required="" type="password">
			</div>
			<div class="form-group">
			<button class="form-control btn  btn-primary" type="submit">Criar</button>
			</div>
			<div class="form-group">
				<button class="form-control btn  btn-primary" onClick="document.location='/login/'">Tentar Fazer Login</button>
			</div>
		</form>
	</div>
</center>	
</div>

{% endblock %}

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
		<form  action="/user/register/" class="form-horizontal" role="form" method="post">{% csrf_token %}
			
			<div class="form-group">
				<label>Nome de Usuário</label>
				<input class="form-control" name="username" required autofocus type="text" autocomplete="on" placeholder="Digite seu nome de usuario">
			</div>
			
			<div class="form-group">
				<label>Primeiro Nome</label>
				<input class="form-control" name="first_name" required type="text" autocomplete="on" placeholder="Digite seu primeiro nome">
			</div>
			
			<div class="form-group">
				<label>Segundo Nome</label>
				<input class="form-control" name="last_name" required type="text" autocomplete="on" placeholder="Digite seu segundo nome">
			</div>

			<div class="form-group">
				<label>Email</label>
				<input class="form-control" name="email" required type="email" autocomplete="on" placeholder="Digite seu email">
			</div>
			<div class="form-group">
				<label>Senha</label>
				<input class="form-control" name="password" required="" type="password" placeholder="Sua Senha">
			</div>
			<div class="form-group">
			<button class="form-control btn  btn-primary" type="submit">Criar Conta</button>
			</div>
		</form>
	</div>
</center>	
</div>

{% endblock %}

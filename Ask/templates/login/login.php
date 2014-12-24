{% extends 'usuario/cabecalhoUser.php' %}

{% block titulo %}
    Login
{% endblock %}

{% block page_atual %}"/login/"{% endblock %}

{% block botoes_adicionais_esq %}{% endblock %}
{% block voltar_all %}{% endblock %}
{% block sair_all %}{% endblock %}

{% block conteudo %}
	<div class="conteudo">
		<center>
			<div class="form-login login">
				<form class="form-vertical" method="post" role="form" action=".">{% csrf_token %}
					<input name="next" value="/principal/" type="hidden">

					<div class="form-group">
						<label>Usuário ou Email</label>
						<input id="id_username" class="form-control" maxlength="254" name="username" type="text" required autofocus autocomplete="on" placeholder="Digite seu nome de usuario ou email">
					</div>
					<div class="form-group">
						<label>Senha</label>
						<input id="id_password" class="form-control" name="password" type="password" required placeholder="Digite sua senha">
					</div>
					<div class="form-group">
						<input class="button form-control btn btn-primary" name="post" value="Entrar" type="submit">
					</div>
					<div class="form-group">
						<button type="button" class="form-control btn  btn-primary"  onClick="document.location='/criarConta/'">Criar Conta</button>
					</div>
				</form>
			</div>
		</center>
	</div>

{% endblock %}

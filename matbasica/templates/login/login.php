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
			<div class="form-login">
				<form class="form-vertical" method="post" role="form">{% csrf_token %}
					<div class="form-group">
						<label>Usuário</label>
						<input type="text" class="form-control" name="usuario" required autofocus autocomplete="on">
					</div>
					<div class="form-group">
						<label>Senha</label>
						<input type="password" class="form-control" name="senha" required >
					</div>
					<div class="form-group">
						<button type="submit" class="form-control btn btn-primary" >Entrar</button>
					</div>
					<div class="form-group">
						<button type="button" class="form-control btn  btn-primary"  onClick="document.location='/criarConta/'">Criar Conta</button>
					</div>
				</form>
			</div>
		</center>
	</div>

{% endblock %}

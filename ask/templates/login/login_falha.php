{% extends 'login/login.php' %}

{% block titulo %}
    Falha Login
{% endblock %}

{% block voltar_all %}{% endblock %}
{% block sair_all %}{% endblock %}


{% block conteudo %}
<div class="container">
<div class="col-xs-12 col-sm-12 col-md-12">
	<div class="row">
		<div class="conteudo">
				<div class="title-container">
					<center><h1>Falha ao Efetuar Login</h1>
				</div>
			<center>
				<button class="btn btn-primary caixa botao-1" onClick="document.location='/login/' ">
					Tentar Novamente <span class="glyphicon glyphicon-repeat"></span>
				</button>
			</center>
		</div>
	</div>
</div>
</center>
{% endblock %}

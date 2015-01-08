{% extends 'usuario/cabecalhoUser.php' %}

{% block titulo %}
    Falha Login
{% endblock %}

{% block botoes_adicionais_esq %}{% endblock %}
{% block voltar_all %}{% endblock %}
{% block sair_all %}{% endblock %}


{% block conteudo %}
<div class="col-md-12 col-xs-12">
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
{% endblock %}

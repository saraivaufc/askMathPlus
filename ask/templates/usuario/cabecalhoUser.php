{% extends 'basico.php' %}

{% block menu %}
<div id="barra-menu">

	<!-- Static navbar -->
      <div class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
				<span class="sr-only">Toggle navigation</span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="/principal/">
				AskMath <span class="glyphicon glyphicon-home"></span>
			</a>
          </div>
          <div class="navbar-collapse collapse">
				<ul class="nav navbar-nav">
					<li><a href="/forum/">
						Forum <span class="glyphicon glyphicon-globe"></span>
						</a>
					</li>
				</ul>

				<ul class="nav navbar-nav navbar-right">
					<li>
						<a href=".">
							<span class="glyphicon glyphicon-user"></span> {{ usuario.username }}
						</a>
					</li>
					<li>
						<a data-toggle="modal" data-target="#contato">
							Contato <span class="glyphicon glyphicon-envelope"></span>
						</a>
					</li>
					<li>
						<a data-toggle="modal" data-target="#sobre">
							Sobre <span class="glyphicon glyphicon-exclamation-sign"></span>
						</a>
					</li>
					<li>
						<a href="/logout/">
							Sair <span class="glyphicon glyphicon-log-out"></span>
						</a>
					</li>
				</ul>

				
          </div><!--/.nav-collapse -->
        </div><!--/.container-fluid -->
      </div>

<!--
	<div class="nav navbar bg-primary">
		<div class="container-fluid">
			<div class="row">
				<div class="col-xs-4 col-sm-4 col-md-4">
					<div class="col-xs-6 col-sm-6 col-md-6">
						<div class="navbar-header">
							<a class="navbar-brand" href="/principal/">
								<div id="title-system">
									AskMath <span class="glyphicon glyphicon-home"></span>
								</div>
							</a>
						</div>
					</div>
					<div class="col-xs-6 col-sm-6 col-md-6">
						<ul class="nav navbar-nav navbar-left">
							{% block botoes_adicionais_esq %}
								<li>
									<a id="forum" data-container="body" data-toggle="popover" data-placement="top" data-content="Use esse forum para quando tiver alguma duvida e nescessitar de ajuda de outros usuários ou bolsistas..."  onclick="window.open('/forum')">
										Forum <span class="glyphicon glyphicon-globe"></span>
									</a>
								</li>
							{% endblock %}
						</ul>
					</div>
				</div>

				<div class="col-xs-8 col-sm-8 col-md-8">
						<ul class="nav navbar-nav navbar-right">
									<li>
										<a href="/principal/">
											<span class="glyphicon glyphicon-user"></span> {{ usuario.username }}
										</a>
									</li>
								{% block botoes-menu-dir %}
									<li>
										<a data-toggle="modal" data-target="#contato">
											Contato <span class="glyphicon glyphicon-envelope"></span>
										</a>
									</li>
									<li>
										<a data-toggle="modal" data-target="#sobre">
											Sobre <span class="glyphicon glyphicon-exclamation-sign"></span>
										</a>
									</li>
								 {% endblock %} 
								{% block sair_all %}
									<li>
										<a  href="/logout/">
											Sair <span class="glyphicon glyphicon-log-out"></span>
										</a>
									</li>
								{% endblock %}
						</ul>
				</div>
			</div>
		</div>
	</div>    
-->

</div><!-- /.barra-menu -->


<div class="font-dconteudo">
 	{% include 'usuario/modals/sobre.php' %}
 	{% include 'usuario/modals/contato.php' %}
</div>


{% endblock %}

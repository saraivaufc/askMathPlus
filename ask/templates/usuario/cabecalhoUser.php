{% extends 'basico.php' %}

{% block menu %}
<div id="barra-menu">
    <div class="nav navbar bg-primary">
        <div class="container-fluid">
          	
        	<div class="navbar-header">
		    	<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
			        <span class="sr-only">Toggle navigation</span>
			        <span class="icon-bar"></span>
			        <span class="icon-bar"></span>
			        <span class="icon-bar"></span>
		      	</button>
		    	<a class="navbar-brand" href="/principal/"><div id="title-system">AskMath</div></a>
		    </div>



	        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
	            <ul class="nav navbar-nav">
	            	{% block botoes_adicionais_esq %}
			            <li><a onclick="window.open('/forum')"  href="#">Forum</a></li>
	            	{% endblock %}
	            </ul>
	            
	            <ul class="nav navbar-nav navbar-right">
	              	<li><a data-toggle="modal" data-target="#contato" href="#">Contato</a></li>
	             	 <li><a data-toggle="modal" data-target="#sobre" href="#">Sobre</a></li>
	              	{% block sair_all %}
	              		<li><a  href="/logout/">Sair</a></li>
	              	{% endblock %}
	            </ul>
	            
	        </div><!--/.nav-collapse -->
        </div><!--/.container-fluid -->
    </div><!--/.nav navbar -->    
</div><!-- /.barra-menu -->


<div class="font-dconteudo">
 	{% include 'usuario/modals/sobre.php' %}
 	{% include 'usuario/modals/contato.php' %}
</div>


{% endblock %}
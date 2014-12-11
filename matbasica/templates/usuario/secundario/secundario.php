{% extends 'usuario/cabecalhoUser.php' %}

    {% block conteudo-left %}
    <div class="conteudo-left">
      <div class="font-dconteudo">
        <div class="descricao-conteudo">
          <center>
            <h3>{{ conteudo.tema }}</h3>
          </center>
          <div class="espacamento"><t> {{ conteudo.descricao|safe }}<t> </div>
          <br>
        </div>
      </div>
    </div>
    {% endblock %}


    {% block conteudo-right %}

    <div class="conteudo-right">
    
    <div id="form-perguntas">
      <div class="font-dconteudo">
        <center>
          <h3>Pergunta</h3>
        </center>
        <t class="espacamento"> {{ pergunta.descricao|safe }} </t>
      </div>
      <form method="POST" id="perguntas" name="resposta">
      {%csrf_token %} 
      	   <input id="pergunta_atual" name="pergunta_atual" value="{{pergunta.id}}" type="hidden"> 
      	   <input id="conteudo_atual" name="conteudo_atual" value="{{conteudo.id}}" type="hidden">
        
        <ol>
          {% for item in itens %}
          <li type="A">
            <div class="font-dconteudo">
              <div class="espacamento-right">
                <input name="opcao" value="{{item.id|safe}}" required="" type="radio"><t>{{ item.descricao | safe }}</t> 
              </div>
            </div>
          </li>
          <br>
          {% endfor %}
        </ol>
      </form>
      </div>
      <div id="barra-responder" >
          <button id="pular" class="btn botao">Pular</button>
          <center>
            <div id="resultado_positivo" class="resultado hidden">
              Acertou!!!
            </div>
            <div id="resultado_negativo" class="resultado hidden">
              Errou!!!
            </div>
            <a id="ajuda" data-toggle="modal" data-target="#ajuda_modal"></a>
          </center>
          <button id="verificar"  class="btn botao">Verificar</button>
      </div>

    </div>


<!-- Modal Ajuda -->
<div class="modal fade" id="ajuda_modal" tabindex="-1" role="dialog" aria-labelledby="sobreLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
      </div>
      <div class="modal-body">
    <center>
    <div>
      <t id="ajuda_text">
      </t>
    </div>
    
    </center>
    </div>
  </div>
  </div>
</div>

{% endblock %}
{% block voltar_all%}
{% endblock %}

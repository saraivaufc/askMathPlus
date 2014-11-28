{% extends 'usuario/cabecalhoUser.php' %}

    {% block conteudo-left %}
    <div class="conteudo-left">
      <div class="font-dconteudo">
        <div class="descricao-conteudo">
          <center>
            <h3>{{ conteudo.tema }}</h3>
          </center>
          <div class="espacamento"> {{ conteudo.descricao }} </div>
          <br>
        </div>
      </div>
    </div>
    {% endblock %}
    {% block conteudo-right %}
    <div class="conteudo-right">
      <div class="font-dconteudo">
        <center>
          <h3>Pergunta</h3>
        </center>
        <p class="espacamento"> {{ pergunta.descricao | capfirst }} </p>
      </div>
      <form method="POST" id="perguntas" name="resposta" onsubmit="return verificarAcerto();">
      {%csrf_token %} 
      	   <input id="pergunta_atual" name="pergunta_atual" value="{{pergunta.id}}" type="hidden"> 
      	   <input id="conteudo_atual" name="conteudo_atual" value="{{conteudo.id}}" type="hidden">
        <ol>
          {% for item in itens %}
          <li type="A">
            <div class="font-dconteudo">
              <div class="espacamento-right"> <input id="opcao" name="opcao" value="{{item.id}}"
                  required="" type="radio"> {{ item.descricao | capfirst }} </div>
            </div>
          </li>
          <br>
          {% endfor %}
        </ol>
        <center> <button class="btn btn-success botao" type="submit">Responder</button>
        </center>
        <ul class="pager">
          <li class="previous"><a href="#">Anterior</a></li>
          <li class="next"><a href="#">Próxima</a></li>
        </ul>
      </form>
    </div>
{% endblock %}
{% block voltar %}'/principal/'{% endblock %}

# askMathPlus

O `askMathPlus` é um projeto Django desenvolvido para oferecer soluções interativas e educacionais relacionadas à matemática. Utilizando uma combinação de tecnologias avançadas, como Celery para tarefas assíncronas e Django Rest Framework para APIs, este projeto visa aprimorar o aprendizado e o ensino de conceitos matemáticos através de uma interface amigável e recursos interativos.

## Pré-requisitos

Antes de instalar o `askMathPlus`, certifique-se de ter o Python e o pip instalados em seu sistema. Este projeto foi testado no Python 2.7 e Django 1.7.11, então recomendamos usar um ambiente virtual para evitar conflitos de dependência.

## Instalação

Para instalar o `askMathPlus`, siga estes passos:

### Clone o repositório:
```sh
git clone https://github.com/saraivaufc/askMathPlus.git
cd askMathPlus
```

### Instale as dependências:

Copy code
```sh

pip install -r requirements.txt
```

### Configure o banco de dados em settings.py conforme necessário.


### Realize as migrações:

```shell
python manage.py migrate
```


### Inicie o servidor de desenvolvimento:

```shell
python manage.py runserver
```

Agora você pode acessar o askMathPlus localmente em http://localhost:8000.


## Uso

### Tela inicial

![alt text](/Documentation/Capturas%20de%20Tela/askmath_1.png)

### Tela com lições de Proposições

![alt text](/Documentation/Capturas%20de%20Tela/askmath_2.png)

### Tela de problemas do estudante

![alt text](/Documentation/Capturas%20de%20Tela/askmath_3.png)

### Tela de uma postagem no fórum

![alt text](/Documentation/Capturas%20de%20Tela/askmath_4.png)

### Tela de administração

![alt text](/Documentation/Capturas%20de%20Tela/askmath_5.png)

### Tela de problemas do administrador

![alt text](/Documentation/Capturas%20de%20Tela/askmath_6.png)

Para mais detalhes, acesse: [https://www.repositorio.ufc.br/bitstream/riufc/24958/1/2016_tcc_mmsaraiva.pdf](https://www.repositorio.ufc.br/bitstream/riufc/24958/1/2016_tcc_mmsaraiva.pdf)

## Contribuindo
Contribuições são sempre bem-vindas! Para contribuir, por favor:

* Faça fork do projeto.
* Crie uma nova branch para sua feature (git checkout -b feature/NovaFeature).
* Faça commit de suas alterações (git commit -am 'Adiciona alguma NovaFeature').
* Push para a branch (git push origin feature/NovaFeature).
* Abra um Pull Request.

## Licença

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>

## Contato

Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato através do e-mail saraiva.ufc@gmail.com
# API Web com Python a FastAPI
*API Web com Python e FastAPI para disciplina de Banco de Dados*<br><br>
Para construir essa API foi necessário a instalação de dois pacotes do Python:<br>
- O primeiro pacote será o ***FastAPI***, um framework web para construção de API's usando python.
- Em seguida, foi utilizado o ***Uvicorn***, que é uma implementação de servidor ASGI para python.

**FastAPI**
>`python -m pip install fastapi`
 
 **Uvicorn**
 >`python -m pip install uvicorn`

<br>

***

### Executando o servidor da API
Após a instalação dos pacotes basta executar o seguinte comando no terminal, no caminho em que se encontra os arquivos da API:
>`python -m uvicorn main:app --reload`

O servidor iniciará e exibirá as seguintes informações:
![terminal exibindo o servidor uvicorn funcionando](/images/uvicorn_output.png)

O servidor estará rodando em localhost: `http://127.0.0.1:8000`

<br>

***

### Documentação da API web
Após ter iniciado o servidor através do comando acima, basta acessar:
>`http://127.0.0.1:8000/docs`

A documentação então será exibida por meio do ***SwaggerUI*** que é automaticamente criado pelo framework *FastAPI*:
![documentação da API](/images/api_documentation_swagger.png)
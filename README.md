# Model Serving Fast API

## Descrição

O ModelServingFastAPI é uma aplicação Python que utiliza o framework FastAPI e ASGI web-server Uvicorn (ou Gunicorn com workers Uvicorn) para fornecer previsões com base em um modelo de aprendizado de máquina pré-treinado no formato .joblib `(1.1.0)` do tipo scikit-learn `(1.0.1)`. Esta aplicação utiliza um banco de dados SQLite local (arquivo .sqlite3) para armazenar informações das requisições, interagindo por meio de SQLAlchemy como ORM. A aplicação também registra os logs do server em um arquivo em formato .txt.

## Pré-requisitos

Os requisitos para executar a aplicação estão inseridos dentro do arquivo `environment.yml `environment.yml que pode ser carregado através do genrenciador de pacotes conda.

**OBS.:** O arquivo foi gerado em OS UNIX, podendo levar a conflitos em sistemas Windows.

Como segunda opção, consultar o arquivo `requirements.txt`.

## Configuração

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/michelhilg/model-serving-fastAPI.git
    cd model-serving-fastAPI
    ```

2. **Instale as dependências:**

    ```bash
    conda env create -f environment.yml
    conda activate fastapi
    ```

    Isso criará um ambiente Conda chamado `fastapi` com as dependências especificadas no arquivo `environment.yml`.

    Ou

    ```bash
    conda create --name fastapi python=3.8
    conda activate fastapi
    pip install -r requirements.txt
    ```

   Isso criará um ambiente Conda chamado `fastapi` com base nas especificações no arquivo `requirements.txt`.

   **OBS.:** Caso encontre problemas, vale a pena conferir a incompatibilidade de OS.

3. **Crie um arquivo de ambiente (`.env`) com as seguintes variáveis:**

    ```dotenv
    ENV_NAME = "Environment"
    BASE_URL = "http://127.0.0.1:8000"
    DB_URL = "sqlite:////path/to/your/database/file/db.sqlite3"
    LOG_PATH = "path/to/your/log/file/log.txt"
    PATH_MODEL = "path/to/your/model/file/modelo.joblib"
    DESIRED_TIMEZONE = "timezone_here"   
    ```

   Certifique-se de ajustar os caminhos de acordo com a localização dos seus arquivos. O arquivo pode ser criado utilizando-se como base o arquivo .env.template.
   
   Essa aplicação possuí um arquivo `config.py` o qual carrega as informações definidas dentro do `.env` para cada modo ambiente de execução definido acima. O `config.py` também defini um backup para as variáveis de ambiente, você pode modificar se achar necessário. 

   Caso não seja fornecida uma `DESIRED_TIMEZONE` no arquivo `.env` será utilizado `Etc/UTC` para rodar a aplicação.

   Para os arquivos `db.sqlite3`, `modelo.joblib` e `log.txt`, você pode usar a estrutura de pastas recomendada.

4. **Modelo**

    Certifique-se de disponibilizar o modelo de machine learning adequado para aplicação, seguindo requisitos essenciais:

    - Formato: `.joblib` `(1.1.0)`
    - Versão scikit-learn: `1.0.1`

    Arquitetura testada foi a LinearRegression, porém outras arquiteturas que recebam duas features de entrada também são compatíveis.

## Uso

- **Para iniciar o APP, execute o seguinte comando:**

    ```bash
    uvicorn main:app --log-config log/log.ini
    ```

    A API estará acessível no endereço descrito no arquivo `.env` para variável `BASE_URL`. Por padrão, o caminho definido é [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

    Como a aplicação roda diretamente no Uvicorn, não é necessário passar outros comandos de na CLI para rodar em modo produção usando Uvicorn, apenas modificar as variáveis de acordo no arquivo `.env`.

- **Para iniciar o APP, com uso do Gunicorn, execute o seguinte comando:**

    Você pode usar o web-server Gunicorn com workers Uvicorn para ganhar mais velocidade em modo produção. Para isso, execute o seguinte comando:

    ```bash
    gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --log-config log/log.ini
    ```
    
    Em que:

    - `w` = Número de Uvicorn workers.

    A API estará acessível no endereço descrito no arquivo `.env` para variável `BASE_URL`. Por padrão, o caminho definido é [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Documentação

Você pode acessar a documentação da API, como o endpoints definido, acessando [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) via `Swagger`.

### Rotas

- **`POST /prediction`:** Envie dados de features no corpo da requisição para obter uma previsão. Exemplo de corpo da requisição:

    ```json
    {
        "feature_1": 0.5,
        "feature_2": 1.0
    }
    ```

    Para testar essa aplicação você pode usar ferramentas como o `Postman`, ótimo para teste de APIs.

## Banco de Dados

A aplicação utiliza um banco de dados SQLite para armazenar os dados das solicitações à API via SQLAlchemy. O arquivo de banco de dados e tabela `prediction` são automaticamente criados se não existir. O `id` de cada requisição é incrementado automaticamente. Para requisições realizadas com sucesso os valores de `feature_1`, `feature_2` e `predicao` também são gravados.

Lembre-se de configurar o caminho de sua database no arquivo de ambiente `.env`.

## Log

As operações da aplicação são registradas em um arquivo de log em formato de texto especificado no arquivo `.env`.

## Contribuindo

Sinta-se à vontade para contribuir!

# Instruções para subir o projeto

Siga as etapas abaixo para configurar o funcionamento do projeto.

## Database

A base de dados é PostgreSQL.

Para inicializar:

- Abra uma nova instância do terminal
- Entre na pasta database: `cd database`
- Execute o script: `./start.sh`

A base deve ser inicializada e já criar a tabela `product.product`.

## Backend

O backend foi desenvolvido na linguagem Python, usando a biblioteca FastAPI.

Para inicializar:

- Abra uma nova instância do terminal
- Entre na pasta backend: `cd backend`
- Crie um ambiente virtual: `python3 -m venv venv_prova`
- Ative o ambiente virtual: `source venv_prova/bin/activate`
- Instale as dependências do projeto: `pip install -r requirements.txt`
- Execute o script: `./start.sh`

Após isso o backend deverá estar acessível pela URL: <http://http://localhost:8081>.

## Cron

A cron executa um código em Python que remove os arquivos *.csv de dentro da pasta de uploads.

Para executar:

- Abra uma nova instância do terminal
- Entre na pasta backend: `cd backend`
- Ative o ambiente virtual: `source venv_prova/bin/activate`
- Execute o script: `./cron.sh`

## Frontend

Para inicializar:

- Abra uma nova instância do terminal
- Entre na pasta frontend: `cd frontend`
- Instale as dependências do projeto: `npm install`
- Inicie o servidor de desenvolvimento: `npm run serve`

Após isso o frontend deverá estar acessível pela URL: <http://http://localhost:8080>.

Para testar a importação de arquivos, existe um arquivo `exemplo.csv` na pasta principal do repositório.

# Instalando o Docker Compose e Iniciando o Ambiente

Considerando que você já tem o Docker instalado, execute os seguintes comandos para instalar o Docker Compose.

```sh
sudo su
COMPOSE_VERSION=1.24.0
curl -L https://github.com/docker/compose/releases/download/$COMPOSE_VERSION/docker-compose-`uname -s`-`uname -m` > /usr/bin/docker-compose
chmod +x /usr/bin/docker-compose
exit
```

## Inicie os conteiners

Use os comandos a seguir para iniciar os conteineres.

```sh
docker compose up
```

Para visualizar os logs de todos os conteineres, use o comando abaixo.

```sh
docker-compose -f docker-compose.yml logs
```

Para visualizar os logs de um conteiner especifico, digite:

```sh
docker-compose -f docker-compose.yml logs NOME_SERVICO
```

O nome do serviço é declarado no arquivo ``docker-compose.yml``. 

Exemplo:

```sh
docker-compose -f docker-compose.yml logs backend
```

Use os comandos a seguir para parar e remover os conteineres.

```sh
docker-compose -f docker-compose.yml stop
docker-compose -f docker-compose.yml rm
```

Para obter mais informações sobre o Docker Compose acesse:

* [https://docs.docker.com/compose/reference/](https://docs.docker.com/compose/reference/)
* [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)


## Iniciando ambiente com a pipeline e helmfile

Use os comandos a seguir para instalar o helmfile

```sh
curl -L https://github.com/helmfile/helmfile/releases/latest/download/helmfile_$(uname -s)_amd64.tar.gz | tar xz
sudo mv helmfile /usr/local/bin/
```

Installe também o plugin do helmdiff

```sh
helm plugin install https://github.com/databus23/helm-diff
```
Installe também o python

```sh
#!/bin/bash

# Instala dependências
sudo apt update
sudo apt install -y wget build-essential libssl-dev zlib1g-dev \
  libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev \
  libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev

# Baixa e instala Python 3.12.3
cd /tmp
wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
tar -xvf Python-3.12.3.tgz
cd Python-3.12.3
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall

# Verifica a instalação
python3.12 --version

```

## Executando a pipeline

Agora podemos rodar o comando abaixo para executar a pipeline

```sh
python pipeline.py
```
Obs: Esse comando tem que ser utilizado no mesmo diretorio onde está a pipeline.py

A pipeline vai fazer:

- build das imagens dockerfile
- publish das imagens com as tags
- executar o deploy no cluster e subir os pods
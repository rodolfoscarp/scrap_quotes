# Bot Scrap Quotes

O projeto faz acesso a [página](https://quotes.toscrape.com) e faz a raspagem das frases juntamente com o autor e suas tags, após os dados são salvos em um banco de dados sqlite e enviados a uma API extrena.

## requisitos

- `Python 3.12`
- `Navegador Google Chrome` (apenas local)

### Execução via Docker

- `Docker`
- `Docker Compose`

## Instalação e Execução

- Clone o repositório: `git clone https://github.com/rodolfoscarp/scrap_quotes.git`
- Acesse o diretório do projeto: `cd <caminh_projeto>/scrap_quotes`
- Crie e edite um arquivo `.env`. Use modelo .env.example.
  - `PAGES`: Quantidade de páginas a raspar.
  - `APIURL`: A URL POST para envio dos dados.
  - `HEADLESS`: Executar o navegador em modo headless

Obs: Utilize a URL: `https://67f67d5c42d6c71cca62461c.mockapi.io/api/quotes` para testes.

### Execução Local

- Crie um ambiente virtual: `python -m venv venv` ou outra ferramenta similar.
- Ative o ambiente virtual: `venv\Scripts\activate.bat` ou comando de ativação do ambiente.
- Instale as dependências: `pip install -r requirements.txt`
- Execute o script:  `python main.py`

#### Criar Execurtavel

Ainda é possui criar um executavel standalone.

- Faça todas as etapas anteriores
- execute `pyinstaller scrap_quotes.spec`

### Execução Via Docker

- Faça todas as etapas anteriores
- Execute o docker-compose: `docker compose -f "docker-compose.yml" up -d`

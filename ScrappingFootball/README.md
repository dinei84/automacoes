# Scrapping Football

Projeto simples em Python para monitorar informações de jogos de times de futebol usando Flask e Playwright.

## Dependências

Instale as dependências usando o `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

### Bibliotecas principais

- `Flask` - para rodar a interface web
- `playwright` - para navegar pelo site e extrair as informações
- `gunicorn` - servidor de produção usado no Render

### Instalar navegadores do Playwright

Após instalar as bibliotecas, execute:

```bash
python -m playwright install chromium
```

Isso baixa o navegador Chromium necessário para o Playwright funcionar corretamente no Render.

## Como usar localmente

### 1. Rodar a aplicação web

```bash
python scrappingfootbla.py
```

Abrir no navegador:

```bash
http://localhost:5000
```

### 2. Rodar o scraper via linha de comando

```bash
python scrappingfootbla.py --cli
```

Isso executa a coleta para todos os times definidos em `TIMES_PARA_MONITORAR` e imprime os resultados no terminal.

## Deploy no Render

O projeto já foi preparado para deploy no Render com os seguintes ajustes:

- `requirements.txt` agora inclui `gunicorn`.
- `scrappingfootbla.py` usa `PORT` via `os.environ.get("PORT", "5000")`.
- Um arquivo `render.yaml` foi adicionado para configurar o serviço Web no Render.
- O workflow GitHub Actions foi atualizado para instalar o navegador Chromium do Playwright.

### Configuração recomendada no Render

1. No painel do Render, crie um novo serviço `Web Service`.
2. Conecte ao repositório `automacoes/ScrappingFootball`.
3. Caso use o `render.yaml`, o Render lerá estas configurações automaticamente.
4. Se configurar manualmente, use:
   - `Build Command`: `pip install -r requirements.txt && playwright install chromium`
   - `Start Command`: `gunicorn scrappingfootbla:app --bind 0.0.0.0:$PORT`
5. Adicione variáveis de ambiente no Render se precisar (opcional):
   - `FLASK_ENV=production`
   - `PYTHONUNBUFFERED=1`

### Deploy via GitHub Actions

Se quiser deploy automático pelo GitHub Actions, configure:

- Secret `RENDER_API_KEY` no repositório GitHub.
- Workflow em `.github/workflows/render.yaml` com `project-name: scrappingfootball` ou altere para o nome real do serviço no Render.

### Observações finais

- O arquivo `render.yaml` existe no repositório e descreve o serviço para o Render.
- O comando principal de produção é `gunicorn scrappingfootbla:app --bind 0.0.0.0:$PORT`.
- Se preferir, você pode usar apenas a configuração do painel do Render e não depender do GitHub Action.

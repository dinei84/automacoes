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

### Instalar navegadores do Playwright

Após instalar a biblioteca, execute:

```bash
python -m playwright install
```

Isso baixa os navegadores necessários para o Playwright funcionar corretamente.

## Como usar

### 1. Rodar a aplicação web

```bash
python scrappingfootbla.py
```

Abrir no navegador:

```
http://localhost:5000
```

Selecione um time e clique em buscar para ver o horário e a transmissão do próximo jogo.

### 2. Rodar o scraper via linha de comando

```bash
python scrappingfootbla.py --cli
```

Isso executa a coleta para todos os times definidos em `TIMES_PARA_MONITORAR` e imprime os resultados no terminal.

## Observações

- O projeto busca informações no site do Globo Esporte.
- Caso não encontre o link de "onde assistir", o resultado exibirá uma mensagem de erro.

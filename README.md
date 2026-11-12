# Exercício 9.4 — Flask e Nuvem

API RESTful em Python com Flask para o Laboratório 09 de Engenharia de Software.

## Rotas

| Método | Rota | Função |
|---|---|---|
| GET | `/` | Página inicial em JSON |
| GET | `/tarefas` | Listar tarefas |
| POST | `/tarefas` | Criar tarefa |
| PUT | `/tarefas/1` | Atualizar tarefa 1 |
| DELETE | `/tarefas/1` | Excluir tarefa 1 |

Use JSON `{"descricao":"Estudar Flask"}` para POST e PUT. O aplicativo inicia com uma tarefa de ID 1. Respostas: GET 200, POST 201, PUT 200, DELETE 200, dados inválidos 400 e tarefa ausente 404.

## Executar localmente

```bash
python -m pip install -r requirements.txt
python app.py
```

Abra `http://127.0.0.1:5000/tarefas`.

## Postman

Importe o arquivo `postman_collection.json` e altere a variável `baseUrl` para a URL publicada na Azure quando necessário. O padrão é `http://127.0.0.1:5000`.

## Azure

Crie um App Service Linux para Python, conecte a branch `main` ao GitHub Actions no Deployment Center e acompanhe o deploy na aba Actions. Caso seja necessário definir o startup command, use `gunicorn app:app`.

**Atenção:** os dados são mantidos apenas em memória; não persistem após reinício e podem variar entre processos na nuvem. Este projeto é apenas um exemplo didático.

## Entrega

O professor solicita link para o código, link do repositório, link da aplicação online e link da coleção do Postman.

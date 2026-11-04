# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, usando métodos HTTP, modelos de dados e códigos de status para gerenciar recursos.

## 📝 Tarefas

### 🛠️ Criar os Endpoints de Leitura

#### Descrição
Use o código inicial para criar endpoints que consultem os itens armazenados em memória.

#### Requisitos
O programa concluído deve:

- Criar um endpoint `GET /items` que retorne todos os itens
- Criar um endpoint `GET /items/{item_id}` que retorne um item pelo ID
- Retornar o status HTTP `404` quando o ID solicitado não existir
- Disponibilizar a documentação interativa da API em `/docs`

### 🛠️ Implementar as Operações de Escrita

#### Descrição
Expanda a API para permitir criar, atualizar e remover itens. Use os modelos Pydantic definidos no código inicial para validar os dados recebidos.

#### Requisitos
O programa concluído deve:

- Criar itens por meio de `POST /items` e retornar o status HTTP `201`
- Atualizar um item existente por meio de `PUT /items/{item_id}`
- Remover um item por meio de `DELETE /items/{item_id}`
- Retornar o status HTTP `404` ao tentar atualizar ou remover um item inexistente
- Validar os dados de entrada e retornar respostas JSON consistentes

Para executar a API, instale `fastapi` e `uvicorn` e inicie o servidor com `uvicorn starter-code:app --reload`.

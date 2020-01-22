# teste-celero

Este projeto contém a implementação do Desafio Celero para Back-End, utilizando os frameworks Django e Django REST Framework.

## Versões utilizadas
* Python: 3.8.1
* Django: 3.0.2
* Django REST: 3.11.0

## Código
O diretório raiz do projeto é o `src/`, onde se encontram o arquivo `manage.py` (Django) e também o script para popular os modelos a partir do arquivo `athlete_events.csv`. Todas as funções da API se encontram no diretório `api`, no componente `olympics (src/olympics/api/)`

### Pré-Requisitos
É necessário que o arquivo CSV para popular os modelos esteja no diretório raiz com o nome `athlete_events.csv`, juntamente com o script `populate.py`

### Script para popular os modelos
Para executar o script (depois de executar os comandos de migração como makemigrations e migrate), é necessário passar como argumento o modelo que deseja popular (athlete ou event)
```
python populate.py athlete
```
Ou, para o modelo Event:
```
python populate.py event
```
**Observação: Caso seja necessário popular os dois modelos, o modelo Athlete deve ser populado primeiro.**

## Execução
Para executar o projeto (após executar os comandos de migração como makemigrations e migrate), basta executar
```
python manage.py runserver
```
no diretório raiz, e acessar as rotas da API no endereço de `localhost` na porta `8000`

## API
As rotas para a interação com os modelos são:

### Rotas do modelo Athlete
`/api/olympics/athlete` para a listagem de todos os atletas e para a criação de um novo atleta

Filtros:
* name (Exemplo: `/api/olympics/athlete?name=Teste`)
* sex (Exemplo: `/api/olympics/athlete?sex=M`)
* age (Exemplo: `/api/olympics/athlete?age=23`)

`/api/olympics/athlete/<id>` para a leitura, atualização e deleção de um atleta específico, indicado pelo campo <id>

Exemplo: `api/olympics/athlete/45`, para operações com o atleta de id 45

### Rotas do modelo Event
`/api/olympics/event` para a listagem de todos os eventos e para a criação de um novo evento

Filtros:
* team
* year
* season
* sport
* medal

Exemplo de filtros:
```
/api/olympics/event?team=China&year=2008
/api/olympics/event?sport=Skiing&medal=Gold
```

## Testes
Testes unitários básicos se encontram no arquivo `tests.py` no diretório `api`, e para executá-los basta executar
```
python manage.py test
```

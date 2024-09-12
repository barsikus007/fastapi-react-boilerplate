# Backend

## For local type checking and suggestion (developer mode)

### Install uv

```bash
# linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# windows (https://scoop.sh)
scoop install uv
```

### Install packages

Be sure that you are in `backend/` dir

```bash
uv venv
uv pip install -r requirements.txt
# uv sync --frozen --no-install-project
```

### Point your IDE to virtual environment

It is automatic in vscode but in other IDEs you could point it manually

¯\\\_( ͡° ͜ʖ ͡°)_/¯

## Launch

- Copy `.env.example` to `.env` and change settings
- `uvicorn src.main:app --reload --host 0.0.0.0'`

## May be useful

### Debug inside docker

- `docker compose -f compose.yaml -f compose.debug.yaml up -d --build`
- then use debugpy to connect with container

### Run psql

`source .env && docker compose exec -it postgres-dev psql -U $POSTGRES_USER`

### [docker pg_dump](https://stackoverflow.com/a/29913462)

```bash
docker compose exec -t postgres-dev pg_dumpall -c -U postgres > dump_`date +%Y-%m-%d'_'%H_%M_%S`.sql

cat dump_%Y-%m-%d_%H_%M_%S.sql | docker exec -i your-db-container psql -U postgres
```

### alembic cheatsheet

```bash
alembic revision --autogenerate -m "Migration name"
alembic upgrade head
alembic downgrade -1
alembic downgrade base
```

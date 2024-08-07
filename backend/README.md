# Backend

## For local type checking and suggestion (developer mode)

### Install python

#### On Windows

I recommend [scoop](https://scoop.sh) package manager

```pwsh
scoop install python312
```

#### On Linux

You already have python, just be sure that you have 3.12 version with venv installed

If your version is lower, then find the way to install it on your distro

Here is the most common distro installation instruction:

##### On Ubuntu

```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install build-essential python3.12-dev python3.12-venv -y
```

##### Other

If your distro haven't prebuilt package, then you can use [pythonz](https://github.com/saghul/pythonz)

### Install packages

Be sure that you in backend dir

#### On Windows

```pwsh
py -m venv venv
venv\Scripts\pip install --upgrade pip wheel setuptools
venv\Scripts\pip install -r requirements.txt
```

#### On Linux

```bash
python3.12 -m venv venv
venv/bin/pip install --upgrade pip wheel setuptools
venv/bin/pip install -r requirements.txt
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

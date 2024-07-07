# fastapi-react-boilerplate

## Features

- boilerplate
- ???
- PROFIT
- (and cute http.cat error pages)

## Installation

### Install docker

#### On Windows

##### Windows 11 or with winget installed

```pwsh
wsl --install -d Ubuntu
winget install Docker.DockerDesktop -h
```

##### Below Windows 11

[Installer](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)

#### On Linux

[Convinient script](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)

```sh
# install docker
curl -sSL https://get.docker.com | sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker; exit
```

#### On MacOS

[Installer](https://docs.docker.com/desktop/install/mac-install/)

#### Arm issues resolution

Due to possible issues with several packages, which haven't builds for linux aarch64, you can use buildx

```sh
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose up -d --build {issued-service}
docker-compose up -d --build {other-services}
```

### Launch app

Copy `.env.example` to `.env` and change settings

#### Development mode

```sh
docker compose up -d --build
```

#### Production mode

```sh
docker compose -f compose.prod.yaml up -d --build
```

### Untemplating

- `s/fastapi-react-boilerplate/your-project-name/g`

## FastAPI React Boilerplate TODO

### frontend

- port new things
  - `*.svg?react`
  - <https://tanstack.com/router/latest/docs/framework/react/guide/external-data-loading#a-more-realistic-example-using-tanstack-query>
    - <https://tanstack.com/router/latest/docs/framework/react/examples/kitchen-sink-react-query-file-based>
  - example usage
    - dayjs
    - react-query
    - tanstack-table
  - styled typography and theming
- to project
  - BACKEND_URL env var
  - remove App.css
  - [ts models from backend](https://fastapi.tiangolo.com/advanced/generate-clients/)
    - [OpenAPI object](https://github.com/ferdikoomen/openapi-typescript-codegen/wiki/OpenAPI-object)
    - task to generate models from backend ?
    - zod ?
- discuss
  - react-query enough as state manager or use effector (or what) ?
  - <https://github.com/lukemorales/query-key-factory>

### backend

- other
  - pylint(too-few-public-methods) on sqlalchemy models
  - use return 201 when create
  - fix return casting `# type: ignore`
  - SQLAlchemy 2.0
    - pydantic.dataclasses.dataclass fix
    - relation model examples
    - onupdate timestamps
  - pip install or pip wheel
    - why pip wheel --no-deps ?
  - hide docs in prod (None to docs and openapi schema)
  - form-multipart test
  - gunicorn logging disable
  - ruff
    - wemake-python-styleguide
  - --proxy-headers <https://fastapi.tiangolo.com/deployment/docker/#behind-a-tls-termination-proxy>
    - other nginx configurations from uvicorn docs
      - better nginx location sctucture (global fastapi location)
  - poetry ?
    - <https://fastapi.tiangolo.com/deployment/docker/#docker-image-with-poetry>
    - <https://gabnotes.org/posts/lighten-your-python-image-docker-multi-stage-builds/>
- arch related
  - <https://docs.sqlalchemy.org/en/20/changelog/migration_20.html#migration-20-step-six>
  - errors
    - rewrite status codes to status consts
      - conflicts with current errors to schema solution
        - make own solution
  - remake structure to more convinient usage
    - make schema autogeneration from models
      - basinc cases only (user is very unusual for example)
    - how to remove fields when inherit pydantic models
- libs related
  - loguru -> default logging ? (with <https://github.com/hynek/structlog>)
  - pendulium
  - apscheduler 4
  - <https://github.com/faust-streaming/faust>
  - uuid7

### devops

- tasks for database backup and restore
- file serving example
  - nginx serve static files
  - max filesize deps for FastAPI
  - nginx client_max_body_size 100M;
  - GUID in env or another workaround for correct file rights (container user not root) (migrations for example)
- update && fix compose.debug.yaml
  - backend
  - frontend
- docker secrets
- prod related
  - docker swarm config ?
  - k8s config ?
  - make different image names (or tags) for different compose files
  - <https://florian-kromer.medium.com/fastapi-microservice-patterns-3052c1241019>
  - <https://stribny.name/blog/fastapi-production/>
  - Add CI/CD example
    - github and/or gitlab ?
    - what and how?
      - tests/lints/checks
      - deploys
      - docker builds?
- nginx to traefik ?
  - https is easier in traefik

### other

- <https://containers.dev>
- examples
  - <https://github.com/testdrivenio/fastapi-sqlmodel-alembic>
  - <https://github.com/nsidnev/fastapi-realworld-example-app>
    - <https://github.com/nsidnev/fastapi-realworld-example-app/blob/master/app/db/migrations/versions/fdf8821871d7_main_tables.py#L20>
- vscode workspace
  - recommended extensions
  - tasks
    - .env file parse (use script for that)
    - openapi schema based mock filler
  - move backend/frotnend specific to own folders
    - (don't move tasks needed for dev mode)
- ./backend#on-ubuntu
  - add bedian (asdf or pyenv)

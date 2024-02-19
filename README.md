# Installation

## Install docker

### On Windows

#### Windows 11 or with winget installed

```pwsh
wsl --install -d Ubuntu
winget install Docker.DockerDesktop -h
```

#### Below Windows 11

[Installer](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)

### On Linux

[Convinient script](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)

```sh
# install docker
curl -sSL https://get.docker.com | sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker; exit
```

### On MacOS

[Installer](https://docs.docker.com/desktop/install/mac-install/)

### Arm issues resolution

Due to possible issues with several packages, which haven't builds for linux aarch64, you can use buildx

```sh
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose up -d --build {issued-service}
docker-compose up -d --build {other-services}
```

## Launch app

Copy `.env.example` to `.env` and change settings

### Development mode

```sh
docker compose up -d --build
```

### Production mode

```sh
docker compose -f compose.prod.yaml up -d --build
```

## Untemplating

- `s/fastapi-react-boilerplate/your-project-name/g`

## FastAPI React Boilerplate TODO

### frontend

- port new things
  - `*.svg?react`
  - react-router 6.4+ data api
    - <https://tkdodo.eu/blog/react-query-meets-react-router>
    - new <https://tanstack.com/> libs
      - react-router or tanstack/router
  - example usage
    - dayjs
    - react-query
    - tanstack-table
  - styled typography and theming
  - bun && front & back dockerfile todo
    - yarn v3 berry vs pnpm vs bun
      - <https://github.com/yarnpkg/berry/issues/4217>
      - <https://github.com/remix-run/remix/issues/683>
- to project
  - remove App.css
  - ts models from backend <https://fastapi.tiangolo.com/advanced/generate-clients/>
    - task to generate models from backend ?
- discuss
  - react-query enough as state manager or use effector (or what) ?

### backend

- other
  - postgres `FATAL:  role "root" does not exist` spam
  - pylint(too-few-public-methods) on sqlalchemy models
  - use return 201 when create
  - fix return casting type: ignore
  - pydantic.dataclasses.dataclass fix
  - relation model examples
  - onupdate timestamps
  - pip install or pip wheel
    - why pip wheel --no-deps ?
  - prod None to docs and openapi
  - add backend cors
  - form-multipart test
  - gunicorn logging disable
  - use ruff
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
    - errors to schema
    - auto HTTPErrors (like IResponse) (maybe with cats)
  - return status code and data in return???
    - [+] protocol agnostic
    - [+] custom response codes
    - [-] overhead
  - remake structure to more convinient usage
    - make schema autogeneration from models
      - basinc cases only (user is very unusual for example)
    - how to remove fields when inherit pydantic models
- libs related
  - passlib[bcrypt] to passlib[argon2] ?
  - padantic 2 when released
    - <https://docs.pydantic.dev/dev-v2/migration/>
    - dotenv settings parsing
  - loguru -> default logging ? (with <https://github.com/hynek/structlog>)
  - pendulium
  - apscheduler 4
  - <https://github.com/faust-streaming/faust>

### devops

- file serving example
  - nginx serve static files
  - max filesize deps for FastAPI
  - nginx client_max_body_size 100M;
  - GUID in env or another workaround for correct file rights (container user not root) (migrations for example)
- rename docker-compose.yml to compose.yml
  - compose.prod.yml?
    - mix it with usual compose file to run prod with docker database example
- docker secrets
- Remove dockerignore ?
  - <https://pnpm.io/docker#example-1-build-a-bundle-in-a-docker-container>
- prod related
  - Add restart to docker services unlike pg ?
  - docker swarm config ?
  - k8s config ?
  - make different image names (or tags) for different compose files
    - fix debug compose
  - <https://florian-kromer.medium.com/fastapi-microservice-patterns-3052c1241019>
  - <https://stribny.name/blog/fastapi-production/>
  - Add CI/CD example
    - github or gitlab ?
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
- vscode workspace recommended extensions
- ./backend#on-ubuntu
  - add bedian (asdf or pyenv)

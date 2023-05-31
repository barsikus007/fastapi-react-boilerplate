# Installation
## Install docker
#### On Windows
##### Windows 11 or with winget installed
```pwsh
wsl --install -d Ubuntu
winget install Docker.DockerDesktop -h
```
##### Below Windows 11
[Installer](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)
#### On Linux
```bash
# install docker
curl -sSL https://get.docker.com | sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker; exit

# install docker compose
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-$(uname -i) -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
```
#### On MacOS
[Installer](https://docs.docker.com/desktop/install/mac-install/)
##### Apple Silicon launch instruction
Due to some issues with several python packages (like asyncpg), which haven't builds for linux aarch64, you should use buildx
```zsh
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose up -d --build
# Then to accelerate frontend, if you are frontend dev, build frontend without buildx
docker-compose up -d --build frontend
```
## Launch app in development mode
###### Note, that on windows you must use WSL if you are frontend developer due to react-scripts@5.0.0 bug with hot reloading
```bash
docker compose up -d --build
```
## Launch app in production mode
```bash
docker compose -f "docker-compose.prod.yml" up -d --build
```
# Boilerplate TODO
- examples
  - https://github.com/testdrivenio/fastapi-sqlmodel-alembic
  - https://github.com/nsidnev/fastapi-realworld-example-app
    - https://github.com/nsidnev/fastapi-realworld-example-app/blob/master/app/db/migrations/versions/fdf8821871d7_main_tables.py#L20
- vscode workspace recommended extensions
## frontend
- remove App.css
- node 20
- ts models from backend https://fastapi.tiangolo.com/advanced/generate-clients/
- react-router 6.4+ data api
- react-query as state manager or effector
- new https://tanstack.com/ libs
  - react-query update to v4
  - react-router or tanstack/router
- add usage examples of
  - dayjs
  - react-query
- yarn v3 berry vs pnpm
  - https://github.com/yarnpkg/berry/issues/4217
  - https://github.com/remix-run/remix/issues/683
## backend
- other
  - relation model examples
  - onupdate timestamps
  - pip install or pip wheel
    - why pip wheel --no-deps ?
  - prod None to docs and openapi
  - add backend cors
  - form-multipart test
  - gunicorn logging disable
  - black, mypy, other linters etc
    - wemake-python-styleguide
  - --proxy-headers https://fastapi.tiangolo.com/deployment/docker/#behind-a-tls-termination-proxy
    - other nginx configurations from uvicorn docs
      - better nginx location managment (global fastapi location)
  - poetry ? https://fastapi.tiangolo.com/deployment/docker/#docker-image-with-poetry
- arch related
  - https://docs.sqlalchemy.org/en/20/changelog/migration_20.html#migration-20-step-six
  - errors
    - rewrite status codes to status consts
    - errors to schema
    - auto HTTPErrors (like IResponse) (maybe with cats)
  - return status code and data in return???
    - + protocol agnostic
    - + custom response codes
    - - overhead
  - remake structure to more convinient usage
    - make schema autogeneration from models
    - remove fields when inherit schemas
- libs related
  - passlib[bcrypt] to passlib[argon2] ?
  - padantic 2 when released
    - https://docs.pydantic.dev/dev-v2/migration/
    - dotenv settings parsing
  - loguru -> default logging? (or https://github.com/hynek/structlog)
  - pendulium
  - apscheduler 4
  - https://github.com/faust-streaming/faust
## devops
- prepare for files
  - nginx serve static files
  - max filesize deps for FastAPI
  - nginx client_max_body_size 100M;
- rename docker-compose to compose
- docker secrets
- Remove dockerignore ?
- Add restart to docker composes ?
- Sync prod and usual docker composes (and make different image names (or tags) if needed)
  - fix debug compose
- GUID in env or another workaround for correct file rights (container user not root) (migrations for example)
- https://florian-kromer.medium.com/fastapi-microservice-patterns-3052c1241019
## other
- ./backend#on-ubuntu
  - add bedian (asdf or pyenv)
  - fnm
- Add CI/CD
  - github or gitlab ?
- nginx to traefik ?
  - https is easier in traefik
- https://stribny.name/blog/fastapi-production/

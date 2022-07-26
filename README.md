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
## frontend
- add dayjs
- add reactquery boilerplate
- yarn v3 react-app https://github.com/remix-run/remix/issues/683
- Eject react-app (for absolute paths with @ and...?)
- Decide about ts usage (or make js loyal ts env)
- Decide about test usage
- Add default node packages (like react query)
- react-query or react-query from react-router stack
- https://fastapi.tiangolo.com/advanced/generate-clients/
## backend
- add backend cors
- fix no connection to postgres at first startup (restart on failure)
- Python app or src
- pendulium?
- celery vs apscheduler
- form-multipart test
- gunicorn logging disable
- pin versions
  - SQLAlchemy = "1.4.35" to fix relations
    - Relationship(sa_relationship_kwargs={"lazy": "selectin"})
- check and use fastapi addons
  - https://github.com/awtkns/fastapi-crudrouter/issues/122
- black, mype, other linters etc
- --proxy-headers https://fastapi.tiangolo.com/deployment/docker/#behind-a-tls-termination-proxy
- poetry ? https://fastapi.tiangolo.com/deployment/docker/#docker-image-with-poetry
- prod conf --chdir src ?
- auto HTTPErrors (like IResponse) (maybe with cats)
- rewrite status codes to status consts
- prepare for files
  - max filesize deps
  - nginx client_max_body_size 100M;
  - compose.prod     command: sh -c 'alembic upgrade head && gunicorn src.main:app -b 0.0.0.0 -w 4 -k uvicorn.workers.UvicornWorker'
- remake structure to more convinient usage
  - make schema autogeneration from models
  - remove fields when inherit schemas 
## devops
- Remove dockerignore?
- Add restart to docker composes
- Sync prod and usual docker composes (and make different image names if needed)
- fix prod compose (files doesn't work)
- Make and test debug docker file
- GUID for file rights (container user not root)
- https://florian-kromer.medium.com/fastapi-microservice-patterns-3052c1241019
## other
- Add CI/CD
- Deal with nginx config
- nginx to traefik ?
- nginx client_max_body_size 100M;
- https
- https://stribny.name/blog/fastapi-production/
- serve local files nginx

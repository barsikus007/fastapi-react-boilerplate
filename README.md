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
#### yarn v3 react-app
#### Eject react-app (for absulute paths with @ and...?)
#### Decide about ts usage (or make js loyal ts env)
#### Decide about test usage
#### Add default node packages (like react query)
#### Deal with nginx config
#### Add CI/CD
#### Python app or src
#### Remove dockerignore?
#### Add env file settings
#### Add restart to docker composes
#### Sync prod and usual docker composes (and make different image names if needed)
#### Make and test debug docker file
#### Relationship(sa_relationship_kwargs={"lazy": "selectin"})
#### celery vs apscheduler
#### form-multipart test
#### pin versions
#### black, mype, other linters etc
#### poetry ?
#### prod conf --chdir src ?

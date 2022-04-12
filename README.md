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
[Check setup guide](https://docs.docker.com/engine/install/)

[Also install compose](https://docs.docker.com/compose/cli-command/#install-on-linux)
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

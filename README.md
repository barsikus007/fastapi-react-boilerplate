
# Installation
## Install docker
#### On Windows
##### Windows 11 or with winget installed
```pwsh
winget install Docker.DockerDesktop -h
wsl --install -d Ubuntu
```
##### Below Windows 11
[Installer](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)

#### On Linux
[Check setup guide](https://docs.docker.com/engine/install/)
[Also install compose](https://docs.docker.com/compose/cli-command/#install-on-linux)
## Launch app in development mode
```bash
docker compose up -d --build
```

## Launch app in production mode
```bash
docker compose -f "docker-compose.prod.yml" up -d --build
```

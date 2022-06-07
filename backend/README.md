# For local type checking and suggestion (developer mode)
## Install python
#### On Windows
I recommend [scoop](https://scoop.sh) package manager
```pwsh
scoop install python
```
#### On Linux
You already have python, just be sure that you have 3.10 version with venv installed

If your version is lower, then find the way to install it on your distro

Here is the most common distro installation instruction:
##### On Ubuntu
```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install python3.10-dev python3.10-venv -y
```
## Install packages
Be sure that you in backend dir
#### On Windows
```pwsh
py -m venv venv
venv\Scripts\pip install --upgrade pip
venv\Scripts\pip install -r requirements.txt
```
#### On Linux
```bash
python3.10 -m venv venv
venv/bin/pip install --upgrade pip wheel
venv/bin/pip install -r requirements.txt
```
## Point your IDE to virtual environment
¯\\\_( ͡° ͜ʖ ͡°)_/¯
## Launch
Copy `.env.example` to `.env` and change settings
## Other
#### docker pg_dump
https://stackoverflow.com/a/29913462
```bash
docker exec -t your-db-container pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql

cat dump_%d-%m-%Y_%H_%M_%S.sql | docker exec -i your-db-container psql -U postgres
```
#### alembic cheatsheet
```bash
alembic revision --autogenerate -m "Migration name"
alembic upgrade head
alembic downgrade -1
alembic downgrade base
```
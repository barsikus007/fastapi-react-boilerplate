# For local type checking and suggestion (developer mode)
## Install python
#### On Windows
I recommend [scoop](scoop.sh) package manager
```pwsh
scoop install python
```
#### On Linux
You already have python, just be sure that you have 3.10 version with venv installed
If your version is lower then find the way to install it on your disto
Here is most common distro installation instruction:
##### On Ubuntu
```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install python3.10-venv -y
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
venv/bin/pip install --upgrade pip
venv/bin/pip install -r requirements.txt
```
## Point your IDE to virtual environment
¯\\\_( ͡° ͜ʖ ͡°)_/¯
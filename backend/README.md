# For local type checking and suggestion (developer mode)
## Install python
#### On Windows
I recommend [scoop](scoop.sh) package manager
```pwsh
scoop install python
```
#### On Linux
You already have python, just be sure that you have 3.10 version installed
## Install packages
Be sure that you in backend dir
#### On Windows
```pwsh
py -m venv venv
venv\Scripts\pip install -r requirements.txt
```
#### On Linux
```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```
## Point your IDE to virtual environment
¯\\\_( ͡° ͜ʖ ͡°)_/¯
# For local type checking and suggestion (developer mode)
## Install node
#### On Windows
I recommend [scoop](scoop.sh) package manager
```pwsh
scoop install nodejs-lts
node -v
# be sure that it starts from 16
corepack enable
```
#### On Linux
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
# or
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
# then reload your terminal
nvm install 16
node -v
# be sure that it starts from 16
corepack enable
```
## Install packages
Be sure that you in frontend dir
```bash
yarn
```
## Config linters and etc
¯\\\_( ͡° ͜ʖ ͡°)_/¯

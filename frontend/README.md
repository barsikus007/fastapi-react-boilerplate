# For local type checking and suggestion (developer mode)
## Install node
###### Note, that on windows you must use WSL if you are frontend developer due to react-scripts@5.0.0 bug with hot reloading
#### On Windows
###### If you are using WSL you must to preceed linux instructions
I recommend [scoop](scoop.sh) package manager
```pwsh
scoop install nvm
# then reload your terminal
nvm install 16
nvm use 16.15.0  # version may differ
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

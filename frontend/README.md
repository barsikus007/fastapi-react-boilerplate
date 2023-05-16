# For local type checking and suggestion (developer mode)
## Install node
#### On Windows
###### If you are using WSL you must to preceed linux instructions
I recommend [scoop](scoop.sh) package manager
```pwsh
scoop install nvm
# then reload your terminal
nvm install 18
nvm use 18.16.0  # version may differ
node -v
# be sure that it starts from 18
corepack enable
```
#### On Linux
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
# or
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
# then reload your terminal
nvm install 18
node -v
# be sure that it starts from 18
corepack enable
```
## Install packages
Be sure that you in frontend dir
```bash
pnpm i
```
## Config linters and etc
### VSCode
Install [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) and [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) extensions
### Other editors
¯\\\_( ͡° ͜ʖ ͡°)_/¯
## This template was created by
```bash
pnpm create vite frontend --template react-swc-ts
```

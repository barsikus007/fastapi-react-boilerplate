# Frontend

## For local type checking and suggestion (developer mode)

### Install node

#### On Windows

I recommend to use WSL filesystem instead of Windows one (Linux instruction)

I recommend [scoop](scoop.sh) package manager (but proto isn't available in scoop right now)

```pwsh
# install https://moonrepo.dev/proto
irm https://moonrepo.dev/install/proto.ps1 | iex
proto install node lts
# not available for windows, use scoop versions bucket instead
# proto install bun
```

#### On Linux

```sh
# install https://moonrepo.dev/proto
curl -fsSL https://moonrepo.dev/install/proto.sh | bash
proto install node lts
proto install bun
```

### Install packages

Be sure that you in current (frontend) dir

```bash
bun i
```

### Config linters and etc

#### VSCode

Install recommended extensions

#### Other editors

¯\\\_( ͡° ͜ʖ ͡°)_/¯

## This template was created by

```bash
bun create vite frontend --template react-swc-ts
```

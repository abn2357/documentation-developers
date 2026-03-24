---
title: Install TronBox
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## TronBox Environment Dependencies

* NodeJS >=8
* Windows, Linux or Mac OS X
* Docker Engine >=v17

## Install Node.js

### Linux and macOS

Node Package Manager (npm) recommends installing Node.js with [Node Version Manager (nvm)](https://node.dev/post/installing-node-js-tutorial-using-nvm-on-mac-os-x-and-ubuntu) to avoid permission errors when installing globally.

1. Use `curl` or `wget` to install `nvm`:

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
 
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```

2. Make sure nvm is properly installed. You may need to reload the terminal for the command to take effect.

```shell
nvm --version
```

3. Use nvm to install a compatible version of Node.js. For example, to install Node.js v12, run

```shell
nvm install 12
```

4. Run `node --version` to confirm that Node.js has been properly installed.

### Windows

TronBox recommends using the installer from the website of Node.js.

Make sure that you agree to automatically install the necessary tools during installation so that the required Visual Studio build tools, Python, and Chocolately package manager can be installed.

![612](https://files.readme.io/c6b30cf-windows-nodejs.png "windows-nodejs.png")

## Install TronBox

You can install TronBox by executing the following command:

```shell
npm install -g tronbox
```

You may receive warnings during installation. Type tronbox version on the terminal to check whether TronBox has been properly installed.

```shell
tronbox version
```

## For Windows users

If you are running TronBox on Windows, you may encounter naming conflicts that may prevent TronBox from executing properly. In this case, please see [Resolve Naming Conflicts](https://developers.tron.network/reference/tronbox-configuration#resolve-naming-conflicts-on-windows) for any helpful information.

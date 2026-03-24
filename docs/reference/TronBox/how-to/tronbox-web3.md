---
title: tronbox-web3
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
# tronbox-web3

tronbox-web3 is a TronBox plugin for integration with Truffle projects. Using the tronbox-web3 plugin will allow you to use TronBox in projects written for Truffle.

# Required plugins

Before using this plugin, you need to [Install TronBox](https://developers.tron.network/reference/install).

# Installation

To install, execute the following command in your project directory:

```shell
npm install tronbox-web3
```

Then, to your `.js` file in your `test` directory, add the following:

```javascript
const [web3, provider] = require('tronbox-web3')(new Web3(Web3.givenProvider), ganache.provider());
```

# Usage

1. Execute `tronbox init` in your Truffle project. This command will generate a configuration file `tronbox-config.js` in the root directory. This file is used to configure network information and other project-related settings.

```note::
  If there is no package.json file in your project, execute `npm init -y` first
```

2. Now, in your Truffle project, you can use TronBox commands such as `tronbox compile`, etc.

```note::
  Due to the differences between TRON and Ethereum, compatibility errors may occur during execution using TronBox, which needs to be resolved manually according to the error message.
```

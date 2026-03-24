---
title: Work with EVM
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
# Use EVM-compatible chains

Starting from 4.0.0 version, Tronbox supports deploying contracts on EVM-compatible blockchains.

## Configuration file

The configuration file for EVM related configurations is named `tronbox-evm-config.js` and is located in the root directory of the project directory. The file content is as follows:

```javascript
module.exports = {
  networks: {
    bttc: {
      privateKey: 'your private key',
      fullHost: 'https://rpc.bt.io',
      gas: 8500000, // Gas sent with each transaction
      gasPrice: '500000000000000', // 500,000 gwei (in wei)
      network_id: '1'
    },
    development: {
      privateKey: 'your private key',
      fullHost: 'http://127.0.0.1:8545',
      network_id: '*'
    }
  },
  compilers: {
    solc: {
      version: '0.8.7',
      settings: {
        optimizer: {
          enabled: true,
          runs: 200
        },
        evmVersion: 'istanbul'
      }
    }
  }
};
```

## Compile the contract

In order to deploy to an EVM-compatible blockchain, you need to use an EVM version of the compiler to compile the contract. Please run the following command:

```shell
tronbox compile --evm
```

After adding the `--evm` parameter to the compilation command, the `solc` version configured in the `tronbox-evm-config.js` file will be used for compilation.

## Deploy the contract

Deploy to an EVM-compatible blockchain, such as the BTTC network. Please configure in the configuration file and run the following command:

```shell
tronbox migrate --network bttc --evm
```

After adding the `--evm` parameter to the deployment contract command, the `network` version configured in the `tronbox-evm-config.js` file will be used for deployment.\
For details of the deployment script, pleaase see [Contract Deployment(Migration)](../reference/contract-deploymentmigrations) .

## Test contract

To run the test on an EVM-compatible blockchain, please run the following command:

```shell
tronbox test --evm
```

After adding the `--evm` parameter to the test contract command, the `network` version configured in the `tronbox-evm-config.js` file will be used for testing. For more information about the test script, please see [Testing Your Contracts](../reference/test-your-contracts) .

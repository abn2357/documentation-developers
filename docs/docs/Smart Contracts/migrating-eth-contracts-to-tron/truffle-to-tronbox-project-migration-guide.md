---
title: Truffle to TronBox Project Migration Guide
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Introduction

TronBox is a Truffle-based smart contract development tool for TRON, providing capabilities such as contract compilation, deployment, and testing.\
This guide details how to migrate Ethereum Truffle projects to TronBox to achieve TRON network compatibility.

# Environment Setup

## TronBox Installation

```
npm install -g tronbox
```

## TronBox Project Initialization

```
tronbox init
```

# Configuration Migration

## Configuration File Renaming and Modification

Rename `truffle-config.js` to `tronbox-config.js` and update the network configuration file according to TronBox specifications:

```
/**
* TronBox Network Configuration Example  
*/  
  module.exports = {  
   networks: {  
     development: {  
       privateKey: process.env.PRIVATE_KEY, // Recommended: Store private keys using environment variables  
       userFeePercentage: 100,  
       feeLimit: 1e8,  
       fullHost: "<http://127.0.0.1:9090">,  
       network_id: "9"  
     },  
     shasta: {  
       privateKey: process.env.PRIVATE_KEY,  
       userFeePercentage: 50,  
       feeLimit: 1e8,  
       fullHost: "<https://api.shasta.trongrid.io">,  
       network_id: "2"  
     },  
     mainnet: {  
       privateKey: process.env.PRIVATE_KEY,  
       userFeePercentage: 50,  
       feeLimit: 1e8,  
       fullHost: "<https://api.trongrid.io">,  
       network_id: "1"  
     }  
   },  
   compilers: {  
     solc: {  
       version: '0.8.6'  
     }  
   }  
  }
```

### Boundary conditions and error handling:

* We recommended using environment variables for private keys to prevent exposure.
* Consider increasing `feeLimit`, since an insufficient `feeLimit` value may cause deployment failures.
* The `fullHost` address should match the target network.

## Command Comparison: Truffle vs TronBox

| Function | Truffle           | TronBox           |
| :------- | :---------------- | :---------------- |
| Init     | `truffle init`    | `tronbox init`    |
| Compile  | `truffle compile` | `tronbox compile` |
| Deploy   | `truffle migrate` | `tronbox migrate` |
| Test     | `truffle test`    | `tronbox test`    |
| Unbox    | `truffle unbox`   | `tronbox unbox`   |
| Console  | `truffle console` | `tronbox console` |

# Contract and Script Adaptation

## Address and Unit Adaptation

* Ethereum addresses are prefixed with `0x`, while TRON addresses are prefixed with `41` (`Base58` format).
* Ethereum uses the units **wei** and **ether**, where 1 ether (ETH) = 10^18 wei; TRON uses the units **sun** and **TRX**, where 1 TRX = 1,000,000 sun.

## Contract Invocation and Energy

In TronBox, the `feeLimit` parameter serves a function similar to the `gas` parameter in `truffle-config.js`, which defines the upper limit for Energy and Bandwidth resources that a single transaction can consume on the TRON network.

## JavaScript Script Adaptation

Replace web3.js with TronWeb.

# Migration Procedure

## TronBox Project Initialization

Create an empty folder and execute the following script within it to create an empty TronBox project.

```
tronbox init
```

## Copying Contracts and Migration Scripts

* Copy the contract files from the Truffle project’s `contracts` directory to the TronBox project’s `contracts` directory.
* Copy the deployment scripts from the Truffle project’s `migrations` directory to the TronBox project’s `migrations` directory.
* Copy the test files from the Truffle project’s `test` directory to the TronBox project’s `test` directory.

## Configuration File Modification

Modify the network and solc version information within `tronbox-config.js`.

## Dependency and Test Script Adaptation

* In TronBox projects, we recommend using TronWeb instead of web3.js as the blockchain interaction library.
* While most test scripts are reusable as-is, they will require adaptations when elements such as addresses and units are involved.

## Command Substitution

Execute the migrated TronBox workflow:

```
tronbox compile  
tronbox migrate  
tronbox test
```

## Common Issues and Resolutions

* **Deployment Failure**: Verify that the feeLimit is adequate, the TRX balance is sufficient, and the network configuration is correct before deployment.
* **Event Listener Differences**: TRON event listeners require the use of TronWeb's specific methods.

## Best Practices

* Use `.env` files to manage sensitive information, such as private keys.
* Thoroughly test locally or on the Nile testnet before deploying to Mainnet.
* Periodically update TronBox and its dependency libraries, and stay updated on official news.

# References

* TronBox Official Documentation: [https://developers.tron.network/reference/tronbox-quickstart](https://developers.tron.network/reference/tronbox-quickstart)
* TronWeb API Documentation: [https://tronweb.network/docu/docs/intro](https://tronweb.network/docu/docs/intro)

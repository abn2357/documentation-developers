---
title: TronBox Configuration
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
## Configuration file location

Your configuration file `tronbox.js` is located at the root of your project directory.  It is a Javascript file that can execute any code necessary to create your configuration.  It must export an object that represents the project configuration, as shown below:

```javascript
module.exports = {
  networks: {
    development: {
      privateKey: 'your private key',
      userFeePercentage: 100, // The percentage of resource consumption ratio.
      feeLimit: 100000000, // The TRX consumption limit for the deployment and trigger, unit is SUN
      fullNode: 'https://api.nileex.io',
      solidityNode: 'https://api.nileex.io',
      eventServer: 'https://event.nileex.io',
      network_id: '*'
    }，
    compilers: {
      solc: {
        version: '0.8.0'
      }
    }
  },
   // solc compiler optimize
  solc: {
    optimizer: {
      enabled: true,
      runs: 200
    },
    evmVersion: 'istanbul'
  }
};
```

Network configuration is included by default, which runs on  `127.0.0.1:9090`.  Other configuration options are explained below.

### Resolve naming conflicts on Windows

When you use the Command Prompt on Windows, the default configuration file name may cause a conflict with the `tronbox` executable. In this case, you may not be able to run TronBox commands properly on existing projects.

This is because of the way command precedence works on the Command Prompt.  The `tronbox.cmd` executable is on the path as part of the npm package, while the `tronbox.js` configuration file is located in the actual directory where the tronbox command runs.  As `.js` is an acceptable executable extension by default, `tronbox.js` takes precedence over `tronbox.cmd`, leading to unexpected results.

This issue can be solved by any of the following solutions:

* Call the executable file explicitly using the `.cmd` extension (`tronbox.cmd compile`).
* Edit the system `PATHEXT` environment variable and remove `.JS`; from the list of executable extensions.
* Rename `tronbox.js `to something else (`tronbox-config.js`).
* Use [Windows PowerShell](https://learn.microsoft.com/en-us/powershell/) or [Git BASH](https://gitforwindows.org/), or shells that do not cause conflicts.

## General configuration options

### Networks

Specify the networks for deployment and the specific transaction parameters (e.g., feelimit, account address, etc.) that will be used when interacting with each network.  Contract artifacts will be saved and recorded for later use when compilation and deployment take place on a specified network.When the contract abstractions detect that we are connected to a specified network, they will use the contract artifacts associated with the aforementioned network to simplify application deployment.

As shown below, the `networks` object is keyed by network names, and each name contains an object that defines the parameters of the corresponding network. You can provide your own network name and configuration to tell TronBox what network to connect to for deployment and testing.

Once you have defined your network, you can provide the name as an option for some commands; this is possible during testing or running migrations. You may specify a network name as follows during the migration:

```
$ tronbox migrate --network nile
```

For example:

```javascript
networks: {
  shasta: {
    privateKey: process.env.PRIVATE_KEY,
    userFeePercentage: 50,
    feeLimit: 1000 * 1e6,
    fullHost: 'https://api.shasta.trongrid.io',
    network_id: '2',
  },
  nile: {
    privateKey: process.env.PRIVATE_KEY,
    userFeePercentage: 100,
    feeLimit: 1000 * 1e6,
    fullHost: 'https://api.nileex.io',
    network_id: '3',
  },
}
```

If transaction options are not specified, the following values will be used for parameters by default, regardless of the network:

* `feeLimit`: feeLimit refers to the upper limit of the Energy cost for deploying or calling a smart contract.  Default value is `1000000000` (1,000 TRX).
* `userFeePercentage`: userFeePercentage refers to the ratio of Energy consumed by the user to Energy consumed by the developer for smart contract execution. Default value is `100`.
* `originEnergyLimit`: originEnergyLimit refers to the maximum amount of Energy consumed by the creator in creating or executing a contract. Default value is `10000000` (10\_000\_000 ENERGY).
* `callValue`: callValue refers to the value of TRX sent to the contract address when deploying a contract. Default value is `0`.
* `tokenId`: tokenId refers to the ID of the TRC10 token sent to a contract address for contract deployment. Default value is `0`.
* `tokenValue`: tokenValue refers to the amount of the TRC10 token sent to a contract address for contract deployment. Default value is `0`.

#### Using mnemonics

If you prefer to use a mnemonic instead of a private key, you can do so in the configuration of `networks`, for example:

```javascript
networks: {
   shasta: {
     // privateKey: process.env.PRIVATE_KEY,
     mnemonic: process.env.MNEMONIC,
     userFeePercentage: 50,
     feeLimit: 1000 * 1e6,
     fullHost: '<https://api.shasta.trongrid.io>',
     network_id: '2',
   },
   …
}
```

Then, add the MNEMONIC configuration to your `.env` file, e.g:

```javascript
export MNEMONIC="test test test test test test test test test test test test test"
```

```note::
To use mnemonic, you need to upgrade your TronBox to v3.0.2 or above.
```

### Specify a contract directory

The default directory for uncompiled contracts is `./contacts` under the root directory.  You can specify a `contracts_directory` property if you want to keep your contracts in a different directory.\
For example, you can have TronBox find contracts in `./allMyStuff/someStuff/theContractFolder` (recursively) at compile time:

```javascript
module.exports = {
  contracts_directory: './allMyStuff/someStuff/theContractFolder',
  networks: {
    nile: {
      privateKey: process.env.PRIVATE_KEY,
      feeLimit: 1000 * 1e6,
      fullHost: 'https://api.nileex.io',
      network_id: '3'
    }
  }
};
```

### Specify a directory for built contract artifacts

The default output directory for compiled contracts is `./build/contracts` relative to the project root.  You can put them under a different directory by changing the attributes of `contracts_build_directory`.\
For example, you can put the built contract artifacts in `./output/contracts`:

```javascript
module.exports = {
  contracts_build_directory: './output',
  networks: {
    nile: {
      privateKey: process.env.PRIVATE_KEY,
      feeLimit: 1000 * 1e6,
      fullHost: 'https://api.nileex.io',
      network_id: '3'
    }
  }
};
```

The built contract artifacts do not have to be inside the project root:

```javascript
module.exports = {
  contracts_build_directory: '../../../output',
  networks: {
    nile: {
      privateKey: process.env.PRIVATE_KEY,
      feeLimit: 1000 * 1e6,
      fullHost: 'https://api.nileex.io',
      network_id: '3'
    }
  }
};
```

Absolute paths also work. However, we do not recommend using absolute paths as they might not exist when you compile contracts on another system.  If you want to use absolute paths on Windows, please add double backslashes (e.g., `C:\\Users\\Username\\output`).

### Migration directory

The default directory for migrations is `./migrations` under the project root directory.  You can also put them under a different directory by changing `migrations_directory`.\
For example:

```javascript
module.exports = {
  migrations_directory: './allMyStuff/someStuff/theMigrationsFolder',
  networks: {
    nile: {
      privateKey: process.env.PRIVATE_KEY,
      feeLimit: 1000 * 1e6,
      fullHost: 'https://api.nileex.io',
      network_id: '3'
    }
  }
};
```

## Specify compilers

In the `compilers` object, you can specify settings related to the compilers used by TronBox.

### solc

Solidity compiler settings support optimizer settings for `solc`.\
An example of TronBox configuration:

```javascript
module.exports = {
  networks: {
    compilers: {
      solc: {
        version: '0.8.6'
      }
    }
  },
  solc: {
    optimizer: {
      enabled: true,
      runs: 200
    },
    evmVersion: 'istanbul'
  }
};
```

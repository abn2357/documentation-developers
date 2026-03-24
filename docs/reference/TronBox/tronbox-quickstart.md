---
title: TronBox Quickstart
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
This doc will take you through the basics of creating a TronBox project and deploying a smart contract to a blockchain.

> NOTE: Before you begin,  it is advised that you read the [TRON documentation](https://tronprotocol.github.io/documentation-en/getting_started/getting_started_with_javatron/).

## TronBox Installation

Before using `TronBox`, please install it using `npm` command. You can install TronBox by referring to the [installation instructions](https://developers.tron.network/reference/install).

## Create a project

Most of the TronBox commands are run under the directories of TronBox projects. So the first step is to create a TronBox project. You can create a bare project, but for those getting started, you can use TronBox Boxes, which offers example applications and project templates.  We'll use the MetaCoin box, which creates a token that can be transferred between accounts. 

1. Create a directory for MetaCoin:

```shell
mkdir MetaCoin
cd MetaCoin
```

2. Download ("unbox") the MetaCoin project:

```shell
tronbox unbox metacoin
```

> You can create a bare project without smart contracts using `tronbox init`.

Once this operation is completed, you will have a project structure with the following items:

* `contracts/`: [Directory for Solidity contracts](ref:interact-with-a-contract) 
* `migrations/`: [Directory for scriptable deployment files](ref:contract-deploymentmigrations) 
* `test/`: Directory for test files for testing your applications and contracts. For more information, refer to ["How to test contracts?"](ref:test-your-contracts) 
* `tronbox.js`: TronBox [configuration file](ref:tronbox-configuration) 
*

## Explore the project

> This page is just a quickstart, and we're going to get into the details in the following sections.

1. `contracts/MetaCoin.sol`: This is a smart contract (written in Solidity) that creates a MetaCoin token. Note that this also references another Solidity file contracts/ConvertLib.sol in the same directory.
2. `contracts/Migrations.sol`: This is a separate Solidity file used to manage and upgrade smart contracts. It is needed in every project and usually does not need to be edited.
3. `migrations/1_initial_migration.js`: This is the script used to deploy the Migrations contract, and is stored within the Migrations.sol file.
4. `migrations/2_deploy_contracts.js`: This is a deployment script that is used to deploy the MetaCoin contract.  (Deployment scripts run in sequence. Scripts titled with 2 normally run after those titled 1.)
5. `test/metacoin.js`:  This is a [testing script written in JavaScript ](ref:test-your-contracts) that ensures your contract is working as expected.
6. `tronbox.js`: This is the TronBox [configuration file](ref:tronbox-configuration) , for setting network information and other project-related settings. The file can be left blank because we can use a TronBox command that has some defaults built in.

## Compile

1. Compile a smart contract:

```shell
tronbox compile
```

We will see the following output:

```shell
Compiling .\contracts\ConvertLib.sol...
Compiling .\contracts\MetaCoin.sol...
Compiling .\contracts\Migrations.sol...
 
Writing artifacts to .\build\contracts
```

## Deploy with TronBox Runtime Environment (TRE)

To deploy our smart contracts, we're going to need to connect to a blockchain. TronBox has a built-in TRE private chain that can be used for testing. Please note that this blockchain is local to your system and does not interact with the main TRON network.\
You can start this blockchain and interact with it using TronBox Runtime Environment. This step is to create a complete personal chain for development on TRON.

Pull images from the docker:

```shell
docker pull tronbox/tre
```

> For how to install docker, please refer to [docker installation documentation](https://docs.docker.com/desktop/install/mac-install/)

### 1. Start the TronBox Runtime Environment and run the following commands:

```shell
docker run -it \
-p 9090:9090 \
--rm \
--name tron \
tronbox/tre
```

We will see the following information:

```shell
TronBox Runtime Environment v1.0.1
 
 
Start the http proxy for dApps...
[HPM] Proxy created: /  ->  http://127.0.0.1:18190
[HPM] Proxy created: /  ->  http://127.0.0.1:18191
[HPM] Proxy created: /  ->  http://127.0.0.1:8545
[HPM] Proxy created: /  ->  http://127.0.0.1:8545
[HPM] Proxy created: /  ->  http://127.0.0.1:8060
 
Tron Quickstart listening on http://127.0.0.1:9090
 
 
ADMIN /admin/accounts-generation
 
FullNode is already.
 
 
Available Accounts
==================
 
(0) THD652niU9nm81xA8Gf2ctSQLDhiWUXT4o (10000 TRX)
(1) TSPjSVn1Ew1QaWMLyYSGiV78qaXbocuFkB (10000 TRX)
(2) TUcEcuj3FDSmsfaSWBH5CTu4k4sHEsStjo (10000 TRX)
(3) TVzQGMmmXBJC12o4yzBkr4dw6VWqPnR9CA (10000 TRX)
(4) TAZC9fKYnjtVFuHnaUzQ5xLSLe5MYovTYn (10000 TRX)
(5) TDi5qjuk8cs6FMG754FZUDxcLqTpVBUhPF (10000 TRX)
(6) TCwGkXWD2C8gi7UChVGnqipmfm8Hq4YYo9 (10000 TRX)
(7) TM3WZw9PWBMUTmFvXV7qxt6dq5Bv2znL7p (10000 TRX)
(8) TVyL1uiusn6r3UPGaosPBu1FTvQnWADNbP (10000 TRX)
(9) TMbXpcWsTXnXEHkqJkSmU1Gj21CCYLVMsv (10000 TRX)
 
Private Keys
==================
 
(0) 6b7b075714de08b1fcc2dc5afe20f5e087fb679032b601717d0cd3807e24d563
(1) 5adab5cdfafab07714895f8a0f9ccf50b3a786902bf21a31f5749f5f3a36a5ee
(2) c2f12cbc82befc3ba3da66fcfadac830e9a6e28fcbb8178bd6fdefaabe15d5fd
(3) 0b44950cb02dfc2e7bdc0803139cf767eff95af03568418f5e7fac0c25e9beeb
(4) ffd86aec3b4a5c2b2bb0df3078eebe97be75115a9affc788b427dcaad9084f10
(5) 367b6da347e91d1d1e02ec775028ffb310d2e37e4fc56001d3a1d96b33142890
(6) 9940da6d6516473373fa92c7731785dd545fac8638ee1b504da27befd2dec722
(7) d9ed135abc58e1ad081a8df755b76a0c6d6bab137021146d38a9bb7674aec345
(8) ba09da49973cd129d114d3b18559b701f68fedd9bdeb6859ba60c58b34c5a860
(9) ebe05e5b6335ce84f37fdc143164dd768a7204718c12f7786e8f44ce1b32412d
 
HD Wallet
==================
Mnemonic:      buyer assume spin morning mosquito fortune enhance vocal raven tired wise fun
Base HD Path:  m/44'/195'/0'/0/{account_index}
 
GET 200  - 32850.036 ms
```

This shows ten accounts (and their private keys) that can be used when interacting with the blockchain.

> This docker image is not optimized for the Apple ARM chip (Apple silicon), so it may be unusable and the docker needs to be restarted several times.

### 2. Open the console and execute the deployment:

```shell
tronbox migrate
```

We will see the following output:

```shell
Using network 'development'.
 
Running migration: 1_initial_migration.js
Replacing Migrations...
Migrations:
    (base58) TBp7j3cUisov1tWbq1vagxwXmNBcmmjLzw
    (hex) 4114381a89161cd01957dc854a69c000f019d3a4cb
Saving successful migration to network...
Saving artifacts...
Running migration: 2_deploy_contracts.js
Replacing ConvertLib...
ConvertLib:
    (base58) TGoVTVUt5KBtLqMd8m4kdhMgivUc83mig1
    (hex) 414af27519fbc1e8ffe911761ab106fff563200830
Linking ConvertLib to MetaCoin
Replacing MetaCoin...
MetaCoin:
    (base58) TQCcNUFpK8zLskJvryWE82ZEGXBqSHA2Sy
    (hex) 419c1aad134258c42af129822814098333ba251e52
Saving successful migration to network...
Saving artifacts...
```

This shows the network, addresses of your deployed contracts, and transaction statuses.

> NOTE: Your transaction hashes and contract addresses will be different from the above.

## Test

1.Open the console terminal and run the Solidity test instance

```shell
tronbox test ./test/metacoin.js
```

2.After hitting the return key, you will see the following output:

```shell
    Contract: MetaCoin
    ✓ should verify that there are at least three available accounts
    ✓ should verify that the contract has been deployed by accounts[0] (64ms)
    ✓ should put 10000 MetaCoin in the first account (116ms)
  Sleeping for 1 second... Slept.
    ✓ should call a function that depends on a linked library (1116ms)
    ✓ should send coins from account 0 to 3 and verify that a Transfer event has been emitted (1066ms)
  Sleeping for 3 seconds... Slept.
    ✓ should send coins from account 0 to 1 (1277ms)

  6 passing (8s)
```

> If you’re on Windows and encountering problems running this command, please see the documentation on [Solving naming conflicts on Windows](https://developers.tron.network/reference/tronbox-configuration#resolve-naming-conflicts-on-windows).

## Interact with the contract

To interact with the contract, you can use the `tronbox console`.

```shell
tronbox console
```

You will see the following prompt:

```shell
tronbox(development)>
```

> The name in the parentheses of the prompt `tronbox(development)>` is the network that is currently connected to.

For example:

* Check the account balance:

```
tronbox(development)> tronWeb.trx.getAccount()

//outputs:
//{
//  account_name: '5a696f6e',
//  address: '41928c9af0651632157ef27a2cf17ca72c575a4d21',
//  balance: 94999899999000000,
//  latest_opration_time: 1667357772000,
//  allowance: 140480000000,
//  is_witness: true,
//  account_resource: {}
//}
```

* Obtain the list of accounts:

```
tronbox(development)> tronWeb._accounts
 
//output:
//[
//  'TPt8VDCU5c5PWsZ8KDTsq9YwQRoSFpN1KX',
//  'TPQbBa5TvHCjoJX3EWBtQ44Laq929wCuxb',
//  'TC5SR8sVePhmPvdusQoks3gaTv7aM523Rp',
//  'TWDvZhLq4cXPF4p9UsyJC3XVLqVGUVwxuj',
//  'TKrtFy3GYGZeoyT8wwbbpap3vuSXSKUq1w',
//  'TLKrFZtDNBcp9wAGnCfkY7nKoMdpeGvtkX',
//  'TKG9BwY5vySYoq6Wmw31c7tXz1q6sjcDC8',
//  'TPSBT6r6kwgMhwrzTYYKsJCrwQkkjQHxBA',
//  'TKu86RPU6Kr88kx6LNxofidA3HRKX5tUEj',
//  'TLpJz5qNiWh2VSkR1ynmVDL3nCFQ8J7euY'
//]
```

* Call the contract to check the account balance:

```shell
tronbox(development)> MetaCoin.deployed().then(res => res.getBalance(tronWeb._accounts[0]))

//outputs:
//BigNumber { _hex: '0x2710', _isBigNumber: true }
```

* Transfer some metacoin to other accounts:

```shell
tronbox(development)> MetaCoin.deployed().then(res => res.sendCoin(tronWeb._accounts[1],500))

//outputs:
//'3b6a2cb56841f5cd39b4e081c33465909204b36794fcd494c0374eb5d3d3fb9d'
```

* Check the balance of the account that received the metacoin:

```
tronbox(development)> MetaCoin.deployed().then(res => res.getBalance(tronWeb._accounts[1]))

//outputs:
//BigNumber { _hex: '0x01f4', _isBigNumber: true }
```

* Check the balance of the account that sent the metacoin:

```shell
tronbox(development)> MetaCoin.deployed().then(res => res.getBalance(tronWeb._accounts[0]))

//outputs:
//BigNumber { _hex: '0x251c', _isBigNumber: true }
```

# Continue learning

This quickstart showed you the basics of the TronBox project lifecycle, but there is much more to learn. Please continue with the rest of our documentation.

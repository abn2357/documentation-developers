---
title: Test Your Contracts
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
## Framework

TronBox comes standard with an automated testing framework to make testing your contracts a breeze. This framework lets you write simple and manageable tests:

* In  [Javascript](https://developers.tron.network/reference/javascript-test-cases), for exercising your contracts from the outside world, just like your application.

## Location

All test files should be located in the `./test`  directory. TronBox will only run test files with the following file extensions: `.js`. All other files are ignored.

## Command

To run all tests, simply run:

```
tronbox test
```

Alternatively, you can specify a path to a specific file you want to run, e.g.,

```
tronbox test ./path/to/test/file.js
```

## Using TronBox Runtime Environment (TRE)

To test our contracts more easily, we need to connect to a blockchain network. After V3.0.0 came out, TronBox has a built-in TRE private chain that can be used for testing. Please note that this blockchain is in our local system and does not connect to the TRON main network.

You can start and interact with the blockchain by using the TronBox Runtime Environment, which is designed to build a complete private chain for development on TRON.

Steps are as follows:

Pull images from the docker:

```
docker pull tronbox/tre
```

### 1. Start the TronBox Runtime Environment and run the following commands:

```
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

Here we see ten accounts (and their private keys) that can be used to interact with the blockchain.

>  This docker image is not optimized for the Apple ARM chip (Apple silicon), so it may be unusable and the docker needs to be restarted several times.

### 2. Open the console and execute the deployment:

```
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

Here shows the network, addresses of your deployed contracts, and transactions statuses.

After starting TRE, you can use the following advanced features in unit testing.

> NOTE: You can use tronWrap to replace tronweb in unit testing.

* `tre_setAccountBalance`: to set account balance

```
const address = 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL';
const balance = '0x3e8';
const result = await tronWrap.send('tre_setAccountBalance', [address, balance]);
console.log(result);
```

* `tre_setAccountCode`: to set account code (It's recommended to set it as runtime\_code, because setting it to the creation code of the contract will cause an exception in executing the contract.)

```
const address = 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL';
const data = '0xbaddad42';
const result = await tronWrap.send('tre_setAccountCode', [address, data]);
console.log(result);
```

* `tre_setAccountStorageAt`: to set account storage

```
const address = 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL';
const slot = '0x0000000000000000000000000000000000000000000000000000000000000005';
const data = '0xbaddad42';
const result = await tronWrap.send('tre_setAccountStorageAt', [address, slot, data]);
console.log(result);
```

* `tre_mine`: Immediately mine the specified number of blocks, and the blocks parameter specifies the additionally mined blocks. The parameter range is (0, 100] (if the parameter is not given, the default is 1)

```
const result = await tronWrap.send('tre_mine', [{ blocks: 5 }]);
console.log(result);
```

* `tre_unlockedAccounts`: unlocked account

```
const result = await tronWrap.send('tre_unlockedAccounts', [['TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL']]);
console.log(result);
```

* `tre_blockTime`: to set the auto-mining time. If the parameter is 0, then the auto-mining stops and only one block is mined after receiving a transaction.

```
const result = await tronWrap.send('tre_blockTime', [3]);
console.log(result);
```

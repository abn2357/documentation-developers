---
title: Interact with a Contract
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
## Introduction

If you were writing raw requests to the TRON network yourself in order to interact with your contracts or conduct tests, you'd soon realize that writing these requests is clunky and cumbersome.  As well, you might find that managing the state for each request you've made is *complicated*.  Fortunately, TronBox takes care of this complexity for you to make interacting with your contracts a breeze.

## Read and write data

The TRON network distinguishes between writing data to the network and reading data from it, which plays a significant part in how you write your application.  In general, writing data is called a **transaction** whereas reading data is called a **call**.  Transactions and calls are treated very differently and have the following characteristics.

## Transaction

`Transactions` fundamentally change the state of the network.  A `transaction` can be as simple as sending TRX to another account, or as complicated as executing a contract function or adding a new contract to the network. The defining characteristic of a `transaction` is that it **writes (or changes) data**. `Transactions` cost "energy" to run and take time to process.  When you execute a contract's function via a `transaction`, you cannot receive that function's return value because the transaction isn't processed immediately. In general, functions meant to be executed via a transaction will not return a value, but a transaction id instead.  So in summary, `transactions`:

* Cost Energy and Bandwidth, which can be obtained by freezing TRX
* Change the state of the network
* Aren't processed immediately (need to wait for confirmations by Super Representatives)
* Won't expose a return value (only a transaction id)

## Call

`Calls`, on the other hand, are very different. `Calls` can be used to execute code on the network, though no data (e.g., state variables) will be permanently changed.  The defining characteristic of `calls` is that they read data. When you execute a contract function via a `call`, you will receive the return value immediately. In summary, `calls`:

* Are free (cost no Energy or Bandwidth)
* Do not change the state of the network
* Are executed immediately
* Will expose a return value

Choosing between a `transaction` and a `call` is as simple as deciding whether you want to read data, or write it.

## Introducing contract abstractions

Contract abstractions are the bread and butter of interacting with TRON contracts from Javascript.  In short, contract abstractions are wrapper code that makes interaction with your contracts easy, in a way that lets you forget about the many engines and gears executing under the hood.  TronBox uses its own contract abstraction via the tronbox-contract module, and this contract abstraction is described below.

Here we use the `MetaCoin` contract available to you through TronBox via `tronbox unbox metacoin` to help you appreciate the usefulness of a contract abstraction.

```javascript
pragma solidity >=0.4.25 <0.6.0;
 
import "./ConvertLib.sol";
 
 
 
//This is just a simple example of a coin-like contract. It is not standards-compliant.
//If you want to create a standards-compliant token, see: https://github.com/ConsenSys/Tokens.
 
contract MetaCoin {
    mapping (address => uint) balances;
 
    event Transfer(address indexed _from, address indexed _to, uint256 _value);
 
    constructor() public {
        balances[tx.origin] = 10000;
    }
 
    function sendCoin(address receiver, uint amount) public returns(bool sufficient) {
        if (balances[msg.sender] < amount) return false;
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Transfer(msg.sender, receiver, amount);
        return true;
}
 
    function getBalanceInEth(address addr) public view returns(uint){
        return ConvertLib.convert(getBalance(addr),2);
}
 
    function getBalance(address addr) public view returns(uint) {
        return balances[addr];
}
}
```

This contract has three methods aside from the constructor (`sendCoin`, `getBalanceInEth`, and `getBalance`). All three methods can be executed as either a `transaction` or a `call`.

Now let's look at the Javascript object called MetaCoin provided for us by TronBox, as made available in the TronBox console:

```javascript
tronbox(development) > MetaCoin.deployed().then(instance => console.log(instance));
 
// outputs:
//
// Contract
// - address: "0xa9f441a487754e6b27ba044a5a8eb2eec77f6b92"
// - allEvents: ()
// - getBalance: ()
// - getBalanceInEth: ()
// - sendCoin: ()
// ...
```

> NOTE that the abstraction contains the exact same functions that exist within our contract.  It also contains an address that points to the deployed version of the MetaCoin contract.

## Execute contract functions

With the abstraction, you can easily execute contract functions on the TRON network.

### Make a transaction

There are three functions on the MetaCoin contract that we can execute.  If you analyze each of them, you'll see that `sendCoin` is the only function that aims to make changes to the network. The goal of `sendCoin` is to "send" some Meta coins from one account to another, and these changes should persist.

When calling `sendCoin`, we'll execute it as a `transaction`. In the following example, we'll send 10 Meta coins from one account to another in a way that is making a `transaction`:

```javascript
tronbox(development) > MetaCoin.deployed().then(res => res.sendCoin(tronWeb._accounts[1], 500, { from: tronWeb._accounts[0] }));
```

A few things are interesting about the above code:

* We called the abstraction's `sendCoin` function directly. This will result in a `transaction` by default (i.e, writing data) instead of `call`.
* We passed an object as the third parameter to `sendCoin`. Note that the `sendCoin` function in our Solidity contract doesn't have a third parameter. What you see above is a special object that can always be passed as the last parameter to a function that lets you edit specific details about the transaction. Here, we set the `from` address ensuring this transaction came from `accounts[0]`. The transaction params that you can set:
  * `from`: from refers to the sending party of the transaction.
  * `callValue`: callValue refers to the value of TRX sent to the contract address when deploying a contract. Default value is `0`.
  * `tokenId`: tokenId refers to the ID of the TRC10 token sent to a contract address for contract deployment. Default value is `0`.
  * `tokenValue`: tokenValue refers to the amount of the TRC10 token sent to a contract address for contract deployment. Default value is `0`.
  * `feeLimit`: feeLimit refers to the upper limit of the Energy cost for deploying or calling a smart contract. Default value is `1000000000` (1,000 TRX).

### Make a call

Continuing with MetaCoin, notice the `getBalance` function is a great candidate for reading data from the network.  It doesn't need to make any changes, as it just returns the MetaCoin balance of the address passed to it.  Let's give it a shot:

```javascript
tronbox(development) > MetaCoin.deployed().then(res => res.getBalance(tronWeb._accounts[0]));
```

### Process transaction results

When you make a `transaction`, you're given a `result` object that gives you a wealth of information about the `transaction`.

```javascript
tronbox(development) > MetaCoin.deployed().then(res => res.sendCoin(tronWeb._accounts[1], 500, { from: tronWeb._accounts[0] }));
 
// outputs:
// 475d5006b56685cc40e07b36498f4d4809f2ce4fa9c678c108476dfe4e02c59e
```

Specifically, you get the following via the transaction id:

```javascript
tronbox(development) > tronWeb.trx.getTransactionInfo('475d5006b56685cc40e07b36498f4d4809f2ce4fa9c678c108476dfe4e02c59e');
 
//outputs:
// {
//   id: '475d5006b56685cc40e07b36498f4d4809f2ce4fa9c678c108476dfe4e02c59e',
//   fee: 1253000,
//   blockNumber: 64403,
//   blockTimeStamp: 1667550996000,
//   contractResult: [
//     '0000000000000000000000000000000000000000000000000000000000000001'
//   ],
//   contract_address: '419c1aad134258c42af129822814098333ba251e52',
//   receipt: {
//     energy_fee: 1253000,
//     energy_usage_total: 12530,
//     net_usage: 346,
//     result: 'SUCCESS'
//   },
//   log: [
//     {
//       address: '9c1aad134258c42af129822814098333ba251e52',
//       topics: [Array],
//       data: '000000000000000000000000989be99ce2c707c16b3d390e943b85c76381718600000000000000000000000093668cda1f0dce82c808d7c1134c3e85d7fc71d200000000000000000000000000000000000000000000000000000000000001f4'
//     }
//   ]
// }
```

* `id` (string) - Transaction hash
* `log` (array) - Decoded events (logs)
* `receipt` (object) - Transaction receipt (includes the amount of Energy used)

### Catch events

Your contracts can fire events that you can catch to gain more insight into what your contracts are doing. Solidity uses the LOG command to record event information in the log field TransactionInfo. The structure of an event is shown below by using the gettransactioninfobyid API to fetch TransactionInfo.\
The event is triggered as part of the sendCoin call (Transfer(msg.sender, receiver, amount);).

```javascript
{
    "id": "475d5006b56685cc40e07b36498f4d4809f2ce4fa9c678c108476dfe4e02c59e",
 
    ......
 
    "log": [
    {
      "address": "FEQNQt6AQsPiaFJGhrWbss6MjSXC9Prq2",
      "topics": [
        "ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
      ],
      "data": "000000000000000000000000989be99ce2c707c16b3d390e943b85c76381718600000000000000000000000093668cda1f0dce82c808d7c1134c3e85d7fc71d200000000000000000000000000000000000000000000000000000000000001f4"
    }
  ]
}
 
log: [
    {
      address: '9c1aad134258c42af129822814098333ba251e52',
      topics: [Array],
      data: '000000000000000000000000989be99ce2c707c16b3d390e943b85c76381718600000000000000000000000093668cda1f0dce82c808d7c1134c3e85d7fc71d200000000000000000000000000000000000000000000000000000000000001f4'
    }
  ]
```

### Add a new contract to the network

We can deploy our own version to the network using the .new() function:

```javascript
tronbox(development)> MetaCoin.new('50').then(res => {console.log(res.address)})
 
41449ca55809f15910db70e67f63c875fcc33e04ac
```

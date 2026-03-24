---
title: tronweb.contract
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
### Smart Contract Deployment

For deploying a smart contract, you can not only use the [tronWeb.transactionBuilder.createSmartContract](https://developers.tron.network/reference/createsmartcontract) interface, but also the [tronWeb.contract().new( )](https://developers.tron.network/reference/tronwebcontractnew) interface.

### Smart Contract Invocation

#### Get smart contract instance

Before calling a smart contract, you need to obtain the smart contract instance first. You can create a contract instance in the following way:

```javascript
let abi = [...];       
let instance = await tronWeb.contract(abi,'contractAddress'); 
```

#### Calling smart contract methods

Different types of contract methods need to be invoked by different tronweb apis:

* Use `call` to execute `pure` or `view` smart contract methods, please refer to [method.call()](https://developers.tron.network/reference/methodcall)
* Use `send` to execute `non-pure` or `modify` smart contract methods, please refer to [method.send()](https://developers.tron.network/reference/methodsend) for specific usage instructions.

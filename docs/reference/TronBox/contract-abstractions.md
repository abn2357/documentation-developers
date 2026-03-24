---
title: Contract Abstractions
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
TronBox provides contract abstractions for interacting with your contracts. Skip ahead to the [API](https://developers.tron.network/reference/contract-abstractions#api) section for a list of contract methods.

## Usage

To obtain a contract abstraction, you can use the `require()` method of the `artifacts` object to load a specific contract artifact. Outside of the console, artifacts are also valid in migration files and testing files. You may create contract abstractions as follows:

```javascript
const MyContract = artifacts.require('MyContract');
```

You can also obtain one in the developer console. You need to use the `at`, `deployed`, or `new` method to obtain contract abstractions in the developer console:

```javascript
tronbox(development) > MyContract.deployed().then(myContract => console.log(myContract));
```

You now have access to the following functions on `MyContract`, as well as many others:

* `at()`: Create a contract abstraction instance of `MyContract` that is deployed at a specific address.
* `deployed()`: Create a contract abstraction instance of `MyContract` that represents the default address managed by `MyContract`.
* `new()`: Deploy a new version of this contract to the network, getting a contract abstraction instance of `MyContract` that represents the newly deployed contract.

Each instance is tied to a specific address on the TRON network, and each instance has a 1-to-1 mapping from Javascript functions to contract functions. For example, if your Solidity contract has a function `someFunction(uint value) {}`(solidity), then you can execute that function on the network in the following way:

```javascript
let deployed;
MyContract.deployed()
  .then(instance => {
    deployed = instance;
    return deployed.someFunction(5);
  })
  .then(result => {
    // Do something with the result or continue with more transactions.
  });
```

You can also use async/await syntax. We will use async/await for the rest of this document, but you may also use Promise to interact with contract methods as well.

```javascript
const deployed = await MyContract.deployed();
const result = await deployed.someFunction(5);
// Do something with the result or continue with more transactions.
```

## API

There are two APIs you need to be aware of. One is the static contract abstraction API and the other is the contract instance API. The abstraction API is a set of functions that exist for all contract abstractions and on the abstractions themselves (i.e., `MyContract.at()`). In contrast, the instance API is the API available to contract instances—abstractions that represent a specific contract on the blockchain network—and this API is created dynamically based on functions available in your Solidity source file.

### Contract abstraction API

Each contract abstraction—`MyContract` in the examples above—has the following useful functions:

#### `MyContract.new([arg1, arg2, ...], [tx params])`

This function takes whatever constructor parameters your contract requires and deploys a new instance of the contract to the network. There is an optional last argument that you can use to pass transaction parameters, including feeLimit, userFeePercentage, and callValue. This function returns a Promise object that is a new instance of the newly deployed contract abstraction.

#### `MyContract.at(address)`

This function creates a new instance of the contract abstraction via the passed-in address. It resolves into a contract abstraction instance after ensuring the contract code exists at the specified address.

#### `MyContract.deployed()`

Return the instance of the contract abstraction created by the contract deployment address saved in the project.

#### `MyContract.link(instance)`

Link a library represented by a contract abstraction instance to MyContract. The library must first be deployed and have its deployed address set. The name and deployment address will be inferred from the contract abstraction instance.\
Libraries can be linked multiple times and will overwrite their previous linkage.

> NOTE: This method has two other forms, but this form is recommended.

#### `MyContract.link(name, address)`

Link a library with a specific name and address to MyContract.

#### `MyContract.link(object)`

Link multiple libraries to MyContract via an object. The keys must be strings representing the library names and the values must be strings representing the addresses.

#### `MyContract.setNetwork(network_id)`

Set the network ID that MyContract is using.

#### `MyContract.hasNetwork(network_id)`

Return a boolean that represents whether this contract has been deployed on a specific network or not.

#### `MyContract.defaults([new_defaults])`

Get and optionally set transaction defaults for all instances created from this abstraction. If called without any parameters, it will simply return an object representing current defaults. Passing an object will result in new defaults being set. An example of default transaction values that can be set is:

```javascript
MyContract.defaults({
  feeLimit: ...,
  callValue: ...,
  tokenValue: ...,
  tokenId: ...,
  userFeePercentage: ...,
  originEnergyLimit: ...
})
```

#### `MyContract.clone(network_id)`

Clone a contract abstraction to get another object that uses a different network\_id. This is useful if you would like to manage the same contract but on a different network. When using this function, do not forget to set the correct network.

```javascript
const MyOtherContract = MyContract.clone(3);
```

### Contract instance API

Each contract instance is different based on the source Solidity contract, and the API is created dynamically. For the purposes of this documentation, let's use the Solidity source code below:

```javascript
contract MyContract {
  uint public value;
  event ValueSet(uint val);
  function setValue(uint val) {
    value = val;
    emit ValueSet(value);
  }
  function getValue() constant returns (uint) {
    return value;
  }
}
```

From Javascript's point of view, this contract has three functions: `setValue`, `getValue`, and `value`.  This is because `value` is public and thus automatically creates a function.

### Make a transaction via a contract function

When we call `setValue()`, this creates a transaction. From Javascript:

```javascript
const tx = await instance.setValue(5);
```

### Call contracts

However, we can get the value by calling `getValue()` and using `.call()`. Calls are always free and do not require any TRX, so they are good for calling functions that read data from the blockchain.

```javascript
const value = await instance.getValue.call();
// value reprsents the `value` storage object in the solidity contract
// since the contract returns that value.
```

More helpfully, we do not even need to use `.call` when a function is marked as `constant`, because `tronbox-contract` will automatically know that this function can only be interacted with via a call.

```javascript
const value = await instance.getValue();
// val reprsents the `value` storage object in the solidity contract
// since the contract returns that value.
```

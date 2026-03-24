---
title: method.call()
excerpt: >-
  Use `call` to execute a `pure` or `view` smart contract method. These methods
  do not modify the blockchain, do not cost anything to execute and are also not
  broadcasted to the network.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Usage**

```javascript
//Example 1
let abi = [...];
let contract = await tronWeb.contract(abi, 'contractAddress'); 
let result = await contract.function_name(para1,para2,...).call();

//Example 2
let abi = [...];
let contract = await tronWeb.contract(abi, 'contractAddress'); 
let result = await contract["function_name"](para1,para2,...).call();
```

**Parameters**\
No need to pass parameters

**Returns**\
Object 

**Example**

```
//example 1
async function triggercontract(){
   let abi = [...];
   let instance = await tronWeb.contract(abi, 'TBBp5VF2q73hfMUoyxr138Kx3kbsi6HQRS');
   let res = await instance.totalSupply().call();
   console.log(res);
}
triggercontract();

//example 2
async function triggercontract(){
   let abi = [...];
   let instance = await tronWeb.contract(abi, 'TBBp5VF2q73hfMUoyxr138Kx3kbsi6HQRS');
   let res = await instance["totalSupply"]().call();
   console.log(res);
}
triggercontract();
```

---
title: estimateEnergy
excerpt: >-
  Estimate the energy required to trigger the contract. This interface requires
  the fullnode node to enable the service. If the call is not enabled, an error
  will be reported. You can continue to use the triggerconstantcontract
  interface to estimate the energy. (v5.1.0 new interface)
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Usage

```js
tronWeb.transactionBuilder.estimateEnergy(contractAddress, functionSelector, options, parameter, issuerAddress);
```

### Parameters

| Parameters       | Parameter Description                                          | Type      |
| :--------------- | :------------------------------------------------------------- | :-------- |
| contractAddress  | the smart contract address                                     | hexString |
| functionSelector | function call, must not leave a blank space                    | String    |
| options          | optional fields (permission id, feelimit and other parameters) | Object    |
| parameter        | the parameter passed to 'function'                             | Array     |
| issuerAddress    | address that triggers the contract                             | hexString |

### Return

Object

### Example

```js
>const result = await tronWeb.transactionBuilder.estimateEnergy(contractAddress, functionSelector, options, parameter, issuerAddress);
> {
  "result": {...}, //The result section is the result of the triggerconstantcontract
  "energy_required": 900000
}
```

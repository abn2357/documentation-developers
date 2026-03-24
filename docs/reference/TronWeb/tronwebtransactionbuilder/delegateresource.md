---
title: delegateResource
excerpt: >-
  After staking and obtaining resources, resources can be delegated to multiple
  recipients through this interface. The optional lock parameter can specify
  whether the delegation can be revoked within 3 days. (v5.1.0 new interface)
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
tronWeb.transactionBuilder.delegateResource(amount, receiverAddress, resource, address, lock, lockPeriod, options);
```

### Parameters

| Parameters      | Parameter Description                                                                                                                                                                                                                      | Type    |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| amount          | the amount of assets to be delegated(sun), larger than 0                                                                                                                                                                                   | Integer |
| receiverAddress | the account address of receiving delegation (base58 or hex)                                                                                                                                                                                | String  |
| resource        | asset type to be delegated, optional BANDWIDTH or ENERGY                                                                                                                                                                                   | String  |
| address         | owner address (base58 or hex)                                                                                                                                                                                                              | String  |
| lock            | enable the lock time limit, the default is false                                                                                                                                                                                           | Boolean |
| lockPeriod      | when lock is true, can set the lock time by this parameter, with the unit of blocks. And the new resource delegating to the same address of same type should have this lockPeriod value larger than the lockup blocks left of the address. | Integer |
| options         | optional fields                                                                                                                                                                                                                            | Object  |

### Return

Object

### Example

```js
> const transaction = await tronWeb.transactionBuilder.delegateResource(10e6, 'receiverAddress', 'BANDWIDTH', 'ownerAddress', true, 86400);
```

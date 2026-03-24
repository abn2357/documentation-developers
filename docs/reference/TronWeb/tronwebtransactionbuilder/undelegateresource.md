---
title: undelegateResource
excerpt: >-
  The interface used to revoke delegated resource, which can specify the number
  of revoked resources. (v5.1.0 new interface)
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
tronWeb.transactionBuilder.undelegateResource(amount, receiverAddress, resource, address, options);
```

### Parameters

| Parameters      | Parameter Description                                               | Type    |
| :-------------- | :------------------------------------------------------------------ | :------ |
| amount          | the amount of assets to be revoked (sun), larger than 0             | Integer |
| receiverAddress | the account address to receive revoked delegation (base58 or hex)   | String  |
| resource        | asset type of revoked delegation, optional BANDWIDTH or ENERGY      | String  |
| address         | the account address of the revoked delegation asset (base58 or hex) | String  |
| options         | optional fields                                                     | Object  |

### Return

Object

### Example

```js
> const transaction = await tronWeb.transactionBuilder.undelegateResource(10e6, 'receiverAddress', 'BANDWIDTH', 'ownerAddress');
```

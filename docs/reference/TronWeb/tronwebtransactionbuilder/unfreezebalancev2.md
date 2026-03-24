---
title: unfreezeBalanceV2
excerpt: >-
  The interface used to cancel the staked resources. It can specify the number
  of canceled stakes, but the number cannot exceed the number that can be
  canceled. The delegated resources cannot be canceled. (v5.1.0 new interface)
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
tronWeb.transactionBuilder.unfreezeBalanceV2(amount, resource, address, options);
```

### Parameters

| Parameters | Parameter Description                                   | Type    |
| :--------- | :------------------------------------------------------ | :------ |
| amount     | the amount of assets to be frozen (sun), larger than 0  | Integer |
| resource   | the frozen asset type, optional BANDWIDTH or ENERGY     | String  |
| address    | the account address of the frozen asset (base58 or hex) | String  |
| options    | optional fields                                         | Object  |

### Return

Object

### Example

```js
> const transaction = await tronWeb.transactionBuilder.unfreezeBalanceV2(10e6, 'BANDWIDTH', 'ownerAddress')
```

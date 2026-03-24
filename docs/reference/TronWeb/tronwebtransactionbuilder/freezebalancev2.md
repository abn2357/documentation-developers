---
title: freezeBalanceV2
excerpt: >-
  The interface used to stake and obtain resources. The resource type can be
  specified as BANDWIDTH or ENERGY. (v5.1.0 new interface)
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
tronWeb.transactionBuilder.freezeBalanceV2(amount, resource, address, options);
```

### Parameters

| Parameter Name | Parameter Description                                   | Type    |
| :------------- | :------------------------------------------------------ | :------ |
| amount         | the amount of assets to be frozen (sun), larger than 0  | Integer |
| resource       | the frozen asset type, optional BANDWIDTH or ENERGY     | String  |
| address        | the account address of the frozen asset (base58 or hex) | String  |
| options        | optional fields                                         | Object  |

### Return

Object

### Example

```js
> const transaction = await tronWeb.transactionBuilder.freezeBalanceV2(10e6, 'BANDWIDTH', 'ownerAddress');
```

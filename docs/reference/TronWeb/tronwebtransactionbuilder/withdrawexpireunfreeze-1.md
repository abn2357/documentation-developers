---
title: withdrawExpireUnfreeze
excerpt: >-
  After performing the operation of canceling the stake, the user need to call
  this interface to retrieve resources after waiting for N days. N is a Tron
  network parameter. (v5.1.0 new interface)
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
tronWeb.transactionBuilder.withdrawExpireUnfreeze(address);
```

### Parameters

| Parameters | Parameter Description                  | Type   |
| :--------- | :------------------------------------- | :----- |
| address    | refund account address (base58 or hex) | String |

### Return

Object

### Example

```js
> const transaction = await tronWeb.transactionBuilder.withdrawExpireUnfreeze('ownerAddress');
```

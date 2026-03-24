---
title: cancelUnfreezeBalanceV2
excerpt: >-
  Support canceling unstaking in Stake 2.0, which means that users can use this
  API to cancel unstaking in waiting period time, make the unstaking TRX
  restaked, and meanwhile help users withdraw the TRX expired waiting period to
  balance. (v5.3.0 new interface)
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
tronWeb.transactionBuilder.cancelUnfreezeBalanceV2(address);
```

### Parameters

| Parameters | Parameter Description                   | Type   |
| :--------- | :-------------------------------------- | :----- |
| address    | restake account address (base58 or hex) | String |

### Return

Object

### Example

```js
> const transaction = await tronWeb.transactionBuilder.cancelUnfreezeBalanceV2('ownerAddress');
```

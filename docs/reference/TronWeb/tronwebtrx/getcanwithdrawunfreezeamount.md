---
title: getCanWithdrawUnfreezeAmount
excerpt: >-
  Query an account under the V2 interface, if you operate WithdrawExpireUnfreeze
  to withdraw the principal, the amount of withdrawal principal that can be
  obtained. (v5.1.0 new interface)
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
tronWeb.trx.getCanWithdrawUnfreezeAmount(address, timestamp, options);
```

### Parameters

| Parameters | Parameter Description                                                     | Type    |
| :--------- | :------------------------------------------------------------------------ | :------ |
| address    | account address (base58 or hex)                                           | String  |
| timestamp  | query cutoff timestamp(millisecond), larger than 0, default is Date.now() | Integer |
| options    | optional fields                                                           | Object  |

### Return

Object

### Example

```js
> const { amount } = await tronWeb.trx.getCanWithdrawUnfreezeAmount('ownerAddress', Date.now());
{
    "amount": 9000000
}
```

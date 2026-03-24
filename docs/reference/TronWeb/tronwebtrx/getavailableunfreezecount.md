---
title: getAvailableUnfreezeCount
excerpt: >-
  Query the number of times an account can operate UnFreezeBalanceV2 to unfreeze
  under the V2 interface. (v5.1.0 new interface)
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
tronWeb.trx.getAvailableUnfreezeCount('address', options);
```

### Parameters

| Parameters | Parameter Description           | Type   |
| :--------- | :------------------------------ | :----- |
| address    | account address (base58 or hex) | String |
| options    | optional fields                 | Object |

### Return

Object

### Example

```js
> const { count } = await tronWeb.trx.getAvailableUnfreezeCount('ownerAddress');
{
    "count": 32
}
```

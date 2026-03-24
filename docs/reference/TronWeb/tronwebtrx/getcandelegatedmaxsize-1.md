---
title: getCanDelegatedMaxSize
excerpt: >-
  Query the maximum value of an account's delegated resources (BANDWIDTH,
  ENERGY) that can be operated on DelegateResource under the V2 interface.
  (v5.1.0 new interface)
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
tronWeb.trx.getCanDelegatedMaxSize(address, resource，options);
```

### Parameters

| Parameters | Parameter Description                       | Type   |
| :--------- | :------------------------------------------ | :----- |
| address    | account address (base58 or hex)             | String |
| resource   | resource type, optional BANDWIDTH or ENERGY | String |
| options    | optional fields                             | Object |

### Return

Object

### Example

```js
> const { max_size } = await tronWeb.trx.getCanDelegatedMaxSize('ownerAddress'，'BANDWIDTH');
{
    "max_size": 100000000
}
```

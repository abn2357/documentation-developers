---
title: getDelegatedResourceV2
excerpt: >-
  Query the resources that an account delegates to another account under the V2
  interface. (v5.1.0 new interface)
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
tronWeb.trx.getDelegatedResourceV2(fromAddress, toAddress, options)
```

### Parameters

| Parameters  | Parameter Description                         | Type   |
| :---------- | :-------------------------------------------- | :----- |
| fromAddress | resource from account address (base58 or hex) | String |
| toAddress   | resource to account address (base58 or hex)   | String |
| options     | optional fields                               | Object |

### Return

Object

### Example

```js
>const delegationInfo = await tronWeb.trx.getDelegatedResourceV2('fromAddress', 'toAddress')
> {
    "delegatedResource": [
        {
            "from": "fromAddress",
            "to": "toAddress",
            "frozen_balance_for_bandwidth": 10000000
        }
    ]
}
```

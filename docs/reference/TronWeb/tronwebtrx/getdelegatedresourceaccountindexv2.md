---
title: getDelegatedResourceAccountIndexV2
excerpt: >-
  Query which accounts have delegated resources to other accounts under the V2
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
tronWeb.trx.getDelegatedResourceAccountIndexV2(address)
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
>const delegationInfo = await tronWeb.trx.getDelegatedResourceAccountIndexV2('ownerAddress')
> {
    "account": "ownerAddress",
    "toAccounts": [
        "toAddress1"
    ]
}
```

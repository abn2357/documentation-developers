---
title: getBandwidth
excerpt: Query the Bandwidth information for the account.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Usage** 

```javascript
tronWeb.trx.getBandwidth("");
```

**Parameters**\
   String(HexString or Base58)

**Returns**\
  Object

**Example** 

```javascript
//Example 1
>tronWeb.trx.getBandwidth('TVJ6njG5EpUwJt4N9xjTrqU5za78cgadS2');
  Promise{<pending>}
  __proto__: Promise
 [[PromiseStatus]]: "resolved"
 [[PromiseValue]]: 5000

//Example 2
>tronWeb.trx.getBandwidth('41D3FD1B6F3F3A86303E2925844456C49876C4561F');
  Promise {<pending>}
  __proto__: Promise
 [[PromiseStatus]]: "resolved"
 [[PromiseValue]]: 5000
```

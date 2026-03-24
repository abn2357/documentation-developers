---
title: getUnconfirmedBrokerage
excerpt: Query unconfirmed brokerage
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
tronWeb.trx.getUnconfirmedBrokerage(address)
```

**Parameter**\
String(HexString or Base58)

**Return**\
Number

**Example**

```javascript
//Parameter Base58
>tronWeb.trx.getUnconfirmedBrokerage("TLyqzVGLV1srkB7dToTAEqgDSfPtXRJZYH").then(result=>console.log(result))
Promise { <pending> }
> 20

//Parameter HexString
>tronWeb.trx.getUnconfirmedBrokerage("4178C842EE63B253F8F0D2955BBC582C661A078C9D").then(result=>console.log(result))
Promise { <pending> }
> 20
```

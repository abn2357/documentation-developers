---
title: getReward
excerpt: Query voted and block reward
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
tronWeb.trx.getReward(address)
```

**Parameter**\
String(HexString or Base58)

**Return**\
Number

**Example**

```javascript
//Parameter Base58
>tronWeb.trx.getReward("TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ").then(result=>console.log(result))
Promise { <pending> }
> 0
//Parameter HexString
>tronWeb.trx.getReward("41BF97A54F4B829C4E9253B26024B1829E1A3B1120").then(result=>console.log(result))
Promise { <pending> }
> 0
```

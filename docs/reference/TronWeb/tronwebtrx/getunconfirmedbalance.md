---
title: getUnconfirmedBalance
excerpt: Query unconfirmed balance
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
tronWeb.trx.getUnconfirmedBalance(address);
```

**Parameter**\
String(HexString or Base58)

**Return**\
Number

**Example**

```javascript
//Parameter Base58
>tronWeb.trx.getUnconfirmedBalance('TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ').then(result=>console.log(result))
Promise { <pending> }
> 29340074430
         
//Parameter HexString
>tronWeb.trx.getUnconfirmedBalance('41BF97A54F4B829C4E9253B26024B1829E1A3B1120').then(result=>console.log(result))
Promise { <pending> }
> 29340074430
```

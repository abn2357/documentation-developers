---
title: getBalance
excerpt: Get the account's balance of TRX, and display the TRX balance in SUN
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
tronWeb.trx.getBalance(address);
```

**Parameter**\
String(HexString or Base58)

**Return**\
Number

**Example**

```javascript
//Parameter Base58
> tronWeb.trx.getBalance('TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ').then(result => console.log(result))
Promise { <pending> }
> 29887074430
         
//Parameter HexString
>tronWeb.trx.getBalance('41BF97A54F4B829C4E9253B26024B1829E1A3B1120').then(result => console.log(result))
Promise { <pending> }
> 29340074430
```

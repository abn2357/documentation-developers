---
title: transaction.txJsonToPb
excerpt: >-
  Serialize a transaction, convert transaction object in json format into
  protobuf structure
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
TronWeb.utils.transaction.txJsonToPb(transaction)
```

**Parameters**\
transaction : Object - The transaction object in json format.

**Return**\
Object - A transaction object in protobuf format.

**Example**

```javascript
const txJson = await tronWeb.transactionBuilder.sendTrx("TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr", 100, "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL");
const txPb = TronWeb.utils.transaction.txJsonToPb(txJson);
```

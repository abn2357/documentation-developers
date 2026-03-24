---
title: transaction.txPbToTxID
excerpt: Calculate the transaction ID from the transaction protobuf format
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
tronWeb.utils.transaction.txPbToTxID(transaction)
```

**Parameters**\
transaction - Transaction object in protobuf format.

**Return**\
String - Transaction ID

**Example**

```javascript
const txJson = await tronWeb.transactionBuilder.sendTrx("TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr", 100, "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL");
// Convert the transaction object in json format to protobuf format
const txPb = TronWeb.utils.transaction.txJsonToPb(txJson);
// Calculate the transaction ID from the transaction protobuf format
const txID = tronWeb.utils.transaction.txPbToTxID(txPb);
```

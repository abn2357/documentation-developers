---
title: sign
excerpt: Sign a provided transaction object
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ❗️ WARNING
>
> Do not use this in any web / user-facing applications. This will expose the private key.

# Usage

```javascript
// sign a transaction
tronWeb.trx.sign(transaction, privateKey);
```

# Input Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Data Type
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        transaction
      </td>

      <td>
        The transaction object
      </td>

      <td>
        JSON
      </td>
    </tr>

    <tr>
      <td>
        privateKey
      </td>

      <td>
        The private key used for signing. Optional.  The default value is the private key passed in when constructing tronweb object.
      </td>

      <td>
        String
      </td>
    </tr>
  </tbody>
</Table>

# Example

sign a transaction

```json
const tradeobj = await tronWeb.transactionBuilder.sendTrx("TNo9e8MWQpGVqdyySxLSTw3gjgFQWE3vfg", 100,"TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR",1);  
const signedtxn = await tronWeb.trx.sign(tradeobj, privateKey);
console.log(signedtxn)
>{ visible: false,
  txID:
   'cbf76171dcf5f8fe00b4911a1a6cc4d2a4448e3348f44d240ca20af06025d0f2',
  raw_data:
   { contract: [ [Object] ],
     ref_block_bytes: '6394',
     ref_block_hash: '8ad966a9b0b6a5d1',
     expiration: 1580983512000,
     timestamp: 1580983453441 },
  raw_data_hex:
   '0a02639422088ad966a9b0b6a5d140c0d7d7cf812e5a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a15417946f66d0fc67924da0ac9936183ab3b07c811261215418cb2ab880d4fa7b33c9645a2276dc9b192902e2d186470818ed4cf812e',
  signature:
   [ '47b1f77b3e30cfbbfa41d795dd34475865240617dd1c5a7bad526f5fd89e52cd057c80b665cc2431efab53520e2b1b92a0425033baee915df858ca1c588b0a1800' ] }
```

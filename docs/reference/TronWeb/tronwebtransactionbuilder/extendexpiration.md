---
title: extendExpiration
excerpt: Extend unsigned transaction expiration time in seconds.
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
tronWeb.transactionBuilder.extendExpiration(transaction, extension);
```

**Parameters**

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
        The transaction object.
      </td>

      <td>
        JSON
      </td>
    </tr>

    <tr>
      <td>
        extension
      </td>

      <td>
        Extension of the expiration time in seconds, must be greater than 3
      </td>

      <td>
        Integer
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
Object 

**Note**\
The Transaction hash(Transaction ID) will be changed after "extendExpiration" was executed as a new transaction object is generated. Please use the newly generated Transactions for subsequent processes like sign or broadcast. thanks.

**Example**

```javascript
> const transaction = await tronWeb.transactionBuilder.sendTrx("TNo9e8MWQpGVqdyySxLSTw3gjgFQWE3vfg", 100,"TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR");  
> const extendExpirationObj =  await tronWeb.transactionBuilder.extendExpiration(transaction, 500);
> const signedtxn = await tronWeb.trx.sign(extendExpirationObj, privateKey);
console.log(extendExpirationObj);
> {txID: "a33e940480202c8d38c65a571a699be4e082e40776bab0000103c8cca63f6cb4", raw_data: {…}, raw_data_hex: "0a02c9bc2208a506a5de6e7a02c040d0c48fd3822e5a650801…d4fa7b33c9645a2276dc9b192902e2d186470e7b1edd2822e", visible: false}
txID: "a33e940480202c8d38c65a571a699be4e082e40776bab0000103c8cca63f6cb4"
raw_data: {contract: Array(1), ref_block_bytes: "c9bc", ref_block_hash: "a506a5de6e7a02c0", expiration: 1581259154000, timestamp: 1581258594535}
raw_data_hex: "0a02c9bc2208a506a5de6e7a02c040d0c48fd3822e5a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a15417946f66d0fc67924da0ac9936183ab3b07c811261215418cb2ab880d4fa7b33c9645a2276dc9b192902e2d186470e7b1edd2822e"
visible: false
__proto__: Object
```

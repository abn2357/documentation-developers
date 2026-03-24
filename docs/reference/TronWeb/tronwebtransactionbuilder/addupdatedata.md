---
title: addUpdateData
excerpt: add memo to an unsigned transaction
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
tronWeb.transactionBuilder.addUpdateData(unsignedTransaction,memo);
```

**Parameter**

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Argument
      </th>

      <th>
        Description
      </th>

      <th>
        Type
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        unsignedTransaction
      </td>

      <td>
        unsigned transaction object
      </td>

      <td>
        JSON
      </td>
    </tr>

    <tr>
      <td>
        memo
      </td>

      <td>
        memo info
      </td>

      <td>
        string
      </td>
    </tr>
  </tbody>
</Table>

**Return**\
object

**Note**\
The Transaction hash(Transaction ID) will be changed after "addUpdateData" was executed as a new transaction object is generated. Please use the newly generated Transactions for subsequent processes like sign or broadcast. thanks. 

**Example**

```javascript
> var txn = await tronWeb.transactionBuilder.sendTrx("TUoHaVjx7n5xz8LwPRDckgFrDWhMhuSuJM", 100, "TUznHJfHe6gdYY7gvWmf6bNZHuPHDZtowf");
> var nexTxn = await tronWeb.transactionBuilder.addUpdateData(txn,"test");
> var signedtxn = await tronWeb.trx.sign(nexTxn, privateKey);
> console.log(nexTxn)
>{
  visible: false,
  txID: "8c3a4b4c20cfdf8df340905949a8241aee639492e0c4d73f1bf18847346444f1",
  raw_data: {
    contract: [ [Object] ],
    data: "74657374", // this is the HexString of memo
	expiration: 1628073045000,
	ref_block_bytes: "7254",
	ref_block_hash: "c45fff3a6a0347cc",
	timestamp: 1628072986845
  },
  raw_data_hex: "0a0272542208c45fff3a6a0347cc4088d8dc85b12f5204746573745a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a1541d0b69631440f0a494bb51f7eee68ff5c593c00f0121541ce8a0cf0c16d48bcf22825f6053248df653c89ca186470dd91d985b12f"
}
```

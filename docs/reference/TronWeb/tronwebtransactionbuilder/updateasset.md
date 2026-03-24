---
title: updateAsset
excerpt: >-
  Create an unsigned transaction that update trc10 token information,equivalent
  to createtoken
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
const options = {
  description:"justfortest",//The description of token, default String
  url:"www.cctv.com",//The token's website url, default String
  freeBandwidth:1000000,//Each token holder's free bandwidth,default number
  freeBandwidthLimit:100,//The total free bandwidth of the token
  permissionId:1//Optional, for multi-signature use
}
tronWeb.transactionBuilder.updateAsset(options, issuerAddress)
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
        options
      </td>

      <td>
        a object that contain some parameters
      </td>

      <td>
        object
      </td>
    </tr>

    <tr>
      <td>
        issuerAddress
      </td>

      <td>
        address  of the token issuer,format: hexstring or base58
      </td>

      <td>
        String
      </td>
    </tr>
  </tbody>
</Table>

**Return**\
object

**Example**

```javascript
> const createasset = {
...   description:"justfortest",
...   url:"www.cctv.com",
...   freeBandwidth:1000000,
...   freeBandwidthLimit:100,
...   permissionId:1
... }
>tronWeb.transactionBuilder.updateAsset(createasset,"TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ").then(result=>console.log(result))
Promise { <pending> }
> {
  visible: false,
  txID: '009e8b45c34fbccf86d3f8d1f5e52d694c40b14550289a49048e9ba64799520f',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: '21ca',
    ref_block_hash: '65b258d979c2d3f8',
    expiration: 1581326298000,
    timestamp: 1581326241240
  },
  raw_data_hex: '0a0221ca220865b258d979c2d3f84090d791f3822e5a72080f126c0a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5570646174654173736574436f6e747261637412380a1541bf97a54f4b829c4e9253b26024b1829e1a3b1120120b6a757374666f72746573741a0c7777772e636374762e636f6d20c0843d2864280170d89b8ef3822e'
}
```

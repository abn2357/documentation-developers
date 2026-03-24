---
title: vote
excerpt: Create an unsigned transaction that vote for witnesses
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
tronWeb.transactionBuilder.vote( votes = {srAddress : voteCount}, voterAddress = this.tronWeb.defaultAddress.hex);
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
        votes
      </td>

      <td>
        dictionary of SR address : vote count key-value pair (SR address format: hexstring or base58)
      </td>

      <td>
        object
      </td>
    </tr>

    <tr>
      <td>
        voterAddress
      </td>

      <td>
        voter address,format:hexstring or base58
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        option
      </td>

      <td>
        The permission Id,optional, for multi-signature use
      </td>

      <td>
        number
      </td>
    </tr>
  </tbody>
</Table>

**Return**\
object

**Example**

```javascript
>tronWeb.transactionBuilder.vote({"TGj1Ej1qRzL9feLTLhjwgxXF4Ct6GTWg2U":1,"TLyqzVGLV1srkB7dToTAEqgDSfPtXRJZYH":1},"TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ",1).then(result=>console.log(result))
Promise { <pending> }
> {
  visible: false,
  txID: 'e214267985087a1820a8533586f5c7db010084f8caa109f967a57e8fbc035a1b',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: '1dca',
    ref_block_hash: 'cb1fd6e2719cef8c',
    expiration: 1581399042000,
    timestamp: 1581398984483
  },
  raw_data_hex: '0a021dca2208cb1fd6e2719cef8c40d0cfe995832e5a860108041281010a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e566f74655769746e657373436f6e7472616374124d0a1541bf97a54f4b829c4e9253b26024b1829e1a3b112012190a15414a193c92cd631c1911b99ca964da8fd342f4cddd100112190a154178c842ee63b253f8f0d2955bbc582c661a078c9d100170a38ee695832e'
}
```

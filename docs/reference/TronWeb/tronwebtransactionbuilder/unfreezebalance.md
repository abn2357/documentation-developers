---
title: unfreezeBalance
excerpt: >-
  Creates an unsigned unfreeze TRX transaction. This unfreezes TRX for the
  specified resource. If you unfreeze for BANDWIDTH, it removes TRON POWER,
  which also removes  VOTES. If the bandwidth is already spent, the account will
  be negative for bandwidth.
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
tronWeb.transactionBuilder.unfreezeBalance(resource, ownerAddress, receiverAddress, options);
```

**Parameter**

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter Name
      </th>

      <th>
        Parameter Description
      </th>

      <th>
        Integer Type
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        resource
      </td>

      <td>
        Specifying the resource type. Must be either "BANDWIDTH" or "ENERGY".
      </td>

      <td>
        string
      </td>
    </tr>

    <tr>
      <td>
        address (optional)
      </td>

      <td>
        Address of the owner of the TRX to be unstaked (defaults to caller's default address).(format:hexstring or base58)
      </td>

      <td>
        string
      </td>
    </tr>

    <tr>
      <td>
        receiver address
      </td>

      <td>
        Address of user in which the resource is being removed from, due to unstake.(hexstring or base58)
      </td>

      <td>
        string
      </td>
    </tr>

    <tr>
      <td>
        options
      </td>

      <td>
        The permission Id,for multi-signature use
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
>tronWeb.transactionBuilder.unfreezeBalance("BANDWIDTH","41BF97A54F4B829C4E9253B26024B1829E1A3B1120","41BF97A54F4B829C4E9253B26024B1829E1A3B1120",1).then(result=>console.log(result))
Promise { <pending> }
> {
  visible: false,
  txID: '2ba070338263eecbec034aac62a0a9b906a033ac34eb3e183cc7ccc2c4d1fb20',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: 'afa9',
    ref_block_hash: 'd25a977d06b9fb63',
    expiration: 1581312834000,
    timestamp: 1581312774685
  },
  raw_data_hex: '0a02afa92208d25a977d06b9fb6340d0f3dbec822e5a53080c124f0a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e556e667265657a6542616c616e6365436f6e747261637412170a1541bf97a54f4b829c4e9253b26024b1829e1a3b1120709da4d8ec822e'
}
```

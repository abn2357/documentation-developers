---
title: updateBrokerage
excerpt: Create an unsigned transaction that updates the Super representative brokerage
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
tronWeb.transactionBuilder.updateBrokerage(brokerage,ownerAddress);
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
        brokerage
      </td>

      <td>
        An integer which defines percentage of the brokerage
      </td>

      <td>
        number
      </td>
    </tr>

    <tr>
      <td>
        ownerAddress
      </td>

      <td>
        Account address
      </td>

      <td>
        string
      </td>
    </tr>
  </tbody>
</Table>

**Return**\
object

**Example**

```javascript
>tronWeb.transactionBuilder.updateBrokerage(100,"414A193C92CD631C1911B99CA964DA8FD342F4CDDD").then(result=>console.log(result))
Promise { <pending> }
> {
  visible: false,
  txID: '754bfc80cf42aa3154fda717262b0ade47ff64b108ad0fdc5f9236d5d4b0ae8a',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: 'c466',
    ref_block_hash: '150f95204fc606c0',
    expiration: 1581328767000,
    timestamp: 1581328708518
  },
  raw_data_hex: '0a02c4662208150f95204fc606c04098b0a8f4822e5a55083112510a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e55706461746542726f6b6572616765436f6e747261637412190a15414a193c92cd631c1911b99ca964da8fd342f4cddd106470a6e7a4f4822e'
}
```

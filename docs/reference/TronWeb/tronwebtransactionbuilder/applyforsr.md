---
title: applyForSR
excerpt: >-
  Create an unsigned transaction that apply to be an SR and this account balance
  needs to be at least 9999trx,it will consume 9999trx.
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
// Format
tronWeb.transactionBuilder.applyForSR(address, url, options)
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
        address
      </td>

      <td>
        account address apply for SR in hex format(hexstring or base58)
      </td>

      <td>
        string
      </td>
    </tr>

    <tr>
      <td>
        url
      </td>

      <td>
        SR URL link
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
>tronWeb.transactionBuilder.applyForSR("41BF97A54F4B829C4E9253B26024B1829E1A3B1120","www.fortest.com").then(result=>console.log(result))
41bf97a54f4b829c4e9253b26024b1829e1a3b1120 false
41bf97a54f4b829c4e9253b26024b1829e1a3b1120 false
41bf97a54f4b829c4e9253b26024b1829e1a3b1120
Promise { <pending> }
> {
  visible: false,
  txID: '388172e15216a6eb216a11ed312c3794ce50dd85873e83767b6c5bea1da78b43',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: '499a',
    ref_block_hash: '05853c8ec7523765',
    expiration: 1580963556000,
    timestamp: 1580963496941
  },
  raw_data_hex: '0a02499a220805853c8ec752376540a0d595c6812e5a620805125e0a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5769746e657373437265617465436f6e747261637412280a1541bf97a54f4b829c4e9253b26024b1829e1a3b1120120f7777772e666f72746573742e636f6d70ed8792c6812e'
}
```

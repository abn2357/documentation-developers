---
title: withdrawBlockRewards
excerpt: Creates an unsigned Super Representative award balance withdrawal transaction.
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
tronWeb.transactionBuilder.withdrawBlockRewards(address, options);
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
        address
      </td>

      <td>
        Optional address of SR’s withdrawal account.
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        options
      </td>

      <td>
        Optional, permission\_id for multi-signature use.
      </td>

      <td>
        Integer
      </td>
    </tr>
  </tbody>
</Table>

**返回值类型**\
Object 

**示例**

```javascript
//Example 1
>tronWeb.transactionBuilder.withdrawBlockRewards("41f1a0466076c57c9f6d07decc86021ddbf8bae0b2", 1).then(result => console.log(result));
Promise { <pending> }
> {
  visible: false,
  txID: '148f2813c2ad76a2f487b3ef402401f7907a8157d9edd60d50f122a8b324dc4e',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: '37d9',
    ref_block_hash: 'c1d5f084d21183b5',
    expiration: 1581343245000,
    timestamp: 1581343187719
  },
  raw_data_hex: '0a0237d92208c1d5f084d21183b540c8859cfb822e5a53080d124f0a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e576974686472617742616c616e6365436f6e747261637412170a1541f1a0466076c57c9f6d07decc86021ddbf8bae0b27087c698fb822e'
}
         
//Example 2
>tronWeb.transactionBuilder.withdrawBlockRewards("TXzorPLynzrRLyfMNXHsGU86doJCad3bQi", 1).then(result => console.log(result));
Promise { <pending> }
> {
  visible: false,
  txID: '04959cc5e0f1836b92e99063ff5d632293cb4cfef9b443ce493253c8b99f2a8a',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: '38cf',
    ref_block_hash: 'f15243134137dc9c',
    expiration: 1581343983000,
    timestamp: 1581343924685
  },
  raw_data_hex: '0a0238cf2208f15243134137dc9c40988bc9fb822e5a53080d124f0a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e576974686472617742616c616e6365436f6e747261637412170a1541f1a0466076c57c9f6d07decc86021ddbf8bae0b270cdc3c5fb822e'
}
```

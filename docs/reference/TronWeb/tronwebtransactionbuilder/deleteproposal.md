---
title: deleteProposal
excerpt: Create a transaction that deletes a proposal.
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
tronWeb.transactionBuilder.deleteProposal(proposalID, issuerAddress, options);
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
        proposalID
      </td>

      <td>
        integer type proposal id.
      </td>

      <td>
        Integer
      </td>
    </tr>

    <tr>
      <td>
        isserAddress
      </td>

      <td>
        proposal issuer address in hex string.
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

**Returns**\
Object 

**Example**

```javascript
//example 1
> tronWeb.transactionBuilder.deleteProposal(1, "41010D3A8E0D80F8C83148240202DD178DF495B7BD", 1).then(result => console.log(result));
Promise { <pending> }
> {
  visible: false,
  txID: '1152c19215aaefffe166cf9fcd6a299b06f532f8ec4b62b9804338fbe533308d',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: '03cf',
    ref_block_hash: 'ec181002d427df4c',
    expiration: 1581332046000,
    timestamp: 1581331986337
  },
  raw_data_hex: '0a0203cf2208ec181002d427df4c40b0c1f0f5822e5a54081212500a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c44656c657465436f6e747261637412190a1541010d3a8e0d80f8c83148240202dd178df495b7bd100170a1efecf5822e'
}

//example 2
> tronWeb.transactionBuilder.deleteProposal(1, "TA4mXQ6rMNSBcvd9Kn9LLFS4bbX8b27RCS", 1).then(result => console.log(result));
Promise { <pending> }
> {
  visible: false,
  txID: '512a758fc5b87615b10c28f840d72f977286384e77959a421c2470bd580f2845',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: '04bb',
    ref_block_hash: 'ca274c26abdb1fc6',
    expiration: 1581332754000,
    timestamp: 1581332694494
  },
  raw_data_hex: '0a0204bb2208ca274c26abdb1fc640d0dc9bf6822e5a54081212500a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c44656c657465436f6e747261637412190a1541010d3a8e0d80f8c83148240202dd178df495b7bd100170de8b98f6822e'
}
```

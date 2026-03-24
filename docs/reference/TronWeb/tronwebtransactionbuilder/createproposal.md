---
title: createProposal
excerpt: Create an unsigned transaction that create proposal
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
tronWeb.transactionBuilder.createProposal(parameters, issuerAddress, options)
```

**Parameter**\
array(parameters),hexstring(issuerAddress),number(optional,or multi-signature use)

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
        parameters
      </td>

      <td>
        Proposal parameters
      </td>

      <td>
        Array
      </td>
    </tr>

    <tr>
      <td>
        issuerAddress
      </td>

      <td>
        Creator address(format:hexstring or base58)
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
        Optional, permission\_id  for multi-signature use
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
> tronWeb.transactionBuilder.createProposal([{"key":32,"value":1},{"key":33,"value":11}],"41BF97A54F4B829C4E9253B26024B1829E1A3B1120",1).then(result=>console.log(result))
Promise { <pending> }
> {
  visible: false,
  txID: '771d2fe10099dd2d48e9f874bc7c17a5882c77bca2622fbb695cc59327e1bc08',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: 'ba3b',
    ref_block_hash: 'e09ff41b96e649f1',
    expiration: 1581050079000,
    timestamp: 1581050021547
  },
  raw_data_hex: '0a02ba3b2208e09ff41b96e649f14098ceb6ef812e5a5e0810125a0a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c437265617465436f6e747261637412230a1541bf97a54f4b829c4e9253b26024b1829e1a3b112012040820100112040821100b70ab8db3ef812e'
}
```

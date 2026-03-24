---
title: updateEnergyLimit
excerpt: >-
  Create an unsigned transaction that update the Origin Energy Limit of the
  smart contract
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
tronWeb.transactionBuilder.updateEnergyLimit(contract_address, origin_energy_limit, owner_address,options);
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
        contract\_address
      </td>

      <td>
        Smart Contract address,format:hestring or base58
      </td>

      <td>
        string
      </td>
    </tr>

    <tr>
      <td>
        origin\_energy\_limit
      </td>

      <td>
        The maximum resource consumption of the creator in one execution or creation
      </td>

      <td>
        number
      </td>
    </tr>

    <tr>
      <td>
        owner\_address
      </td>

      <td>
        Smart contract creator's address,format:hestring or base58
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
        Optional, for multi-signature use
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
> tronWeb.transactionBuilder.updateEnergyLimit("TBQ8ubHnwWAZvHVPJevnKpEfabetDdaQdQ",30,"TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ",1).then(result=>console.log(result))
Promise { <pending> }
> {
  visible: false,
  txID: 'b17022e101f964e0f1b413e0862ca8a3ca6c7e48f39b1765103ca59bd3a84f0a',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: '2782',
    ref_block_hash: '6309a83565218acf',
    expiration: 1581330690000,
    timestamp: 1581330630613
  },
  raw_data_hex: '0a02278222086309a83565218acf40d0df9df5822e5a6e082d126a0a36747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e557064617465456e657267794c696d6974436f6e747261637412300a1541bf97a54f4b829c4e9253b26024b1829e1a3b11201215410faf1b6bce9e815555544aea9d350f9d3dc6d3ba181e70d58f9af5822e'
}
```

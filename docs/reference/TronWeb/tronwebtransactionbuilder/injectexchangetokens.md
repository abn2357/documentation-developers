---
title: injectExchangeTokens
excerpt: >-
  Create a transaction to inject tokens into  an exchange pair based on Bancor
  protocol.
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
tronWeb.transactionBuilder.injectExchangeTokens(exchangeID, tokenID, tokenAmount, ownerAddress, options)
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
        exchangeID
      </td>

      <td>
        non-negative integer exchange id.
      </td>

      <td>
        Integer
      </td>
    </tr>

    <tr>
      <td>
        tokenID
      </td>

      <td>
        Token id of the token inject.
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        tokenAmount
      </td>

      <td>
        The number of token inject.
      </td>

      <td>
        Integer
      </td>
    </tr>

    <tr>
      <td>
        ownerAddress
      </td>

      <td>
        The address of the creator of the exchange pair.
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
// Example 1
> tronWeb.transactionBuilder.injectExchangeTokens(1, "1000003",10000,"410ca7c49aa44d26aabfe7f594c645cf9f17a4ff70",1).then(result => console.log(result));
Promise { <pending> }
> {
  visible: false,
  txID: 'cdac0a375d5042042aef204301d67181bb83390ba060b11033a7913221af0ebb',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: 'ce03',
    ref_block_hash: '620c5f8f84ac6944',
    expiration: 1581261939000,
    timestamp: 1581261879534
  },
  raw_data_hex: '0a02ce032208620c5f8f84ac694440b8c2b9d4822e5a60082a125c0a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e45786368616e6765496e6a656374436f6e747261637412250a15410ca7c49aa44d26aabfe7f594c645cf9f17a4ff7010011a073130303030303320904e70eef1b5d4822e'
} 

//Example 2
> tronWeb.transactionBuilder.injectExchangeTokens(1, "1000003",10000,"TB8865sqTQ3qxWqhNQRCBov3KtPXFRPccK",1).then(result => console.log(result));
Promise { <pending> }
> {
  visible: false,
  txID: 'a05cace199e2a1d39410adfac5f17a18e63f43bdc78b5840f63a083cbcfa6cb9',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: '72a2',
    ref_block_hash: 'd85b910374acd2ed',
    expiration: 1581388404000,
    timestamp: 1581388345878
  },
  raw_data_hex: '0a0272a22208d85b910374acd2ed40a0aae090832e5a60082a125c0a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e45786368616e6765496e6a656374436f6e747261637412250a15410ca7c49aa44d26aabfe7f594c645cf9f17a4ff7010011a073130303030303320904e7096e4dc90832e'
}
```

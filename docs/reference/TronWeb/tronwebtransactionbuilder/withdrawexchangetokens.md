---
title: withdrawExchangeTokens
excerpt: >-
  Create a transaction to withdraw tokens from an exchange pair based on Bancor
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
tronWeb.transactionBuilder.withdrawExchangeTokens(exchangeID, tokenID, tokenAmount, ownerAddress, options);
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
        Token Id of the token withdraw.
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
        The number of the token withdraw.
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
//Example 1
> tronWeb.transactionBuilder.withdrawExchangeTokens(1, "1000003", 100, "410ca7c49aa44d26aabfe7f594c645cf9f17a4ff70", 1).then(result => console.log(result));
Promise { <pending> }
> {
  visible: false,
  txID: '560b803647f39b87a76623c4428102d1d96d18367b7f679412cc810029499a71',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: '6e55',
    ref_block_hash: '96fe9781aef670d8',
    expiration: 1581385101000,
    timestamp: 1581385042932
  },
  raw_data_hex: '0a026e55220896fe9781aef670d840c8dd968f832e5a61082b125d0a35747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e45786368616e67655769746864726177436f6e747261637412240a15410ca7c49aa44d26aabfe7f594c645cf9f17a4ff7010011a0731303030303033206470f497938f832e'
}

// Example 2
> tronWeb.transactionBuilder.withdrawExchangeTokens(1, "1000003", 100, "TB8865sqTQ3qxWqhNQRCBov3KtPXFRPccK", 1).then(result => console.log(result));
Promise { <pending> }
> {
  visible: false,
  txID: 'a776c9009655b72c4ad4858d391e25a522d753d9e40197f24703adda41dc3c77',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: '6e7b',
    ref_block_hash: '413bf5de7cf22452',
    expiration: 1581385215000,
    timestamp: 1581385155940
  },
  raw_data_hex: '0a026e7b2208413bf5de7cf224524098d89d8f832e5a61082b125d0a35747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e45786368616e67655769746864726177436f6e747261637412240a15410ca7c49aa44d26aabfe7f594c645cf9f17a4ff7010011a0731303030303033206470e48a9a8f832e'
}
```

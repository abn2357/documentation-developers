---
title: tradeExchangeTokens
excerpt: Trade tokens on a bancor style exchange.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
```javascript
// Format
tronWeb.transactionBuilder.tradeExchangeTokens(exchangeID, tokenName, tokenAmountSold, tokenAmountExpected, ownerAddress, options)
```

**Arguments**

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Argument
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Type
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        exchangeID
      </td>

      <td style={{ textAlign: "left" }}>
        non-negative integer exchange id
      </td>

      <td style={{ textAlign: "left" }}>
        integer
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        tokenID
      </td>

      <td style={{ textAlign: "left" }}>
        tokeID
      </td>

      <td style={{ textAlign: "left" }}>
        string
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        tokenAmountSold
      </td>

      <td style={{ textAlign: "left" }}>
        amount of token actually sold
      </td>

      <td style={{ textAlign: "left" }}>
        integer
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        tokenAmountExpected
      </td>

      <td style={{ textAlign: "left" }}>
        amount of token expected
      </td>

      <td style={{ textAlign: "left" }}>
        integer
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        ownerAddress
      </td>

      <td style={{ textAlign: "left" }}>
        token owner address in hex
      </td>

      <td style={{ textAlign: "left" }}>
        hexString
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        options
      </td>

      <td style={{ textAlign: "left" }}>
        The permission Id
      </td>

      <td style={{ textAlign: "left" }}>
        integer
      </td>
    </tr>
  </tbody>
</Table>

# Return

Object

# Example

```javascript
tronWeb.transactionBuilder.tradeExchangeTokens(1, "1000003",1000,1000,"410ca7c49aa44d26aabfe7f594c645cf9f17a4ff70",1).then(result => console.log(result));
>{
    "visible": false,
    "txID": "545ed6a5eb793fe5903ec177761b2504147e010875644fce321f0dbb28799456",
    "raw_data": {
        "contract": [
            {
                "parameter": {
                    "value": {
                        "exchange_id": 1,
                        "token_id": "31303030303033",
                        "expected": 1000,
                        "owner_address": "410ca7c49aa44d26aabfe7f594c645cf9f17a4ff70",
                        "quant": 1000
                    },
                    "type_url": "type.googleapis.com/protocol.ExchangeTransactionContract"
                },
                "type": "ExchangeTransactionContract"
            }
        ],
        "ref_block_bytes": "c778",
        "ref_block_hash": "db086b31f0f10f69",
        "expiration": 1581650238000,
        "timestamp": 1581650180365
    },
    "raw_data_hex": "0a02c7782208db086b31f0f10f6940b0b4cd8d842e5a68082c12640a38747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e45786368616e67655472616e73616374696f6e436f6e747261637412280a15410ca7c49aa44d26aabfe7f594c645cf9f17a4ff7010011a073130303030303320e80728e807708df2c98d842e"
}
```

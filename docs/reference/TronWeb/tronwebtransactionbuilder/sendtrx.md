---
title: sendTrx
excerpt: Creates an unsigned TRX transfer transaction
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Usage

```javascript
// Format
tronWeb.transactionBuilder.sendTrx(to, amount, from, options);
```

**Arguments**

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
        Type
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        to
      </td>

      <td>
        Address to send TRX to, converted to a hex string.
      </td>

      <td>
        hexString
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        Amount of TRX (**units in SUN**) to send.
      </td>

      <td>
        integer (**units in SUN**)
      </td>
    </tr>

    <tr>
      <td>
        from
      </td>

      <td>
        Optional address that is transferring the Tokens. If left blank, will use the address associated with the private key.
      </td>

      <td>
        hexString
      </td>
    </tr>

    <tr>
      <td>
        options
      </td>

      <td>
        The permissions Id
      </td>

      <td>
        integer
      </td>
    </tr>
  </tbody>
</Table>

# Return

Object

# Example

```javascript
tronWeb.transactionBuilder.sendTrx("TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr", 100, "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL");
>{
    "visible": false,
    "txID": "9f62a65d0616c749643c4e2620b7877efd0f04dd5b2b4cd14004570d39858d7e",
    "raw_data": {
        "contract": [
            {
                "parameter": {
                    "value": {
                        "amount": 100,
                        "owner_address": "418840e6c55b9ada326d211d818c34a994aeced808",
                        "to_address": "41d3136787e667d1e055d2cd5db4b5f6c880563049"
                    },
                    "type_url": "type.googleapis.com/protocol.TransferContract"
                },
                "type": "TransferContract"
            }
        ],
        "ref_block_bytes": "0add",
        "ref_block_hash": "6c2763abadf9ed29",
        "expiration": 1581308685000,
        "timestamp": 1581308626092
    },
    "raw_data_hex": "0a020add22086c2763abadf9ed2940c8d5deea822e5a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a15418840e6c55b9ada326d211d818c34a994aeced808121541d3136787e667d1e055d2cd5db4b5f6c880563049186470ac89dbea822e"
}
```

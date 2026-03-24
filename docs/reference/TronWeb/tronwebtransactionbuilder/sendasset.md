---
title: sendAsset
excerpt: Creates an unsigned TRC10 token transfer transaction
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
tronWeb.transactionBuilder.sendAsset(to, amount, tokenID, from, options);
```

# Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameters
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
        Address to send Token to.
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
        Amount of Token to send.
      </td>

      <td>
        integer
      </td>
    </tr>

    <tr>
      <td>
        tokenID
      </td>

      <td>
        ID of the token,
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        from
      </td>

      <td>
        Optional address that is transferring the Tokens.
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
        The permission Id
      </td>

      <td>
        integer
      </td>
    </tr>
  </tbody>
</Table>

# Return

**Object** 

# Example

```javascript
tronWeb.transactionBuilder.sendAsset("TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr", 100, "1000086", "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL");
>{
    "visible": false,
    "txID": "0de6f3f2178045456f907ad16c9c67096f47a0b0aee0beafbf9e76f47cce5e2a",
    "raw_data": {
        "contract": [
            {
                "parameter": {
                    "value": {
                        "amount": 100,
                        "asset_name": "31303030303836",
                        "owner_address": "418840e6c55b9ada326d211d818c34a994aeced808",
                        "to_address": "41d3136787e667d1e055d2cd5db4b5f6c880563049"
                    },
                    "type_url": "type.googleapis.com/protocol.TransferAssetContract"
                },
                "type": "TransferAssetContract"
            }
        ],
        "ref_block_bytes": "088e",
        "ref_block_hash": "78d48563585bc6e8",
        "expiration": 1581306912000,
        "timestamp": 1581306853656
    },
    "raw_data_hex": "0a02088e220878d48563585bc6e84080baf2e9822e5a730802126f0a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e736665724173736574436f6e747261637412390a07313030303038361215418840e6c55b9ada326d211d818c34a994aeced8081a1541d3136787e667d1e055d2cd5db4b5f6c88056304920647098f2eee9822e"
}
```

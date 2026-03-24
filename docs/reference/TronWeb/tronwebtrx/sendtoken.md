---
title: sendToken
excerpt: >-
  Sends TRC10 token from one address to another. Will create and broadcast the
  transaction if a private key is provided.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ❗️ WARNING
>
> Do not use this in any web / user-facing applications. This will expose the private key.

# Usage

```javascript
tronWeb.trx.sendToken();
```

# Parameters

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
        to
      </td>

      <td>
        Address to send TRX to.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        Amount of TRX to send.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        tokenID
      </td>

      <td>
        Name of the token, matching the exact capitalization.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        privateKey
      </td>

      <td>
        Optionally provide a private key to sign the transaction
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# Example

```json
//example1
tronWeb.trx.sendToken("TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr",1000,’100010’);

//example2 
tronWeb.trx.sendToken("TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr", 1000,’100010’,’from_address_private’);
{ result: true,
 transaction:
  { visible: false,
    txID:
     '7d3e08aed30e47d7f03062282ecaba9ac18164a5a2aa0830a6f4af8620c9b8ea',
    raw_data:
     { contract: [Array],
       ref_block_bytes: 'b4c2',
       ref_block_hash: '653e58b56f0a0c06',
       expiration: 1579076202000,
       timestamp: 1579076144747 },
    raw_data_hex:
     '0a02b4c22208653e58b56f0a0c064090dc9ac2fa2d5a730802126f0a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e736665724173736574436f6e747261637412390a07313030303030311215417946f66d0fc67924da0ac9936183ab3b07c811261a1541d3136787e667d1e055d2cd5db4b5f6c880563049200a70eb9c97c2fa2d',
    signature:
     [ '29d1db1203a3eb163b2602181cd77b1bbf1010bd66490b9f023d5cfbf22950892103ffefaf5c85d6894bd2baa27975d2ce456d121210a44a618791a2d36d82b301' ] } }
```

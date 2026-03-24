---
title: verifyMessageV2
excerpt: Verify the signature on a plaintext string
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The plaintext string can be signed through the [signMessageV2](https://developers.tron.network/reference/signmessagev2) interface, and then the signature can be verified through this interface.

# Usage

```javascript
// Call directly
TronWeb.Trx.verifyMessageV2(message, signature)

// Called via the instantiated tronWeb object
tronWeb.trx.verifyMessageV2(message, signature)
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
        message
      </td>

      <td>
        the signed string
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        signature
      </td>

      <td>
        Signature to be verified
      </td>

      <td>
        String
      </td>
    </tr>
  </tbody>
</Table>

# Returns

String - the signed address in base58 format

# Example

```javascript
var str = "helloworld"; 
var signature = await tronWeb.trx.signMessageV2(messge);
var base58Address = await tronWeb.trx.verifyMessageV2(messge, signature);
```

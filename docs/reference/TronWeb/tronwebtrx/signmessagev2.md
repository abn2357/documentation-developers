---
title: signMessageV2
excerpt: Sign a string
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
signMessageV2 can not only sign the Hex format string, but also sign a plaintext string. Please use the [verifyMessageV2](https://developers.tron.network/reference/verifymessagev2) interface for signature verification.

# Usage

```javascript
// Call directly，privatekey is needed in this way
TronWeb.Trx.signMessageV2(message, privateKey)

// Called via the instantiated tronWeb object
tronWeb.trx.signMessageV2(message, privateKey);
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
        Message to be signed
      </td>

      <td>
        Bytes / String
      </td>
    </tr>

    <tr>
      <td>
        privateKey
      </td>

      <td>
        The private key used for signing, optional parameter. Default to use the private key passed in when building tronweb object.
      </td>

      <td>
        String
      </td>
    </tr>
  </tbody>
</Table>

# Returns

String - the signature.

# Example

```javascript
var messge = 'hello world';
var signature = await tronWeb.trx.signMessageV2(messge);
console.log(signature);
>0x1d1b0779da653630d29fc4f1ea1e5a109a30d52e21e7657fa896d2fccc3b430b14089377e13b6ed35ef371a1c91873773d568219d1100fa8595e5f2eec39e3e41c
```

---
title: signMessageV1
excerpt: >-
  Sign a hex formatted string. Deprecated. Suggest to use signMessageV2 to sign
  a hex formatted string
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This interface is used to sign the Hex format string, and the signature verification uses [verifyMessage](https://developers.tron.network/reference/verifymessage) interface.

> ❗️ WARNING
>
> Do not use this in any web / user-facing applications. This will expose the private key.

# Usage

```javascript
// sign a Hex formatted string
tronWeb.trx.sign(str, privateKey)
```

# Input Parameters

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
        str
      </td>

      <td>
        Hex formatted string
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        privateKey
      </td>

      <td>
        The private key used for signing. Optional.  The default value is the private key passed in when constructing tronweb object.
      </td>

      <td>
        String
      </td>
    </tr>
  </tbody>
</Table>

# Example

```javascript
var str = "helloworld"; 
var HexStr = tronWeb.toHex(str);
var signedStr = await tronWeb.trx.sign(HexStr, privateKey);
console.log(signedStr)

>0xe89b777b011b678c9f52e464117f8a8a2193f2cb8d37cbb9e1bd7bd8905fb79046185ea458fab36ed387d60b0842b59b15c7a419797575986492d0271a91d9e71b
```

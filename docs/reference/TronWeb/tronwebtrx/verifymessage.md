---
title: verifyMessage
excerpt: >-
  verify signature of a hex formatted string. Deprecated, please use
  signMessageV2 and verifyMessageV2 to sign and verify strings
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
tronWeb.trx.verifyMessage(hexMsg, signedMsg, address)
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
        hexMsg
      </td>

      <td>
        hex formatted string
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        signedMsg
      </td>

      <td>
        signature of the string
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        address
      </td>

      <td>
        signature address(base58 or hex)
      </td>

      <td>
        String
      </td>
    </tr>
  </tbody>
</Table>

# Return

bool - true if verify successfully, else return error

# Example

```json
// sign a string message

var str = "helloworld"; 
// convert to hex format and remove the beginning "0x"
var hexStrWithout0x = tronWeb.toHex(str).replace(/^0x/, '');
// conert hex string to byte array
var byteArray = tronWeb.utils.code.hexStr2byteArray(hexStrWithout0x)
// keccak256 computing, then remove "0x" 
var strHash= tronWeb.sha3(byteArray).replace(/^0x/, '');
// sign 
var signedStr = await tronWeb.trx.sign(strHash).replace(/^0x/, '');
var tail = signedStr.substring(128, 130);
if(tail == '01')
{
    signedStr = signedStr.substring(0,128)+'1c';
}
else if(tail == '00')
{
  	signedStr = signedStr.substring(0,128)+'1b';
}
  

// verify the signature
var res = await tronWeb.trx.verifyMessage(strHash,signedStr,'TPNcZ1j55FrGpsaw6K6rVjuL4HfT8ZbBf7')
console.log(res);
>true
```

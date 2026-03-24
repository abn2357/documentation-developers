---
title: createRandom
excerpt: >-
  Generate a random mnemonic (total number 12) and using TRON path "m/44'/195'"
  by default, return the 0th account address and private key
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

```
// Call directly
TronWeb.createRandom()

// Called via the instantiated tronWeb object
tronWeb.createRandom()
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
        options
      </td>

      <td>
        Optional parameter with three fields:\
        path - BIP44 path\
        extraEntropy - entropy\
        locale - the locale
      </td>

      <td>
        Object
      </td>
    </tr>
  </tbody>
</Table>

# Returns

Object - Returns randomly created account information, including mnemonic, public key, and private key. If the entered BIP44 path does not start with `m/44'/195'`, throw an exception - Error: Invalid tron path provided.

# Example

Example 1

```javascript
>tronWeb.createRandom()
{
  "mnemonic": {
    "phrase": "chimney cloth deny claim play rude love dose apart shove rack stone",
    "path": "m/44'/195'/0'/0/0",
    "locale": "en"
  },
  "privateKey": "0x79092289f3bfde55f079202e3642b2c4ba071d5f0b85d65b1919c8724e94848c",
  "publicKey": "0x0421c47d627bc2d856760dda17b42b726b4bc8f5def76aed0cbcd71566d0ffedfc3904c9c854854a5019b8373d2aed0c6b96ff5f3be07722403088742b0949a6c9",
  "address": "TEFAyPnainfiAJBuhExfMLJeHHxD2DZJmF",
}
```

Example 2

```javascript
>tronWeb.createRandom({path: "m/44'/195'/0'/0/0", extraEntropy: '', locale: 'en'})
{
  mnemonic: {
    phrase: 'dinosaur lemon cause answer push accuse small blind oak abandon afraid record',
    path: "m/44'/195'/0'/0/0",
    locale: 'en'
  },
  privateKey: '0xa067d2f82f5f3de0bd95eedf3c3cfb6c01b6a78e9ceaf7a806afe253afa06b71',
  publicKey: '0x04c09f023b2cb459402126db9432aa16d524501ec62fff73c51fba6c5e44529499e817783abc06484ea1f8217bf61d1670704ca21b07c127cb36a9d2146df59f8d',
  address: 'TXBNANG5bmRt2wN5c94jQfUySLGjms2DCX'
}

```

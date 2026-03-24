---
title: verifyTypedData
excerpt: >-
  Verify the signature of the typed data `value` with `types` data structure for
  `domain` using the [TIP-712
  specification](https://github.com/tronprotocol/tips/issues/443).
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
tronWeb.trx.verifyTypedData(domain, types, value, signature, address);
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
        domain
      </td>

      <td>
        Domain separator. This field is to prevent collisions with other transactions on the network or messages with the same structure.
      </td>

      <td>
        JSON
      </td>
    </tr>

    <tr>
      <td>
        types
      </td>

      <td>
        Type definition of Typed Data
      </td>

      <td>
        JSON
      </td>
    </tr>

    <tr>
      <td>
        value
      </td>

      <td>
        The value of Typed Data
      </td>

      <td>
        JSON
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

    <tr>
      <td>
        address
      </td>

      <td>
        Signed account address (Base58 format or Hex format)
      </td>

      <td>
        String
      </td>
    </tr>
  </tbody>
</Table>

# Return

bool - true if verify successfully, else return error `Signature does not match`.

# Example

```javascript
// All properties on a domain are optional
const domain = {
  name: 'TRON Mail',
  version: '1',
  chainId: '0x2b6653dc',
  verifyingContract: 'TUe6BwpA7sVTDKaJQoia7FWZpC9sK8WM2t'
};

// The named list of all type definitions
const types = {
  Person: [
    { name: 'name', type: 'string' },
    { name: 'wallet', type: 'address' }
  ],
  Mail: [
    { name: 'from', type: 'Person' },
    { name: 'to', type: 'Person' },
    { name: 'contents', type: 'string' }
  ]
};

// The data to sign
const value = {
  from: {
    name: 'Cow',
    wallet: 'TUg28KYvCXWW81EqMUeZvCZmZw2BChk1HQ'
  },
  to: {
    name: 'Bob',
    wallet: 'TT5rFsXYCrnzdE2q1WdR9F2SuVY59A4hoM'
  },
  contents: 'Hello, Bob!'
};

const signature = await tronWeb.trx._signTypedData(domain, types, value);

const result = await tronWeb.trx.verifyTypedData(domain, types, value, signature);
// verification result: true
```

---
title: fromMnemonic
excerpt: Obtain the address and private key according to the provided mnemonic
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
TronWeb.fromMnemonic()

// Called via the instantiated tronWeb object
tronWeb.fromMnemonic()
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
        mnemonic
      </td>

      <td>
        mnemonic. Separate each mnemonic with a space.
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        path
      </td>

      <td>
        BIP44 path, optional parameter. If you want to get an account other than index 0, you need to fill in this parameter, and the complete path is required.
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        wordlist
      </td>

      <td>
        Language type, optional parameter. If the incoming mnemonic is not english(en), you need to fill in the corresponding language type through this parameter, such as zh, ja, it, ...
      </td>

      <td>
        String
      </td>
    </tr>
  </tbody>
</Table>

# Returns

Object - Returns the obtained account information, including mnemonic, public key, and private key. If the entered BIP44 path does not start with `m/44'/195'`, throw an exception - Error: Invalid tron path provided.

# Example

Example 1

```javascript
>tronWeb.fromMnemonic( 'patch left empty genuine rain normal syrup yellow consider moon stock denial')
{
  mnemonic: {
    phrase: 'patch left empty genuine rain normal syrup yellow consider moon stock denial',
    path: "m/44'/195'/0'/0/0",
    locale: 'en'
  },
  privateKey: '0x0f9148e9be0c5b0213607a6491603891241ec7aa204918018dba691e4269ffe7',
  publicKey: '0x04642b796ba0acf06233e65695b977d28d2cae90fabd70dc0a300a831866b8f46ce5ee0ffa832492ce1b55a6c90463b2a31a03729b212281f6531558145b634ee0',
  address: 'TPiD26cc1vptLxwYmw4waHTPCNgqtZ5SCX'
}

```

Example 2

```javascript
>tronWeb.fromMnemonic( 'patch left empty genuine rain normal syrup yellow consider moon stock denial',"m/44'/195'/0'/0/1")
{
  mnemonic: {
    phrase: 'patch left empty genuine rain normal syrup yellow consider moon stock denial',
    path: "m/44'/195'/0'/0/1",
    locale: 'en'
  },
  privateKey: '0x5f3ecfca6e51dc70d58bca89d9b8fcb60cf193e0d8943af62311136c3e6504a0',
  publicKey: '0x04df45411faa27c933e10c83305da6f15138a018d2b539d8d4155a7e15f2552f9de3c6a7993e3814b4022a673faa70ad137bcc65857fc40cc0d59218ce28002361',
  address: 'TXzMaz1QU4jKLctDu2QibrWvPtogtYHdW7'
}


```

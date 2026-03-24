---
title: signTransaction
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
## signTransaction(transaction\[, callback])

Signing the raw transaction or message.

* `transaction`  &lt;Object&gt; | &lt;String&gt; The raw transaction or message.

* `privateKey`  &lt;String&gt; The signer's private key.

* `useTronHeader` &lt;Boolean&gt; Use Tron message header. Default: `true`.

* `multisig`  &lt;Boolean&gt; Use multi-sign if set true . Default: `false`.

* `callback`  &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance.

Example:

```js
// Example 1
const transaction = await tronWeb.sidechain.transactionBuilder.freezeBalance(10e5);
const signedTransaction = await tronWeb.sidechain.signTransaction(transaction);
console.log(signedTransaction);
/*
  output:
  {
    visible: false,
    txID: '38fe27104a5a6621345bd178178c3893615282e8b369d3a1d1221d92e4eff792',
    raw_data: {
      contract: [
        {
          parameter: {
            value: {
              frozen_duration: 3,
              frozen_balance: 1000000,
              owner_address: '41d6e0b756afc9cabbc9b880edcccf22078f45df5d'
            },
            type_url: 'type.googleapis.com/protocol.FreezeBalanceContract'
          },
          type: 'FreezeBalanceContract'
        }
      ],
      ref_block_bytes: '948f',
      ref_block_hash: 'a38650d7b9e4d165',
      expiration: 1591876059000,
      timestamp: 1591876000747
    },
    raw_data_hex: '0a0294...99aa2e',
    signature: ['f2c4b9...298601']
  }
*/

// Example 2
const message = tronWeb.toHex('message');
const signedString = await tronWeb.sidechain.signTransaction(message);
console.log(signedString);
// output: 0xe81256...1c071b
```
---
title: multiSign
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
## multiSign(transaction\[, callback])

Multi-Signing the raw transaction.

* `transaction` \<Object> The raw transaction.

* `privateKey` \<String> The signer's private key.

* `permissionId` \<Number> Specifies which permission to use. Default: `0`.

* `callback` \<Function>

Returns \<Promise> If no callback was passed it returns a Promise instance.

Example:

```js
const transaction = await tronWeb.sidechain.transactionBuilder.freezeBalance(10e5);
const signedTransaction = await tronWeb.sidechain.multiSign(transaction);
console.log(signedTransaction);
/*
  output:
  {
    visible: false,
    txID: '26915da94483642dd63a0dd25aec3bfff6266e49ac0dddfdcce4e3cd819e8d55',
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
      ref_block_bytes: '94cf',
      ref_block_hash: '29419bda0a6c1b22',
      expiration: 1591876251000,
      timestamp: 1591876193147
    },
    raw_data_hex: '0a0294...99aa2e',
    signature: ['c83032...84ea00']
  }
*/
```

---
title: Creating Transaction using Different Account Permissions
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Developers can send transactions easily using SDKs. This article will take the account `TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ` as an example to explain how to create a transfer transaction using different account permissions on the Nile test network with the TronWeb SDK.

The steps for creating a transaction involving different account permissions are as follows (Note: If your account's permission has already been modified, you can go to Step 3 directly):

1. [Modify Account Permission](#1-modify-account-permission)
2. [Query Account Permission](#2-query-account-permission)
3. [Select Permission and Create Transaction](#3-select-permission-and-create-transaction)
4. [Sign Transaction with Permissioned Accounts](#4-sign-the-transaction-by-the-accounts-which-have-the-permission)
5. [Check Transaction's Signature Weight](#5-check-transactions-sign-weight)
6. [Check Approved List](#6-check-approved-list)
7. [Broadcast Transaction](#7-broadcast-transaction)

## 1. Modify Account Permission

Modify the account permission on TRONSCAN or using the [wallet/accountpermissionupdate](https://developers.tron.network/reference/accountpermissionupdate) API. In this example, an active permission named "NewAddedActivePermission" is added to the account `TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ` on TRONSCAN.

## 2. Query Account Permission

Use the [wallet/getaccount](https://developers.tron.network/reference/account-getaccount) API to query account permission settings:

```
curl --location --request POST 'https://api.nileex.io/wallet/getaccount' \
--header 'Content-Type: text/plain' \
--data-raw '{
     "address": "TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ",
     "visible": true
}'
```

Returns:

```
{
    "address": "TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ",
    "balance": 2897800000,
    ......
    "owner_permission": {
        "permission_name": "owner",
        "threshold": 1,
        "keys": [
            {
                "address": "TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ",
                "weight": 1
            }
        ]
    },
    "active_permission": [
        {
            "type": "Active",
            "id": 2,
            "permission_name": "active",
            "threshold": 1,
            "operations": "7fff1fc0033efb0f000000000000000000000000000000000000000000000000",
            "keys": [
                {
                    "address": "TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ",
                    "weight": 1
                }
            ]
        },
        {
            "type": "Active",
            "id": 3,
            "permission_name": "NewAddedActivePermission",
            "threshold": 2,
            "operations": "77ff07c00260c30f000000000000000000000000000000000000000000000000",
            "keys": [
                {
                    "address": "TXTMqofe9nS5bN5tfhfd6ayWocJm7oxJKT",
                    "weight": 1
                },
                {
                    "address": "TVqTEPUPiTxhzaSnD9xXEvarUQooLibkXM",
                    "weight": 1
                }
            ]
        }
    ],
    ......
}
```

From the returned result, we can see that the account `TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ` has an active permission with id set to 3 and the threshold of 2, and the permission is authorized to two accounts, with the weight of each account set to 1.

## 3. Select Permission and Create Transaction

In this example, we use the active permission with `id = 3` of `TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ` to construct a TRX transfer transaction through the [tronWeb.transactionBuilder.sendTrx](https://developers.tron.network/reference/sendtrx) method:

```
var unsignedTransaction = await tronWeb.transactionBuilder.sendTrx('TVqTEPUPiTxhzaSnD9xXEvarUQooLibkXM', 10000000, 'TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ',{permissionId: 3});
```

* **Sender**: the `owner_address` in the transaction, which is `TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ` in this example. When building a transaction, you don't need to pay special attention to the transaction creator; just set the TRX sender in the transaction to the account address:  `TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ`.
* **Permission**: Select the active permission with `id = 3` of `TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ` - `{permissionId: 3}`

## 4. Sign Transaction with Permissioned Accounts

The active permission of `TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ` with `id = 3` is authorized to `TXTMqofe9nS5bN5tfhfd6ayWocJm7oxJKT` and `TVqTEPUPiTxhzaSnD9xXEvarUQooLibkXM`. These two accounts can use the [tronWeb.trx.multiSign](https://developers.tron.network/reference/multisign) API to sign the transaction:

```
// Sign with the first private key
var signedTransaction = await tronWeb.trx.multiSign(unsignedTransaction, 'f0bd085a...ac479f74'); // Private Key, hex, 64 characters total

// Sign with the second private key
signedTransaction = await tronWeb.trx.multiSign(signedTransaction, '6c72f51d...d726edc'); // Private Key, hex, 64 characters total
```

Returns:

```
{
  visible: false,
  txID: '507efa43ef267005cd384f74f8bc2b2d6e807807144144fd01f194f36ddfb93a',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: 'e5b2',
    ref_block_hash: 'c565570704ef1e7a',
    expiration: 1700538150000,
    timestamp: 1700538091138
  },
  raw_data_hex: '0a02e5b22208c565570704ef1e7a40f0d8e3ffbe315a6a080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a1541cbe603e1f0ac26c50bb795d8d54a95706c64b2e2121541d9eb1101ba37f55c436cc668ed1ac18d23d6c6631880ade204280370828de0ffbe31',
  signature: [
    '9f51d0839b8dd10b5a6bc3b043f6246d5c8a00a79839a52b0987ee337911b3375d0376c3b1aef3a7ffa0779a2e3d0cb95380294e6b934f738964a0551675d45501',
    '2bc656a647cbd9de932bf63909f73aacf2e97f0c771bd72b69654f6242a152e8ecbc8712ad59fe95a280cffbed5ef2dd28777dc27267976fe0c6374e00ba355c01'
  ]
}


```

## 5. Check Transaction's Signature Weight

With the [`tronweb.trx.getSignWeight`](https://developers.tron.network/reference/getsignweight) method, you can not only check the weight required by the used permission, but also how many addresses have signed the transaction and the corresponding sum weight. The method can be called during or after the entire transaction signing process.

```
var signWeight = await tronWeb.trx.getSignWeight(signedTransaction);
```

Returns:

```
{
  result: {},
  approved_list: [
    '41d9eb1101ba37f55c436cc668ed1ac18d23d6c663',
    '41ebadab040181bcc649169d00c28a3ad1bb6bfeb7'
  ],
  permission: {
    operations: '77ff07c00260c30f000000000000000000000000000000000000000000000000',
    keys: [ [Object], [Object] ],
    threshold: 2,
    id: 3,
    type: 'Active',
    permission_name: 'NewAddedActivePermission'
  },
  current_weight: 2,
  transaction: {
    result: { result: true },
    txid: '507efa43ef267005cd384f74f8bc2b2d6e807807144144fd01f194f36ddfb93a',
    transaction: {
      signature: [Array],
      txID: '507efa43ef267005cd384f74f8bc2b2d6e807807144144fd01f194f36ddfb93a',
      raw_data: [Object],
      raw_data_hex: '0a02e5b22208c565570704ef1e7a40f0d8e3ffbe315a6a080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a1541cbe603e1f0ac26c50bb795d8d54a95706c64b2e2121541d9eb1101ba37f55c436cc668ed1ac18d23d6c6631880ade204280370828de0ffbe31'
    }
  }
}


```

## 6. Check Approved List

You can also view the list of accounts that have signed the transaction through [tronWeb.trx.getApprovedList](https://developers.tron.network/reference/getapprovedlist).

```
var approvedList = await tronWeb.trx.getApprovedList(signedTransaction);
```

Returns:

```
{
  result: {},
  approved_list: [
    '41d9eb1101ba37f55c436cc668ed1ac18d23d6c663',
    '41ebadab040181bcc649169d00c28a3ad1bb6bfeb7'
  ],
  transaction: {
    result: { result: true },
    txid: '507efa43ef267005cd384f74f8bc2b2d6e807807144144fd01f194f36ddfb93a',
    transaction: {
      signature: [Array],
      txID: '507efa43ef267005cd384f74f8bc2b2d6e807807144144fd01f194f36ddfb93a',
      raw_data: [Object],
      raw_data_hex: '0a02e5b22208c565570704ef1e7a40f0d8e3ffbe315a6a080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a1541cbe603e1f0ac26c50bb795d8d54a95706c64b2e2121541d9eb1101ba37f55c436cc668ed1ac18d23d6c6631880ade204280370828de0ffbe31'
    }
  }
}

```

## 7. Broadcast Transaction

After the required signatures are collected, you can broadcast the signed transaction directly and later check it through  `getTransactionById`.

```
var result = await tronWeb.trx.broadcast(signedTransaction);
```

Returns:

```
{
  result: true,
  txid: '507efa43ef267005cd384f74f8bc2b2d6e807807144144fd01f194f36ddfb93a',
  transaction: {
    visible: false,
    txID: '507efa43ef267005cd384f74f8bc2b2d6e807807144144fd01f194f36ddfb93a',
    raw_data: {
      contract: [Array],
      ref_block_bytes: 'e5b2',
      ref_block_hash: 'c565570704ef1e7a',
      expiration: 1700538150000,
      timestamp: 1700538091138
    },
    raw_data_hex: '0a02e5b22208c565570704ef1e7a40f0d8e3ffbe315a6a080112640a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412330a1541cbe603e1f0ac26c50bb795d8d54a95706c64b2e2121541d9eb1101ba37f55c436cc668ed1ac18d23d6c6631880ade204280370828de0ffbe31',
    signature: [
      '9f51d0839b8dd10b5a6bc3b043f6246d5c8a00a79839a52b0987ee337911b3375d0376c3b1aef3a7ffa0779a2e3d0cb95380294e6b934f738964a0551675d45501',
      '2bc656a647cbd9de932bf63909f73aacf2e97f0c771bd72b69654f6242a152e8ecbc8712ad59fe95a280cffbed5ef2dd28777dc27267976fe0c6374e00ba355c01'
    ]
  }
}

```

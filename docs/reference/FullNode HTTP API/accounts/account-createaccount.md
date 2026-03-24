---
title: CreateAccount
excerpt: >-
  Activate an account. Address generation (i.e., creating a public/private key
  pair) can be done offline using tools such as Wallet-CLI or TRON SDKs like
  TronWeb. After generating the key pair, this API can be used to activate the
  account on-chain.  It is important to note that the most common way to
  activate an account is by transferring any amount of TRX to it. Therefore, you
  may explicitly activate the account by calling this API, or transferring TRX
  to the account.
api:
  file: full-node-http-api.json
  operationId: account-createaccount
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Returns**

Transaction - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `AccountCreateContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field           | Type   | Description                                   |
| :-------------- | :----- | :-------------------------------------------- |
| owner_address   | string | Transaction initiator address.                |
| account_address | string | Account address to be activated.              |
| type            | int    | Account type (e.g., 0 for external accounts). |

> 📘 Note
>
> * The expiration time for transactions created via the HTTP API is 1 minute.
>
>   To ensure the transaction is successfully recorded on-chain, please complete the signing and broadcasting within 1 minute of its creation.
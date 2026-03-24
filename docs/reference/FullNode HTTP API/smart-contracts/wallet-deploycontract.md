---
title: DeployContract
excerpt: >-
  Deploys a contract. Returns TransactionExtention, which contains an unsigned
  transaction.
api:
  file: full-node-http-api.json
  operationId: wallet-deploycontract
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

Returned Object: Transaction (Unsigned).

General Fields: Refer to the [Transaction](/docs/tron-protocol-transaction) section.

`CreateSmartContract` Specific Fields: The `raw_data.contract[0].parameter.value` within the transaction contains parameters for the contract invocation:

| Field            | Type          | Description                                                                                                                      |
| :--------------- | :------------ | :------------------------------------------------------------------------------------------------------------------------------- |
| owner_address    | string        | Transaction initiator address.                                                                                                   |
| new_contract     | SmartContract | Data of the deployed smart contract. See [GetContract](https://developers.tron.network/reference/wallet-getcontract) for fields. |
| call_token_value | int64         | The amount of TRC-10 transferred into the contract                                                                               |
| token_id         | int64         | TRC-10 token id                                                                                                                  |

<br />
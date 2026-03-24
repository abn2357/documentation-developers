---
title: GetTransactionById
excerpt: Query transaction information by transaction id
api:
  file: full-node-http-api.json
  operationId: wallet-gettransactionbyid
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: ''
  description: ''
  robots: index
---
**Returns**

The interface returns a Transaction object, which contains the following fields:

<br />

| Field           | Type        | Description                                                                                                       |
| :-------------- | :---------- | :---------------------------------------------------------------------------------------------------------------- |
| txID            | String      | Transaction ID(Hash).                                                                                             |
| ret.contractRet | string[]    | Transaction Execution Results.                                                                                    |
| signature       | string[]    | Transaction signature.                                                                                            |
| raw_data_hex    | string      | The transaction's raw data. (Format: hex)                                                                         |
| raw_data        | Transaction | Transaction content. See [here](https://developers.tron.network/docs/tron-protocol-transaction)  for details.     |
| fee_limit       | Long        | The transaction's `FeeLimit`. See [here](https://developers.tron.network/docs/feelimit)  for details. (Unit: sun) |
| ref_block_bytes | String      | The last two bytes of the reference block's number (height), used for transaction validation.                     |
| ref_block_hash  | String      | Bytes 8 to 16 of the reference block's hash, used for transaction validation.                                     |
| expiration      | Long        | Transaction expiration time. (Unit: millisecond)                                                                  |
| timestamp       | Long        | The block timestamp. (Unit: millisecond)                                                                          |
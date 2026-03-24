---
title: GetBlock
excerpt: >-
  Queries block header information or entire block information according to
  block height or block hash. (Confirmed state)
api:
  file: full-node-http-api.json
  operationId: getblock-2
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

| Field                                  | Type          | Description                                                                                                                                                               |
| :------------------------------------- | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `blockID`                              | string        | Block hash.                                                                                                                                                               |
| `block_header.raw_data.timestamp`      | int64         | Block timestamp. (Unit: millisecond)                                                                                                                                      |
| `block_header.raw_data.txTrieRoot`     | string        | Root hash of the transaction Merkle tree.                                                                                                                                 |
| `block_header.raw_data.parentHash`     | string        | Hash of the parent block.                                                                                                                                                 |
| `block_header.raw_data.number`         | int64         | Block number (height).                                                                                                                                                    |
| `block_header.raw_data.witness_id`     | int64         | ID of the Super Representative.                                                                                                                                           |
| `block_header.raw_data.witness_address`| string        | Address of the Super Representative that produced the block.                                                                                                              |
| `block_header.raw_data.version`        | int32         | Protocol version number.                                                                                                                                                  |
| `block_header.raw_data.accountStateRoot`| string        | Root hash of the account state tree.                                                                                                                                      |
| `block_header.witness_signature`       | string        | Signature of the Super Representative.                                                                                                                                    |
| `transactions`                         | Transaction[] | List of transaction objects in the block. See [GetTransactionById](https://developers.tron.network/reference/wallet-gettransactionbyid) for contents in each transaction. |
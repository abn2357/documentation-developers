---
title: GetBlockBalance
excerpt: >-
  Get all balance change operations in a block. (Note: This API requires the
  node to enable the historical balance query feature. When using official
  nodes, the interface is currently available only on the following nodes:
  13.228.119.63, 18.139.193.235, 18.141.79.38, and 18.139.248.26.)
api:
  file: full-node-http-api.json
  operationId: getblockbalance
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

| Field                     | Type                      | Description                                           |
| :------------------------ | :------------------------ | :---------------------------------------------------- |
| timestamp                 | int64                     | Timestamp. (Unit: millisecond)                        |
| block_identifier.hash     | string                    | Block hash.                                           |
| block_identifier.number   | int64                     | Block number.                                         |
| transaction_balance_trace | TransactionBalanceTrace[] | List of transaction information with balance changes. |

The fields contained in the TransactionBalanceTrace object are as follows:

| Field                  | Type        | Description                                                                                                                                                                                                                                                        |
| :--------------------- | :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| transaction_identifier | string      | Transaction ID (hash).                                                                                                                                                                                                                                             |
| operation              | Operation[] | List of balance change operations in this transaction, including sender deductions, receiver additions, and resource fee burns (Bandwidth/Energy). Each item contains `operation_identifier` (index), `address` (affected address), and `amount` (balance change). |
| type                   | string      | Transaction type.                                                                                                                                                                                                                                                  |
| status                 | string      | Transaction result status.                                                                                                                                                                                                                                         |
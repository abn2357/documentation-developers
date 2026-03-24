---
title: eth_getBlockByHash
excerpt: Fetches the block object associated with the provided hash.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
**Parameters**

1. `DATA`, 32 Bytes - Block Hash.
2. `Boolean` - Returns full transaction details if `true`, or only hashes if `false`.

**Returns**

* `Object` - The return value is a block object (see schema below) or null if the block does not exist. The object includes the following items:

  | Item Name          | Data Type         | Description                                                                             |
  | :----------------- | :---------------- | :-------------------------------------------------------------------------------------- |
  | `number`           | `QUANTITY`        | Block number.                                                                           |
  | `hash`             | `DATA`, 32 Bytes  | Block hash.                                                                             |
  | `parentHash`       | `DATA`, 32 Bytes  | Parent block hash.                                                                      |
  | `nonce`            | `QUANTITY`        | This field is not used.                                                                 |
  | `sha3Uncles`       | `DATA`, 32 Bytes  | SHA3 hash of the block's uncle's data.                                                  |
  | `logsBloom`        | `DATA`, 256 Bytes | Block log Bloom filter.                                                                 |
  | `transactionsRoot` | `DATA`, 32 Bytes  | The root of the transaction trie for the block.                                         |
  | `stateRoot`        | `DATA`, 32 Bytes  | The root of the final state trie for the block.                                         |
  | `receiptsRoot`     | `DATA`, 32 Bytes  | The root of the receipts trie for the block.                                            |
  | `miner`            | `DATA`, 20 Bytes  | The address of the beneficiary who received the mining rewards.                         |
  | `difficulty`       | `QUANTITY`        | Block difficulty (integer).                                                             |
  | `totalDifficulty`  | `QUANTITY`        | The total difficulty of the chain up to this block, represented as an integer.          |
  | `extraData`        | `DATA`            | The “extra data” of this block.                                                         |
  | `size`             | `QUANTITY`        | Block size in bytes (integer).                                                          |
  | `gasLimit`         | `QUANTITY`        | The maximum gas allowed in this block                                                   |
  | `gasUsed`          | `QUANTITY`        | Total gas used by all transactions in this block.                                       |
  | `timestamp`        | `QUANTITY`        | Block creation time (Unix timestamp in seconds).                                        |
  | `transactions`     | `Array`           | Array of transaction objects or 32-byte hashes, contingent on the last input parameter. |
  | `uncles`           | `Array`           | Array of uncle hashes.                                                                  |

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"method": "eth_getBlockByHash",
	"params": ["0x0000000000f9cc56243898cbe88685678855e07f51c5af91322c225ce3693868", false],
	"id": 1
}'
```

Response

```json
{"jsonrpc":"2.0","id":1,"result":null}
```

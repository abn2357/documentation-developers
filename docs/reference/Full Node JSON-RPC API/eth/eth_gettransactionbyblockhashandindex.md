---
title: eth_getTransactionByBlockHashAndIndex
excerpt: >-
  Returns information about a transaction by block hash and transaction index
  position.
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

1. `DATA`, 32 Bytes - Hash of a block.
2. `QUANTITY` - Transaction index position.

**Returns**

* `Object` - A transaction object or `null` when no transaction was found. The transaction includes items as below:

  | Item Name          | Data Type        | Description                                              |
  | :----------------- | :--------------- | :------------------------------------------------------- |
  | `blockHash`        | `DATA`, 32 Bytes | Hash of the block where this transaction was in.         |
  | `blockNumber`      | `QUANTITY`       | Block number where this transaction was in.              |
  | `from`             | `DATA`, 20 Bytes | Address of the sender.                                   |
  | `gas`              | `QUANTITY`       | Unused.                                                  |
  | `gasPrice`         | `QUANTITY`       | Energy price.                                            |
  | `hash`             | `DATA`, 32 Bytes | Hash of the transaction.                                 |
  | `input`            | `DATA`           | Data sent along with the transaction.                    |
  | `nonce`            | `QUANTITY`       | Unused.                                                  |
  | `to`               | `DATA`, 20 Bytes | Address of the receiver.                                 |
  | `transactionIndex` | `QUANTITY`       | Integer of the transactions index position in the block. |
  | `value`            | `QUANTITY`       | Value transferred in sun.                                |
  | `v`                | `QUANTITY`       | ECDSA recovery ID.                                       |
  | `r`                | `DATA`, 32 Bytes | ECDSA signature `r`.                                     |
  | `s`                | `DATA`, 32 Bytes | ECDSA signature `s`.                                     |

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"method": "eth_getTransactionByBlockHashAndIndex",
	"params": ["00000000020ef11c87517739090601aa0a7be1de6faebf35ddb14e7ab7d1cc5b", "0x0"],
	"id": 64
}'
```

Response

```json
{
	"jsonrpc": "2.0",
	"id": 64,
	"result": {
		"blockHash": "0x00000000020ef11c87517739090601aa0a7be1de6faebf35ddb14e7ab7d1cc5b",
		"blockNumber": "0x20ef11c",
		"from": "0xb4f1b6e3a1461266b01c2c4ff9237191d5c3d5ce",
		"gas": "0x0",
		"gasPrice": "0x8c",
		"hash": "0x8dd26d1772231569f022adb42f7d7161dee88b97b4b35eeef6ce73fcd6613bc2",
		"input": "0x",
		"nonce": null,
		"r": "0x6212a53b962345fb8ab02215879a2de05f32e822c54e257498f0b70d33825cc5",
		"s": "0x6e04221f5311cf2b70d3aacfc444e43a5cf14d0bf31d9227218efaabd9b5a812",
		"to": "0x047d4a0a1b7a9d495d6503536e2a49bb5cc72cfe",
		"transactionIndex": "0x0",
		"type": "0x0",
		"v": "0x1b",
		"value": "0x203226"
	}
}
```

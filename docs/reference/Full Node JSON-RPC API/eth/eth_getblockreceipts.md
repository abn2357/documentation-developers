---
title: eth_getBlockReceipts
excerpt: Queries all transaction receipts contained in a specified block.
deprecated: false
hidden: false
metadata:
  robots: index
---
**Parameters**

1. `DATA`, 32 Bytes - The block identifier, which can be a block number(hex string), a block hash (with or without `0x` prefix), a hexadecimal block number, or a block tag ("latest", "earliest", "finalized").

**Returns**

* `Object` - A list of transaction receipts contained in the block. For the fields of each transaction receipt, please refer to [eth_gettransactionreceipt](/reference/eth_gettransactionreceipt).

  **Note**: For the genesis block, pruned blocks by LiteFullNode, or blocks that have not yet been produced, the API returns `null`.

**Example**

Request

```curl
# query by blockNumber
curl --location 'https://api.shasta.trongrid.io/jsonrpc' \
--header 'Content-Type: application/json' \
--data '{   "method":"eth_getBlockReceipts",
   "params":["0x377a8a2"],
   "id":1,
   "jsonrpc":"2.0"
}'

# query by blockHash
curl --location 'https://api.shasta.trongrid.io/jsonrpc' \
--header 'Content-Type: application/json' \
--data '{   "method":"eth_getBlockReceipts",
   "params":["00000000049e470616a96ca7af19fc46a473e9733796960d840697dd70ac14ad"],
   "id":1,
   "jsonrpc":"2.0"
}'

#query by tag
curl --location 'https://api.shasta.trongrid.io/jsonrpc' \
--header 'Content-Type: application/json' \
--data '{   "method":"eth_getBlockReceipts",
   "params":["latest"],
   "id":1,
   "jsonrpc":"2.0"
}'


```

Response

```json
{
	"jsonrpc": "2.0",
	"id": 64,
	"result": [{
		"blockHash": "0x00000000020ef11c87517739090601aa0a7be1de6faebf35ddb14e7ab7d1cc5b",
		"blockNumber": "0x20ef11c",
		"contractAddress": null,
		"cumulativeGasUsed": "0x646e2",
		"effectiveGasPrice": "0x8c",
		"from": "0x6eced5214d62c3bc9eaa742e2f86d5c516785e14",
		"gasUsed": "0x0",
		"logs": [],
		"logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
		"status": "0x1",
		"to": "0x0697250b9d73b460a9d2bbfd8c4cacebb05dd1f1",
		"transactionHash": "0xc9af231ad59bcd7e8dcf827afd45020a02112704dce74ec5f72cb090aa07eef0",
		"transactionIndex": "0x6",
		"type": "0x0"
  }]
}
```
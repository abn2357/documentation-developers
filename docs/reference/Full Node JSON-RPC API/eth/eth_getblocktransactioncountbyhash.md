---
title: eth_getBlockTransactionCountByHash
excerpt: >-
  Returns the number of transactions in a block from a block matching the given
  block hash.
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

**Returns**

* `QUANTITY` - Integer of the number of transactions in this block.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "eth_getBlockTransactionCountByHash",
	"params": ["0x00000000020ef11c87517739090601aa0a7be1de6faebf35ddb14e7ab7d1cc5b"]
}'
```

Response

```json
{"jsonrpc":"2.0","id":1,"result":"0x39"}
```

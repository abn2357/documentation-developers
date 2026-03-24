---
title: eth_getTransactionByBlockNumberAndIndex
excerpt: >-
  Returns information about a transaction by block number and transaction index
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

1. `QUANTITY|TAG` - Block number, or the string "earliest", "latest".
2. `QUANTITY` - Transaction index position.

**Returns**

* `object` - a transaction object or null when no transaction was found. See [eth_getTransactionByBlockHashAndIndex](https://developers.tron.network/reference#eth_gettransactionbyblockhashandindex)

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"method": "eth_getTransactionByBlockNumberAndIndex",
	"params": ["0xfb82f0", "0x0"],
	"id": 64
}'
```

Response

```json
{"jsonrpc":"2.0","id":64,"result":null}
```

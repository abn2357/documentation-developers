---
title: eth_getBlockTransactionCountByNumber
excerpt: Returns the number of transactions in a block matching the given block number.
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

1. `QUANTITY|TAG` - Integer of a block number, or the string "earliest" or "latest".

**Returns**

* `QUANTITY` - Integer of the number of transactions in this block.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"method": "eth_getBlockTransactionCountByNumber",
	"params": ["0xF96B0F"],
	"id": 1
}'
```

Result

```json
{"jsonrpc":"2.0","id":1,"result":"0x23"}
```

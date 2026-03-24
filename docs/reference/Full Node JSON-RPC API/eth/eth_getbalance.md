---
title: eth_getBalance
excerpt: Returns the balance of the provided account address.
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

1. `DATA`, 20 Bytes - Target account address for balance inquiry.
2. `QUANTITY` - Block number; currently, only "latest" is supported.

**Returns**

* `QUANTITY` - Integer of the current balance. (Unit: sun)

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"method": "eth_getBalance",
	"params": ["0x41f0cc5a2a84cd0f68ed1667070934542d673acbd8", "latest"],
	"id": 64
}'
```

Response

```json
{"jsonrpc":"2.0","id":64,"result":"0x492780"}
```

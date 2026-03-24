---
title: eth_getCode
excerpt: Returns runtime code of a given smart contract address.
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

1. `DATA`, 20 Bytes - Contract address.
2. `QUANTITY|TAG` - Block number; currently, only "latest" is supported.

**Returns**

* `DATA` - The runtime code from the given address.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"method": "eth_getCode",
	"params": ["0x4170082243784DCDF3042034E7B044D6D342A91360", "latest"],
	"id": 64
}'
```

Response

```json
{"jsonrpc":"2.0","id":64,"result":"0x"}
```

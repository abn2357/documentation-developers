---
title: eth_getWork
excerpt: Returns the hash of the current block.
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
None

**Returns**

* `Array` - Array with the following properties:

  1.`DATA`, 32 Bytes - Hash of the block.

  2.`DATA` - Unused.

  3.`DATA` - Unused.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"method": "eth_getWork",
	"params": [],
	"id": 73
}'
```

Response

```json
{
	"jsonrpc": "2.0",
	"id": 73,
	"result": ["0x00000000020e73915413df0c816e327dc4b9d17069887aef1fff0e854f8d9ad0", null, null]
}
```
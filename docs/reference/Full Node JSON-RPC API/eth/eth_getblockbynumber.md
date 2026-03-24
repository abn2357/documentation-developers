---
title: eth_getBlockByNumber
excerpt: Fetches the block object associated with the provided block number.
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

1. `QUANTITY|TAG` - Block number (integer) or a string tag (`earliest`, `latest`).
2. `Boolean` - If `true`, returns full transaction objects; if `false`, returns only the transaction hashes.

**Returns**

* `Object` - A block object, or `null` if the specified block cannot be found. See [eth_getBlockByHash](https://developers.tron.network/reference#eth_getblockbyhash)

<br />

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"method": "eth_getBlockByNumber",
	"params": ["0xF9CC56", true],
	"id": 1
}'
```

Response

```json
{"jsonrpc":"2.0","id":1,"result":null}
```

---
title: eth_syncing
excerpt: Returns an object with data about the sync status of the node.
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

* `Object|Boolean` - An object with sync status data or FALSE, when not syncing, the items in the object include:

  | Item Name       | Data Type  | Description                                                                                  |
  | :-------------- | :--------- | :------------------------------------------------------------------------------------------- |
  | `startingBlock` | `QUANTITY` | The block at which the import started (will only be reset, after the sync reaches its head). |
  | `currentBlock`  | `QUANTITY` | Current block.                                                                               |
  | `highestBlock`  | `QUANTITY` | Estimated highest block.                                                                     |

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":64}'
```

Response

```json
{
	"jsonrpc": "2.0",
	"id": 64,
	"result": {
		"startingBlock": "0x20e76cc",
		"currentBlock": "0x20e76df",
		"highestBlock": "0x20e76e0"
	}
}
```
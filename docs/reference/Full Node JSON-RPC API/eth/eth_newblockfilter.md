---
title: eth_newBlockFilter
excerpt: >-
  Creates a new block filter on the node, enabling clients to be notified when a
  new block arrives.
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

* `QUANTITY` - ID of the filter.

<br />

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
    "jsonrpc": "2.0",
    "method": "eth_getFilterChanges",
    "params": [
        "0xc11a84d5e906ecb9f5c1eb65ee940b154ad37dce8f5ac29c80764508b901d996"
    ],
    "id": 71
}'
```

Response

```json
{
    "jsonrpc": "2.0",
    "id": 71,
    "error": {
        "code": -32000,
        "message": "filter not found",
        "data": "{}"
    }
}
```

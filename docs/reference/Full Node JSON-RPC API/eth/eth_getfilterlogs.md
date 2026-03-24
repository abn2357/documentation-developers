---
title: eth_getFilterLogs
excerpt: Returns all log objects that match the filter identified by the given ID.
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

1. `QUANTITY` - ID of the filter.

**Returns**

* See [eth_getFilterChanges](/reference/eth_getfilterchanges).

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
    "jsonrpc": "2.0",
    "method": "eth_getFilterLogs",
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

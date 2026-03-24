---
title: eth_uninstallFilter
excerpt: >-
  Uninstalls the filter by the given ID. It should always be called when the
  filter is no longer required. Filters automatically time out if they are not
  queried using `eth_getFilterChanges` within a certain period.
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

* `Boolean` - Return `ture` if the filter was successfully uninstalled, otherwise `false`.

<br />

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
    "jsonrpc": "2.0",
    "method": "eth_uninstallFilter",
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
    "result": true
}
```

---
title: eth_gasPrice
excerpt: Returns the current energy price in sun.
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

* `QUANTITY` - Integer of the current Energy price. (Unit: sun)

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"jsonrpc": "2.0", "id": 1, "method": "eth_gasPrice", "params": []}'
```

Response

```json
{"jsonrpc":"2.0","id":1,"result":"0x8c"}
```

---
title: web3_clientVersion
excerpt: Returns the current client version.
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

* `String` - Current client version.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"jsonrpc": "2.0", "id": 1, "method": "web3_clientVersion", "params": []}'
```

Response

```json
{"jsonrpc":"2.0","id":1,"result":"TRON/v4.3.0/Linux/Java1.8/GreatVoyage-v4.2.2.1-281-gc1d9dfd6c"}
```

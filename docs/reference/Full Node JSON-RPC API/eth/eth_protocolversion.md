---
title: eth_protocolVersion
excerpt: Returns the java-tron block version.
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

* `String` - The current java-tron block version.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"jsonrpc":"2.0","method":"eth_protocolVersion","params":[],"id":64}'
```

Response

```json
{"jsonrpc":"2.0","id":64,"result":"0x16"}
```
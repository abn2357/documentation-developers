---
title: net_version
excerpt: Returns the hash of the genesis block.
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

* `String` - Hash of genesis block.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"jsonrpc":"2.0","method":"net_version","params":[],"id":64}'
```

Response

```json
{"jsonrpc":"2.0","id":64,"result":"0x2b6653dc"}
```

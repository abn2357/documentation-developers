---
title: net_peerCount
excerpt: Returns the number of peers currently connected to the client.
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

* `QUANTITY` - Integer value representing the number of connected peers.

<br />

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"jsonrpc":"2.0","method":"net_peerCount","params":[],"id":64}'
```

Response

```json
{"jsonrpc":"2.0","id":64,"result":"0x9"}
```

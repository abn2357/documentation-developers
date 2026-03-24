---
title: net_listening
excerpt: >-
  Returns `ture` if the client is currently listening for incoming network
  connections.
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

* `Boolean` - Returns `true` when the client is listening; otherwise `false`.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"jsonrpc":"2.0","method":"net_listening","params":[],"id":64}'
```

Response

```json
{"jsonrpc":"2.0","id":64,"result":true}
```

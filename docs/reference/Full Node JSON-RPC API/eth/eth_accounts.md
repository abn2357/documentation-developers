---
title: eth_accounts
excerpt: 'Returns a list of addresses owned by the client. '
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

* `Array` - Empty list. In TRON, this API always returns an empty list.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '
{"jsonrpc": "2.0", "id": 1, "method": "eth_accounts", "params": []}'
```

Response

```json
{"jsonrpc":"2.0","id":1,"result":[]}
```

<br />

<br />

<br />

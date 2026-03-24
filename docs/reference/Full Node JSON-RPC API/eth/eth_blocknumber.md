---
title: eth_blockNumber
excerpt: Returns the number of the most recent block.
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

* `QUANTITY` - Latest block number.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":64}'
```

Response

```
{"jsonrpc":"2.0","id":64,"result":"0x20e0cf0"}
```

<br />

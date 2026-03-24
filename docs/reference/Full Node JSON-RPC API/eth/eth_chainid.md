---
title: eth_chainId
excerpt: Returns chainId, which is the last 4 bytes of the genesis block hash.
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

* `DATA` - The chainId of the TRON network.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":79}'
```

Response

```json
{"jsonrpc":"2.0","id":79,"result":"0x2b6653dc"}
```
---
title: eth_coinbase
excerpt: Returns the Super Representative (SR) address of the current node.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Parameters**  
None

**Returns**

* `DATA` -  The node's SR address.
  * If multiple SR addresses are configured, the first one is returned.
  * If no valid SR address is configured or the address has not produced any blocks, an error is returned: `etherbase must be explicitly specified`.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"jsonrpc": "2.0", "id": 1, "method": "eth_coinbase", "params": []}'
```

Response

```json
{"jsonrpc":"2.0","id":1,"error":{"code":-32000,"message":"etherbase must be explicitly specified","data":"{}"}}
```

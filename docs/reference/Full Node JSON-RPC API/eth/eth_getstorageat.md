---
title: eth_getStorageAt
excerpt: >-
  Returns the value from a storage position at a given address. It can be used
  to get the value of a variable in a contract.
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

1. `DATA`, 20 Bytes - Address.
2. `QUANTITY` - Integer of the position in the storage.
3. `QUANTITY|TAG` - Block number, currently only supports "latest".

**Returns**

* `DATA` - The value at this storage position.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"method": "eth_getStorageAt",
	"params": ["0xE94EAD5F4CA072A25B2E5500934709F1AEE3C64B", "0x29313b34b1b4beab0d3bad2b8824e9e6317c8625dd4d9e9e0f8f61d7b69d1f26", "latest"],
	"id": 1
}'
```

Response

```json
{"jsonrpc":"2.0","id":1,"result":"0x0000000000000000000000000000000000000000000000000000000000000000"}
```

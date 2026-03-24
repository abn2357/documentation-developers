---
title: eth_call
excerpt: >-
  Executes a message call immediately in a read-only manner without creating a
  transaction on the blockchain (functionally equivalent to
  [triggerConstantContract](/reference/triggerconstantcontract)).
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

1. `Object` - The transaction call object, The fields in the object include:

   | Item Name  | Data Type        | Description                                                                             |
   | :--------- | :--------------- | :-------------------------------------------------------------------------------------- |
   | `from`     | `DATA`, 20 Bytes | Caller address, using TRON's hexadecimal address format with the `41` prefix removed.   |
   | `to`       | `DATA`, 20 Bytes | Contract address, using TRON's hexadecimal address format with the `41` prefix removed. |
   | `gas`      | `QUANTITY`       | Not supported in TRON; must be set to `0x0`.                                            |
   | `gasPrice` | `QUANTITY`       | Not supported in TRON; must be set to `0x0`.                                            |
   | `value`    | `QUANTITY`       | Not supported in TRON; must be set to `0x0`.                                            |
   | `data`     | `DATA`           | Function selector along with ABI-encoded parameters.                                    |
2. `QUANTITY|TAG` - Block number or block identifier; currently, only `"latest"` is supported.

**Returns**

* `DATA` - The result returned from executing the contract function.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"method": "eth_call",
	"params": [{
		"from": "0xF0CC5A2A84CD0F68ED1667070934542D673ACBD8",
		"to": "0x70082243784DCDF3042034E7B044D6D342A91360",
		"gas": "0x0",
		"gasPrice": "0x0",
		"value": "0x0",
		"data": "0x70a08231000000000000000000000041f0cc5a2a84cd0f68ed1667070934542d673acbd8"
	}, "latest"],
	"id": 1
}'
```

Response

```json
{"jsonrpc":"2.0","id":1,"result":"0x"}
```

---
title: eth_estimateGas
excerpt: Estimates Estimates the Energy consumption required for a transaction.
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

1. `Object` - Transaction call object containing the following fields:

   | Item Name  | Data Type        | Description                                                         |
   | :--------- | :--------------- | :------------------------------------------------------------------ |
   | `from`     | `DATA`, 20 Bytes | Sender's address.                                                   |
   | `to`       | `DATA`, 20 Bytes | Receiver's address.                                                 |
   | `gas`      | `QUANTITY`       | Fee limit. Retained for Ethereum compatibility; ignored by TRON.    |
   | `gasPrice` | `QUANTITY`       | Energy price. Retained for Ethereum compatibility; ignored by TRON. |
   | `value`    | `QUANTITY`       | Amount of TRX sent via `call_value`. (Unit: sun)                    |
   | `data`     | `DATA`           | Function selector along with ABI-encoded parameters.                |

**Returns**

* `QUANTITY` - Amount of Energy used.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "eth_estimateGas",
	"params": [{
		"from": "0x41F0CC5A2A84CD0F68ED1667070934542D673ACBD8",
		"to": "0x4170082243784DCDF3042034E7B044D6D342A91360",
		"gas": "0x01",
		"gasPrice": "0x8c",
		"value": "0x01",
		"data": "0x70a08231000000000000000000000041f0cc5a2a84cd0f68ed1667070934542d673acbd8"
	}]
}'
```

Response

```json
{"jsonrpc":"2.0","id":1,"result":"0x0"}
```

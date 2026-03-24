---
title: eth_getLogs
excerpt: Returns an array of all logs that match the given filter object.
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

1. `Object` - The filter options, which include the following fields:

   | Field       | Type                    | Description                                                                                                                                                                                                                                                                             |
   | :---------- | :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `fromBlock` | `QUANTITY\|TAG`         | (optional, default: `"latest"`) The block number from which to start searching for logs, or `"latest"` for the most recently mined block.                                                                                                                                               |
   | `toBlock`   | `QUANTITY\|TAG`         | (optional, default: `"latest"`) The block number at which to stop searching for logs, or `"latest"` for the most recently mined block.                                                                                                                                                  |
   | `address`   | `DATA\|Array`, 20 Bytes | (optional) A contract address or a list of addresses from which logs should originate.                                                                                                                                                                                                  |
   | `topics`    | `DATA[]`                | (optional) An array of 32-byte DATA topics. Topics are order-dependent. Each topic may also be an array of DATA representing "or" options.                                                                                                                                              |
   | `blockHash` | `DATA`, 32 Bytes        | (optional) Restricts the logs returned to a single block identified by this 32-byte hash. Using `blockHash` is equivalent to setting `fromBlock` and `toBlock` to the block number of the referenced block. If `blockHash` is provided, `fromBlock` and `toBlock` must not be included. |

**Returns**

* See [eth_getFilterChanges](/reference/eth_getfilterchanges).

<br />

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"jsonrpc":"2.0","method":"eth_getLogs","params":[{"address":["cc2e32f2388f0096fae9b055acffd76d4b3e5532","E518C608A37E2A262050E10BE0C9D03C7A0877F3"],"fromBlock":"0x989680","toBlock":"0x9959d0","topics":["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",null,["0x0000000000000000000000001806c11be0f9b9af9e626a58904f3e5827b67be7","0x0000000000000000000000003c8fb6d064ceffc0f045f7b4aee6b3a4cefb4758"]]}],"id":1}'
```

Response

```json
{
    "jsonrpc": "2.0",
    "id": 71,
    "result": []
}
```

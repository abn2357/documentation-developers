---
title: eth_getFilterChanges
excerpt: >-
  Polling method for a filter, which returns an array of logs which occurred
  since last poll.
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

1. `QUANTITY` - ID of the filter.

**Returns**

* For filters created with `eth_newFilter`, returns a list of log Objects. Each log object contains the following fields:

  | Field              | Type             | Description                                                                                |
  | :----------------- | :--------------- | :----------------------------------------------------------------------------------------- |
  | `removed`          | `TAG`            | `true` if the log was removed due to a chain reorganization; `false` if it is a valid log. |
  | `logIndex`         | `QUANTITY`       | Index position of the log in the block. `null` if the log is pending.                      |
  | `transactionIndex` | `QUANTITY`       | Index position of the transaction that created the log. `null` if the log is pending.      |
  | `transactionHash`  | `DATA`, 32 Bytes | Hash of the transaction from which this log was generated.                                 |
  | `blockHash`        | `DATA`, 32 Bytes | Hash of the block containing this log. `null` if the log is pending.                       |
  | `blockNumber`      | `QUANTITY`       | Block number containing this log.                                                          |
  | `address`          | `DATA`, 32 Bytes | Address from which this log originated.                                                    |
  | `data`             | `DATA`           | Contains one or more 32-byte non-indexed arguments of the log.                             |
  | `topics`           | `DATA[]`         | An array of event topics and indexed arguments.                                            |
* For filters created with `eth_newBlockFilter`, the return value is an array of block hashes (`DATA`, 32 bytes each).

<br />

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
    "jsonrpc": "2.0",
    "method": "eth_getFilterChanges",
    "params": [
        "0xc11a84d5e906ecb9f5c1eb65ee940b154ad37dce8f5ac29c80764508b901d996"
    ],
    "id": 71
}'
```

Response

```json
{
    "jsonrpc": "2.0",
    "id": 71,
    "error": {
        "code": -32000,
        "message": "filter not found",
        "data": "{}"
    }
}
```

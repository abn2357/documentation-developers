---
title: BroadcastTransaction
excerpt: Broadcasts a signed transaction to the network.
api:
  file: full-node-http-api.json
  operationId: broadcasttransaction
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Returns**

| Field   | Type    | Description                                                                                             |
| :------ | :------ | :------------------------------------------------------------------------------------------------------ |
| result  | boolean | Whether the broadcast was successful. `true` - successful; `false` - failed. (Field omitted in result). |
| txid    | string  | The transaction hash.                                                                                   |
| code    | string  | Error code indicating the result.                                                                       |
| message | string  | Detailed error information.                                                                             |
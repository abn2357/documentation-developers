---
title: CreateTransaction
excerpt: >-
  Creates a TRX transfer transaction. If the recipient account (to_address) does
  not exist, it will be automatically activated.
api:
  file: full-node-http-api.json
  operationId: createtransaction
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

Returns an unsigned transaction JSON object. Refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the field definitions. For the `TransferContract type`, the `raw_data.contract[0].parameter.value` fields are:

| Field         | Type   | Description                                                    |
| :------------ | :----- | :------------------------------------------------------------- |
| owner_address | string | Sender address.                                                |
| to_address    | string | Recipient address                                              |
| amount        | int64  | Amount of TRX to transfer. (Unit: sun, 1 TRX = 1,000,000 sun). |

<br />
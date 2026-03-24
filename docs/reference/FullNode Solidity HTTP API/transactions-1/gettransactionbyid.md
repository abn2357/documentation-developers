---
title: GetTransactionById
excerpt: Queries transaction information by transaction id. (Confirmed)
api:
  file: full-node-http-api.json
  operationId: gettransactionbyid
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
**Returns**

A transaction object, which contains the following fields:

| Field          | Type     | Description                                                                                                   |
| :------------- | :------- | :------------------------------------------------------------------------------------------------------------ |
| `ret`          | Result[] | Transaction Execution Results                                                                                 |
| `txID`         | string   | Transaction ID (Hash).                                                                                        |
| `raw_data`     | object   | Transaction content. See [here](https://developers.tron.network/docs/tron-protocol-transaction)  for details. |
| `signature`    | string[] | Transaction signature.                                                                                        |
| `raw_data_hex` | string   | The transaction's raw data. (Format: hex)                                                                     |

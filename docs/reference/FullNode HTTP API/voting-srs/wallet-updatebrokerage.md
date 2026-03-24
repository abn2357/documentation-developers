---
title: UpdateBrokerage
excerpt: Update the SR's brokerage setting
api:
  file: full-node-http-api.json
  operationId: wallet-updatebrokerage
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

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `UpdateBrokerageContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field         | Type   | Description                                     |
| :------------ | :----- | :---------------------------------------------- |
| owner_address | string | Super Representative (SR) address.              |
| brokerage     | int32  | Dividend ratio, from 0 to 100, 1 represents 1%. |
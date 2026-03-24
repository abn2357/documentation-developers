---
title: UpdateAccount
excerpt: Modify the name of an account.
api:
  file: full-node-http-api.json
  operationId: updateaccount
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

Transaction - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `AccountUpdateContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field         | Type   | Description      |
| :------------ | :----- | :--------------- |
| owner_address | string | Account address. |
| account_name  | string | Account name.    |
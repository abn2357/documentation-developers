---
title: ExchangeCreate
excerpt: Creates a trading pair
api:
  file: full-node-http-api.json
  operationId: exchangecreate
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ❗️ Warning!
>
> Successful execution, signing, and broadcast of this API call will deduct 1024 TRX from the user's account.

**Returns**

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `ExchangeCreateContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field                | Type   | Description                                          |
| :------------------- | :----- | :--------------------------------------------------- |
| owner_address        | string | Account address.                                     |
| first_token_id       | string | ID of the first token in the DEX trading pair.       |
| first_token_balance  | int64  | Balance of the first token in the DEX trading pair.  |
| second_token_id      | string | ID of the second token in the DEX trading pair.      |
| second_token_balance | int64  | Balance of the second token in the DEX trading pair. |
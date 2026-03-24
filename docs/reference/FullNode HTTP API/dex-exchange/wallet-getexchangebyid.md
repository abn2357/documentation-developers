---
title: GetExchangeById
excerpt: Query exchange pair based on id
api:
  file: full-node-http-api.json
  operationId: wallet-getexchangebyid
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

| Field                | Type   | Description                                          |
| :------------------- | :----- | :--------------------------------------------------- |
| exchange_id          | int64  | ID of the DEX trading pair.                          |
| creator_address      | string | Creator address.                                     |
| create_time          | int64  | Creation time.                                       |
| first_token_id       | string | ID of the first token in the DEX trading pair.       |
| first_token_balance  | int64  | Balance of the first token in the DEX trading pair.  |
| second_token_id      | string | ID of the second token in the DEX trading pair.      |
| second_token_balance | int64  | Balance of the second token in the DEX trading pair. |
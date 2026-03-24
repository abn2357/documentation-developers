---
title: ExchangeInject
excerpt: >-
  Injects capital into the trading pair. The purpose of injecting capital into
  the trading pair is to prevent price fluctuation from affecting the
  transaction.
api:
  file: full-node-http-api.json
  operationId: exchangeinject
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

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `ExchangeInjectContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field         | Type   | Description                                            |
| :------------ | :----- | :----------------------------------------------------- |
| owner_address | string | Transaction initiator address. (Format: Base58 or Hex) |
| exchange_id   | int64  | ID of the DEX trading pair.                            |
| token_id      | string | ID of the token to inject.                             |
| quant         | int64  | Amount of tokens to inject from a DEX trading pair.    |

<br />
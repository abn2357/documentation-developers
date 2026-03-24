---
title: UnfreezeBalance
excerpt: >-
  Unstake the TRX staked during Stake1.0, release the obtained bandwidth or
  energy and TP. This operation will cause automatically cancel all votes.
api:
  file: full-node-http-api.json
  operationId: account-resources-unfreezebalance
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

Transaction - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `UnfreezeBalanceContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field            | Type   | Description                                     |
| :--------------- | :----- | :---------------------------------------------- |
| owner_address    | string | Transaction initiator address.                  |
| resource         | string | Type of resource. (Enum: `BANDWIDTH`, `ENERGY`) |
| receiver_address | string | Resource receiver address.                      |
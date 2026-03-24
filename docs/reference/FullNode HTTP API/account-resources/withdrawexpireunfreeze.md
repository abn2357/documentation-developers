---
title: WithdrawExpireUnfreeze
excerpt: >-
  Withdraw unfrozen balance in Stake2.0,  the user can call this API to get back
  their funds after executing /wallet/unfreezebalancev2 transaction and waiting
  N days, N is a network parameter.
api:
  file: full-node-http-api.json
  operationId: withdrawexpireunfreeze
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Note: Stake 2.0 supports multiple partial unstakes. Through this API, all unstaked funds that have passed the N-day lock-up period will be withdrawn at one time.

**Returns**  
Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `WithdrawExpireUnfreezeContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field         | Type   | Description                    |
| :------------ | :----- | :----------------------------- |
| owner_address | string | Transaction initiator address. |
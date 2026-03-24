---
title: WithdrawBalance
excerpt: >-
  Super Representative or user withdraw rewards, usable every 24 hours.

  Super representatives can withdraw the balance from the account allowance into
  the account balance,

  Users can claim the voting reward from the SRs and deposit into his account
  balance.
api:
  file: full-node-http-api.json
  operationId: withdrawbalance
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

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `WithdrawBalanceContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field          | Type   | Description     |
| :------------- | :----- | :-------------- |
| owner\_address | string | Account address |
---
title: CancelAllUnfreezeV2
excerpt: >-
  Cancel unstakings, all unstaked funds still in the waiting period will be
  re-staked, all unstaked funds that exceeded the 14-day waiting period will be
  automatically withdrawn to the owner’s account.
api:
  file: full-node-http-api.json
  operationId: cancelallunfreezev2
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
When canceling unstakings, all unstaked funds still in the waiting period will be re-staked, and the resource obtained through the re-staking remains the same as before. Unstakings that exceeded the 14-day waiting period cannot be canceled, and this part of the unstaked funds will be automatically withdrawn to the owner’s account. The users can use `wallet/gettransactioninfobyid` to query the amount of unstaking TRX that canceled (`cancel_unfreezeV2_amount`) and the amount of unstaked TRX withdrawn to the  account (`withdraw_expire_amount `).

**Returns**

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `CancelAllUnfreezeV2Contract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field         | Type   | Description                    |
| :------------ | :----- | :----------------------------- |
| owner_address | string | Transaction initiator address. |
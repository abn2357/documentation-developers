---
title: UnfreezeBalanceV2
excerpt: >-
  Unstake some TRX staked in Stake2.0, release the corresponding amount of
  bandwidth or energy, and voting rights (TP).
api:
  file: full-node-http-api.json
  operationId: unfreezebalancev2-1
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Unlock the TRX staked at the Stake 2.0 stage through this interface. After unstaking, the user needs to wait for 14 days before calling the [/wallet/withdrawexpireunfreeze](/reference/withdrawexpireunfreeze) interface to withdraw the funds of this unstaking.

When executing unstaking, if there is a previously unstaked funds that has passed the lock-up period, then this unstaking operation will also withdraw the unstaked funds that has passed the lock-up period to the account at the same time. You can query the amount of funds withdrawn in this transaction through [gettransactioninfobyid](/reference/gettransactioninfobyid) API.

**Returns**

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `UnfreezeBalanceV2Contract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field            | Type   | Description                                     |
| :--------------- | :----- | :---------------------------------------------- |
| owner_address    | string | Transaction initiator address.                  |
| resource         | string | Type of resource. (Enum: `BANDWIDTH`, `ENERGY`) |
| unfreeze_balance | int64  | Amount of TRX to unstake. (Unit: sun)           |

---
title: FreezeBalanceV2
excerpt: >-
  In Stake2.0, stake an amount of TRX to obtain bandwidth or energy, and obtain
  equivalent TRON Power(TP) according to the staked amount.
api:
  file: full-node-http-api.json
  operationId: freezebalancev2-1
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

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `FreezeBalanceV2Contract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field          | Type   | Description                                       |
| :------------- | :----- | :------------------------------------------------ |
| owner_address  | string | Transaction initiator address.                    |
| resource       | string | Type of resource. (Enum: `BANDWIDTH`, `ENERGY`)   |
| frozen_balance | int64  | Amount of TRX to stake. (Unit: sun, in Stake 2.0) |

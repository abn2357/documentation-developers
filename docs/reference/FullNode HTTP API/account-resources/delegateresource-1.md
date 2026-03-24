---
title: DelegateResource
excerpt: Delegate bandwidth or energy resources to other accounts in Stake2.0.
api:
  file: full-node-http-api.json
  operationId: delegateresource-1
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
Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `DelegateResourceContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field            | Type   | Description                                                                                                     |
| :--------------- | :----- | :-------------------------------------------------------------------------------------------------------------- |
| owner_address    | string | Transaction initiator address.                                                                                  |
| resource         | string | Type of resource. (Enum: `BANDWIDTH`, `ENERGY`)                                                                 |
| receiver_address | string | Resource receiver address.                                                                                      |
| balance          | Int64  | Amount of TRX for resource delegation. (Unit: sun)                                                              |
| lock             | bool   | Whether to lock the resource delegation. If `true`, the delegation cannot be canceled during the `lock_period`. |
| lock_period      | Int64  | Lock duration in blocks (1 block ≈ 3 seconds). Only valid if `lock` is `true`. (e.g., 1 day = 28800)            |
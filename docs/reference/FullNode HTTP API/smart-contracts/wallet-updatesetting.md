---
title: UpdateSetting
excerpt: Update the smart contract's `consume_user_resource_percent` parameter.
api:
  file: full-node-http-api.json
  operationId: wallet-updatesetting
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

Returned Object: **Transaction (Unsigned).

General Fields: Refer to the [Transaction](/docs/tron-protocol-transaction) section.

`UpdateSettingContract` Specific Fields: The `raw_data.contract[0].parameter.value` within the transaction contains parameters for the contract invocation:

| Field                         | Type   | Description                                                                  |
| :---------------------------- | :----- | :--------------------------------------------------------------------------- |
| owner_address                 | string | Transaction initiator address.(Format: Base58 or Hex)                        |
| contract_address              | string | Contract address. (Format: Base58 or Hex)                                    |
| consume_user_resource_percent | int64  | Percentage of user Energy consumption for a smart contract. (Range: [0-100]) |

<br />
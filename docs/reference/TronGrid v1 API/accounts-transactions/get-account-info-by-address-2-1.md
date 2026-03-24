---
title: '[Layered table]Get account info by address'
api:
  file: trongrid-v1-api.json
  operationId: get_v1accounts{address}-2-1
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
**Returns**

| Root           | Object/Array            | Field                            | Nested         | Type    | Description                                                 |
| :------------- | :---------------------- | :------------------------------- | :------------- | :------ | :---------------------------------------------------------- |
| <b>success</b> |                         |                                  |                | Boolean | Whether the request was successful.                         |
| <b>meta</b>    | at                      |                                  |                | Long    | The response timestamp. (Unit: millisecond)                 |
|                | page_size               |                                  |                | Integer | The number of items returned on the current page.           |
| <b>data</b>    | address                 |                                  |                | String  | Account address. (Format: hex)                              |
|                | balance                 |                                  |                | Long    | TRX balance. (Unit: sun)                                    |
|                | account_name            |                                  |                | String  | Account name.                                               |
|                | is_witness              |                                  |                | Boolean | Indicates if the account is an SR, SR Partner or candidate. |
|                | <b>account_resource</b> | energy_usage                     |                | Long    | The amount of Energy used.                                  |
|                |                         | energy_window_size               |                | Long    | Duration in blocks for Energy recovery.                     |
|                |                         | <b>frozen_balance_for_energy</b> | frozen_balance | Long    | TRX staked for Energy. (Stake 1.0)                          |
|                |                         |                                  | expire_time    | Long    | Timestamp for unstake availability. (Stake 1.0)             |
|                | <b>frozen[]</b>         | frozen_balance                   |                | Long    | TRX staked for Bandwidth. (Stake 1.0)                       |
|                | <b>frozenV2[]</b>       | amount                           |                | Long    | Total TRX staked for resource in Stake 2.0.                 |
|                |                         | type                             |                | String  | Resource type (BANDWIDTH/ENERGY).                           |
|                | <b>owner_permission</b> | permission_name                  |                | String  | Owner permission name.                                      |
|                |                         | <b>keys[]</b>                    | address        | String  | Address associated with the permission.                     |
|                |                         |                                  | weight         | Integer | Signature weight of the address.                            |
|                | <b>assetV2[]</b>        | key                              |                | String  | TRC-10 Token ID.                                            |
|                |                         | value                            |                | Long    | TRC-10 Token balance.                                       |

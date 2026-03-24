---
title: GetDelegatedResourceV2
excerpt: >-
  [Stake 2.0] Returns the resource delegations from a specific address to a
  target address (solidified state).
api:
  file: full-node-solidity-http-api.json
  operationId: post_walletsoliditygetdelegatedresourcev2
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
**Returns**  
`delegatedResource` - List\<DelegatedResource>: A list of resource delegations from a specific address to target addresses.

A `DelegatedResource` object contains the following fields:

| Field                          | Type   | Description                                                                                           |
| :----------------------------- | :----- | :---------------------------------------------------------------------------------------------------- |
| `from`                         | string | Delegator account address. (Format: Base58 or Hex)                                                    |
| `to`                           | string | Recipient account address. (Format: Base58 or Hex)                                                    |
| `frozen_balance_for_bandwidth` | int64  | Amount of staked TRX delegated from the `from` address to the `to` address for Bandwidth. (Unit: sun) |
| `frozen_balance_for_energy`    | int64  | Amount of staked TRX delegated from the `from` address to the `to` address for Energy. (Unit: sun)    |
| `expire_time_for_bandwidth`    | int64  | Expiration timestamp of the Bandwidth delegation lock. (Unit: milliseconds)                           |
| `expire_time_for_energy`       | int64  | Expiration timestamp of the Energy delegation lock. (Unit: milliseconds)                              |

Note: If a field value is `0` or empty, it will not be displayed in the returned results.

Regarding the delegation expiration time, if a 3-day lock is not specified when delegating the resource, `expire_time_for_bandwidth` or `expire_time_for_energy` will be `0`.

<br />
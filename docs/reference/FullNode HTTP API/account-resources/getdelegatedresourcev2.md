---
title: GetDelegatedResourceV2
excerpt: >-
  In Stake2.0, query the detail of resource share delegated from fromAddress to
  toAddress.
api:
  file: full-node-http-api.json
  operationId: getdelegatedresourcev2
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
delegatedResource - List\<DelegatedResource>: Resource delegation list, each resource delegation information includes below fields:

| Field                        | Type   | Description                                                                                           |
| :--------------------------- | :----- | :---------------------------------------------------------------------------------------------------- |
| from                         | string | Delegate account address.                                                                             |
| to                           | string | Resource recipient address.                                                                           |
| frozen_balance_for_bandwidth | int64  | Amount of TRX staked for Bandwidth delegated from the `from` address to the `to` address. (Unit: sun) |
| frozen_balance_for_energy    | int64  | Amount of TRX staked for energy delegated from the `from` address to the `to` address. (Unit: sun)    |
| expire_time_for_bandwidth    | int64  | Timestamp when the Bandwidth delegation lock expires. (Unit: millisecond)                             |
| expire_time_for_energy       | int64  | Timestamp when the energy delegation lock expires. (Unit: millisecond)                                |

Note that if the field value is 0 or null, the field will not be displayed in the returned result. For delegation deadlines, expire_time_for_bandwidth or expire_time_for_energy will be 0 if no lock is specified when delegating resources, and does not been displayed.
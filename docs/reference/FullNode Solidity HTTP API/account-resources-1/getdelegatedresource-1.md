---
title: GetDelegatedResource
excerpt: >-
  Returns all resources delegations during stake 1.0 phase from an account to
  another account. The fromAddress can be retrieved from the
  GetDelegatedResourceAccountIndex API. (Confirmed state)
api:
  file: full-node-http-api.json
  operationId: getdelegatedresource-1
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
`delegatedResource` - List\<DelegatedResource>: A list of resources that an address delegates to a target address. A `DelegatedResource` object contains the following fields:

| Field                          | Type   | Description                                                               |
| :----------------------------- | :----- | :------------------------------------------------------------------------ |
| `from`                         | string | Delegate account address.                                                 |
| `to`                           | string | Resource receiver account address.                                        |
| `frozen_balance_for_bandwidth` | int64  | Bandwidth delegate share. (Unit: sun)                                     |
| `frozen_balance_for_energy`    | int64  | Energy delegate share. (Unit: sun)                                        |
| `expire_time_for_bandwidth`    | int64  | Timestamp when the Bandwidth delegation lock expires. (Unit: millisecond) |
| `expire_time_for_energy`       | int64  | Timestamp when the energy delegation lock expires. (Unit: millisecond)    |
